inputName = document.querySelector('#name');
inputSurname = document.querySelector('#surname');
resultElement = document.querySelector(".button");

const user = {
  name: "",
  surname: "",
}

resultElement.addEventListener('click', function myfunc() {
  user.name = inputName.value;
  user.surname = inputSurname.value;
  console.log(user);
});