console.log("hello fontparts")

// const sidebar = document.querySelector("#sidebar")

// console.log(sidebar.classList)

function collapseSidebar() {
    var sidebar = document.querySelector('#sidebar');
    
    if (sidebar != null) {
        sidebar.classList.add('collapsed')
    }
};

window.addEventListener('DOMContentLoaded', function() {
    console.log('window - DOMContentLoaded - capture');
    collapseSidebar()

    var navButton = document.querySelector('#nav-button');
    navButton.addEventListener('click', toggleNav)
}, true);

function toggleNav() {
    console.log('nav icon clicked');
    var sidebar = document.querySelector('#sidebar');
    sidebar.classList.toggle('expanded')
}