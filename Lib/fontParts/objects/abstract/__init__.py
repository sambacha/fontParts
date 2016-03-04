"""
The goal is to define a very clean scripting API
that preserves the main functionality of RoboFab.
Say something about the importance of script
portability. Designers have workflows and specific
binary requirements, etc.

Things that should be considered for removal:
- anything that does anything too magical.
- anything that was originally implemented for
  environment specific reasons.
- anything that was designed as a speed optimization.

Things that haven't been defined, but should.
- a common error instead of relying on the environment
  errors. those often differ from environment
  to environment and that's a portability problem.
- what errors should be raised by each method
- an interpolation method for all realistic objects.
  this way font.interpolate can just iterate through
  those.
- classes for subobjects need to be declared in the
  parent objects.
- the class to use for a copy operation needs to
  be defined for each object that has a copy method.

Things that we should consider adding:
- a naming convention for environment specific
  things. for example, it would be bad if two
  environments defined "makeMyFont" but they took
  different arguments and did different things.
- a parent tree system like in defcon. this would
  replace the fragile getParent.
"""
