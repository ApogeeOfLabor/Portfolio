let output_msg = document.querySelector(".message__text");


async function start() {
  let start_msg = await eel.start_hello()();
  output_msg.textContent = start_msg.value;
};