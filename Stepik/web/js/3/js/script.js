const inputElement = document.querySelector(".block__text");
const resultElement = document.querySelector("span");

inputElement.addEventListener("change", function somename(){
	resultElement.textContent = inputElement.value;
})