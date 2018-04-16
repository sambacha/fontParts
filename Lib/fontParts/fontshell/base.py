class RBaseObject(object):

    wrapClass = None

    def _init(self, wrap=None):
        if wrap is None and self.wrapClass is not None:
            wrap = self.wrapClass()
        if wrap is not None:
            self._wrapped = wrap

    def naked(self):
        if hasattr(self, "_wrapped"):
            return self._wrapped
        return None


class RSubscribableMixin(object):

    _defconNotifications = []

    def _beginObservingWrappedObject(self):
        if not hasattr(self, "_subscriberProxy"):
            self._subscriberProxy = _SubscriberProxy(self)
        for notification in self._defconNotifications:
            self._wrapped.addObserver(
                observer=self._subscriberProxy,
                methodName="notificationPassThrough",
                notification=notification
            )

    def _stopObservingWrappedObject(self):
        for notification in self._defconNotifications:
            self._wrapped.removeObserver(
                observer=self._subscriberProxy,
                notification=notification
            )

    def _wrappedObjectNotificationCallback(self, notification):
        if notification.name.endswith(".Changed"):
            self.makeAnnouncement()


class _SubscriberProxy(object):

    """
    This proxy is needed because the fontParts objects
    __hash__ uses id(object.naked()). This means that
    if there are two fontParts wrappers around the same
    object, the two fontParts objects will have the same
    hash id. defcon's notification system only allows
    one subscription per (observer + notificationName).
    So, if two wrappers exist, the subscription triggers
    a traceback. This proxy will be unique to each wrapper
    and will thus conform to defcon's system.
    """

    def __init__(self, obj):
        import weakref
        self._object = weakref.ref(obj)

    def notificationPassThrough(self, notification):
        obj = self._object()
        if obj is not None:
            obj._wrappedObjectNotificationCallback(notification)