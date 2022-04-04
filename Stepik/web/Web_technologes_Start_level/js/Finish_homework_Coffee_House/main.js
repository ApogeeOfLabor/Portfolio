$('body').on('input', '.menu__count', function () {
  this.value = this.value.replace(/[^0-9]/g, '');
});


const btn = document.querySelector('.header__submit');
const checkboxes = document.querySelectorAll('[name="product"]');

