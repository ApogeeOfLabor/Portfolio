btn = document.querySelector(".btn");
result = document.querySelector(".result");
radioButtons = document.querySelectorAll('[name="contact"]');

btn.addEventListener("click", function myFunc(){
  let selectedContactValue = 0;
  for (const radioButton of radioButtons){
      if (radioButton.checked){
        selectedContactValue = selectedContactValue + parseInt(radioButton.value);
      }
  }
  result.textContent = `${selectedContactValue}р`;
})