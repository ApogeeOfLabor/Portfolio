const btn = document.querySelector("#btn");
const inputRadio = document.querySelectorAll('[name="goods"]');

const someObject = {
  value: "",
  price: 0,
  size: "",
}

btn.addEventListener("click", () => {
  inputRadio.forEach(element => {
    if(element.checked){
      someObject.value = element.value;
      someObject.price = parseInt(element.dataset.price);
      someObject.size = element.dataset.size;
    }
  });
  console.log(someObject);
})