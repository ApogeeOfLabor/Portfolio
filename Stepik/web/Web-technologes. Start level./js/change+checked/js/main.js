
result = document.querySelector(".result");
radioButtons = document.querySelectorAll('[name="contact"]');
let selectedContactValue = 0

radioButtons.forEach(element => {
  element.addEventListener("change", function myfunc() {
    if(element.checked){
      selectedContactValue = selectedContactValue + parseInt(element.value);
    }else{
      selectedContactValue = selectedContactValue - parseInt(element.value);
    }

    if(selectedContactValue){
      result.textContent = selectedContactValue;
    }else{
      result.textContent = "Ничего не выбрано!"
    }
  });
});