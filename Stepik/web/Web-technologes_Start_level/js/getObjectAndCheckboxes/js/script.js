const btn = document.querySelector('.button');
const checkboxElement = document.querySelectorAll('[name="contact"]');
let resultElement = document.querySelector('.result');

const contactChecked = {
  email: false,
  phone: false,
  mail: false,
};

btn.addEventListener("click", 
  () => {
    checkboxElement.forEach(element => {
    contactChecked[element.value] = element.checked;
    });
    console.log(contactChecked);
    resultElement.textContent = "объект получен";
    setTimeout(() => { resultElement.textContent = ""; }, 1300);
  }
);
