firstName = document.querySelector('[name="firstName"]');
lastName = document.querySelector('[name="lastName"]');
btnElem = document.querySelector('.btn')
resElem = document.querySelector('.answer')

btnElem.addEventListener("click", function myFunction() {
  userName = firstName.value
  userSurname = lastName.value

  if(userName === "" && userSurname === "") {
    firstName.style.borderColor = "red";
    lastName.style.borderColor = "red";
    resElem.textContent = "Данные отсутствуют!";
  } else if (userName === "" && userSurname !== "") {
    firstName.style.borderColor = "";
    lastName.style.borderColor = "";
    resElem.textContent = `Здравствуйте, ${userSurname}!`;
  } else if (userName !== "" && userSurname === "") {
    firstName.style.borderColor = "";
    lastName.style.borderColor = "";
    resElem.textContent = `Здравствуйте, ${userName}!`;
  } else {
    firstName.style.borderColor = "";
    lastName.style.borderColor = "";
    resElem.textContent = `Здравствуйте, ${userName} ${userSurname}!`;
  }
});