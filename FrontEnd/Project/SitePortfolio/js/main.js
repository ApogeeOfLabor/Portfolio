// Side Navigation JS Code

const closeBtn = document.querySelector('.header__close-btn');
const menuBtn = document.querySelector('.header__menu-btn');
const menu = document.querySelector('.header__list');

menuBtn.onclick = function () {
    menuBtn.style.opacity = "0";
    menuBtn.style.pointerEvents = "none";
    menu.classList.add("header__list--active");
}
closeBtn.onclick = function () {
    menuBtn.style.opacity = "1";
    menuBtn.style.pointerEvents = "auto";
    menu.classList.remove('header__list--active');
}

// Sticky Navigation JS Code
const nav = document.querySelector('.nav');
let val;
window.onscroll = function () {
    if(document.documentElement.scrollTop > 20){
        nav.classList.add('sticky');
    }else{
        nav.classList.remove('sticky');
    }
}