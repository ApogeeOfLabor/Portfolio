const firstname = document.querySelector('.firstname')
const lastname = document.querySelector('.lastname')

const checkboxes = document.querySelectorAll('[name="product"]');
const counts = document.querySelectorAll('[type="number"]');

const btn = document.querySelector('.header__submit');
const result = document.querySelector('.result__text')


checkboxes.forEach(element => {
  element.addEventListener("change", function () {
    if (element.checked) {
      let count = document.querySelector("[name='count']")
      count.value = 1;
    }
  })
});

const Products = {
  espresso: 0,
  americano: 0,
  latte: 0,
  capuchino: 0,
  choco_cupcake: 0,
  blueberrie_cupcake: 0,
  apple_cupcake: 0,
};

const choicePriceGoods = {
  expresso: 0,
  americano: 0,
  latte: 0,
  capuchino: 0,
  chocolate_muffin: 0,
  blueberry_muffin: 0,
  apple_tart: 0,
};

function getResultSum() {
  let sum = 0;
  Object.keys(countGoods).forEach((key) => {
    sum += countGoods[key] * choicePriceGoods[key];
  });
  resultElem.innerText = `Итого: ${sum} р.`;
  return sum;
}

countElements.forEach((elem) => {
  elem.addEventListener("change", function () {
    let goodEl = null;
    goodsElements.forEach((goods) => {
      if (this.id === goods.dataset.goods) {
        goodEl = goods;
      }
    });
    if (
      this.value < 0 ||
      this.value.startsWith("0") ||
      this.value.length === 0
    ) {
      goodEl.checked = false;
      countGoods[this.id] = 0;
      choicePriceGoods[this.id] = 0;
      this.value = 0;
    } else {
      goodEl.checked = true;
      countGoods[this.id] = this.value;
      choicePriceGoods[this.id] = goodEl.value;
    }
    getResultSum();
  });
});

goodsElements.forEach((product) => {
  product.addEventListener("change", function () {
    let countEl = null;
    countElements.forEach((el) => {
      if (el.id === this.dataset.goods) {
        countEl = el;
      }
    });
    if (this.checked) {
      countGoods[this.dataset.goods] += 1;
      choicePriceGoods[this.dataset.goods] += this.value;
      countEl.value = countGoods[this.dataset.goods];
    } else {
      countGoods[this.dataset.goods] = 0;
      choicePriceGoods[this.dataset.goods] = 0;
      countEl.value = 0;
    }
    getResultSum();
  });
});

btn.addEventListener("click", () => {
  alert(
    `Заказчик: ${userName.value} ${userSurname.value}\n${resultElem.textContent}`
  );
});
