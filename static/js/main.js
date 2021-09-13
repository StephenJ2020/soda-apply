// global variables

const current_page = window.location.pathname;
const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
let activeId = "";
let navLink_ids = [];

// Navbar JS

for(let i = 0; i < navLinks.length; i++) {
    navLink_ids.push(navLinks[i].id);
};

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
            navLinks[0].setAttribute('aria-current', 'page');
        }
        break;
    case '/job_listings':
        activeId = navLink_ids[1];

        if (navLink_ids.includes(activeId)) {
            navLinks[1].classList.add('active');
            navLinks[1].setAttribute('aria-current', 'page');
        }
        break;
    case '/profile':
        activeId = navLink_ids[2];

        if (navLink_ids.includes(activeId)) {
            navLinks[2].classList.add('active');
            navLinks[2].setAttribute('aria-current', 'page');
        }
        break;
    case '/user_registration':
        activeId = navLink_ids[3];

        if (navLink_ids.includes(activeId)) {
            navLinks[3].classList.add('active');
            navLinks[3].setAttribute('aria-current', 'page');
        }
        break;
    case '/login':
        activeId = navLink_ids[4];

        if (navLink_ids.includes(activeId)) {
            navLinks[4].classList.add('active');
            navLinks[4].setAttribute('aria-current', 'page');
        }
        break;
    case '/contact':
        activeId = navLink_ids[5];

        if (navLink_ids.includes(activeId)) {
            navLinks[5].classList.add('active');
            navLinks[5].setAttribute('aria-current', 'page');
        }
        break;  
    default:
        break;  
};

// Font resizer

const slider = document.querySelector("#font-slider");

slider.addEventListener("input", () => {
    let size = (slider.value) * 1.6;
    document.body.style.fontSize = size + "rem";
});

// Color blindnes Theme switch

const root = document.documentElement;
const theme = document.querySelector('#color-blind-mode');
const p1Color = '--p1-color';
const s1Color = '--s1-color';
const t1Color = '--t1-color';
const dkColor = '--dk-color';
const dkTextColor = '--dk-text-color';
const highlightTextColor = '--highlight-text-color';

theme.addEventListener("change", () => {
    /**
     * Simple color blind theme switcher
     * to improve user experience for those
     * with potential color blindness types.
     * 
     * Colors defined in this switch statement
     * needs to be researched more to ensure
     * type of color blindness is properly catered
     * for. This is just a proof of concept right now.
     */
    switch(theme.value) {
        case 'protanomaly':
            root.style.setProperty(p1Color, '#E1DAAE');
            root.style.setProperty(s1Color, '#CC2D35');
            root.style.setProperty(t1Color, '#FF934F');
            root.style.setProperty(dkColor, '#1e1e1e');
            root.style.setProperty(dkTextColor, '#0e151d');
            root.style.setProperty(highlightTextColor, '#32378c');
            break;
        case 'deuteranopia':
            root.style.setProperty(p1Color, '#e0f3db');
            root.style.setProperty(s1Color, '#43a2ca');
            root.style.setProperty(t1Color, '#a8ddb5');
            root.style.setProperty(dkColor, '#1e1e1e');
            root.style.setProperty(dkTextColor, '#0e151d');
            root.style.setProperty(highlightTextColor, '#3428ba');
            break;
        case 'deuteranomaly':
            root.style.setProperty(p1Color, '#d2cdee');
            root.style.setProperty(s1Color, '#7071E9');
            root.style.setProperty(t1Color, '#7071E9');
            root.style.setProperty(dkColor, '#1e1e1e');
            root.style.setProperty(dkTextColor, '#07071b');
            root.style.setProperty(highlightTextColor, '#111264');
            break;
        case 'tritanopia':
            root.style.setProperty(p1Color, '#D8BFD8');
            root.style.setProperty(s1Color, '#DF67D0');
            root.style.setProperty(t1Color, '#c281bf');
            root.style.setProperty(dkColor, '#1e1e1e');
            root.style.setProperty(dkTextColor, '#02030f');
            root.style.setProperty(highlightTextColor, '#0d2791');
            break;
        default:
            root.style.setProperty(p1Color, '#FFEBEA');
            root.style.setProperty(s1Color, '#f0452b');
            root.style.setProperty(t1Color, '#cc9290');
            root.style.setProperty(dkColor, '#1e1e1e');
            root.style.setProperty(dkTextColor, '#0e151d');
            root.style.setProperty(highlightTextColor, '#c02421');
            break;
    }
});
