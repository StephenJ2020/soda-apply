// global variables

<<<<<<< HEAD
=======
const current_page = window.location.pathname;
const navLinks = document.querySelectorAll(".nav-link");
let activeId = "";
let navLink_ids = [];

// Navbar JS

for(let i = 0; i < navLinks.length; i++) {
    navLink_ids.push(navLinks[i].id);
}

switch (current_page) {
    /**
     * Switch statement to handle currently active page
     * in Navbar and highlight to user via append of
     * class "active" to nav-link list item, with addition
     * of "aria-current-page" attribute for current visually
     * styled item.
     * 
     */
    case '/':
        activeId = navLink_ids[0];

        if (navLink_ids.includes(activeId)) {
            navLinks[0].classList.add('active');
            navLinks[0].setAttribute('aria-current-page', 'page');
        }
        break;
    case '/jobs':
        activeId = navLink_ids[1];

        if (navLink_ids.includes(activeId)) {
            navLinks[1].classList.add('active');
            navLinks[1].setAttribute('aria-current-page', 'page');
        }
        break;
    case '/profile':
        activeId = navLink_ids[2];

        if (navLink_ids.includes(activeId)) {
            navLinks[2].classList.add('active');
            navLinks[2].setAttribute('aria-current-page', 'page');
        }
        break;
    case '/user_registration':
        activeId = navLink_ids[3];

        if (navLink_ids.includes(activeId)) {
            navLinks[3].classList.add('active');
            navLinks[3].setAttribute('aria-current-page', 'page');
        }
        break;
    case '/login':
        activeId = navLink_ids[4];

        if (navLink_ids.includes(activeId)) {
            navLinks[4].classList.add('active');
            navLinks[4].setAttribute('aria-current-page', 'page');
        }
        break;
    default:
        activeId = navLink_ids[5];

        if (navLink_ids.includes(activeId)) {
            navLinks[5].classList.add('active');
            navLinks[5].setAttribute('aria-current-page', 'page');
        }
        break;  
};
>>>>>>> ccb84ac7169c0f2b84dacc3e94723da33bda09d7
