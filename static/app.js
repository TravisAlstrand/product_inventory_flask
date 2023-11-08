// GET STARTED PAGE
const mainSelect1 = document.querySelector("#mainSelect1");
const select2Div = document.querySelector("#categorySelect");
const mainSelect2 = document.querySelector("#mainSelect2");
const startSubmitBtn = document.querySelector("#startSubmitBtn");

if (mainSelect1) {
  mainSelect1.addEventListener("change", () => {
    select2Div.style.display = "flex";
    mainSelect2.value = "";
    showBtn();
  });
}

if (mainSelect2) {
  mainSelect2.addEventListener("change", () => {
    showBtn();
  });
}

function showBtn() {
  if (mainSelect2.value !== "" && mainSelect1.value !== "") {
    startSubmitBtn.style.display = "flex";
  } else {
    startSubmitBtn.style.display = "none";
  }
}

// BRAND EDIT
const brandEditForm = document.querySelector("#brandEditForm");
const brandNameInput = document.querySelector("#brandNameInput");
let brandIsValid = true;

if (brandEditForm) {
  brandNameInput.addEventListener("input", (e) => {
    brandIsValid = checkNameField(e.target);
  });

  brandEditForm.addEventListener("submit", (e) => {
    if (!brandIsValid) {
      e.preventDefault();
    }
  });
}

// PRODUCT EDIT
const prodEditForm = document.querySelector("#productEditForm");
const prodNameInput = document.querySelector("#productNameInput");
const priceInput = document.querySelector("#priceInput");
const quantityInput = document.querySelector("#quantityInput");
let prodNameIsValid = true;
let priceIsValid = true;
let quantityIsValid = true;

if (prodEditForm) {
  prodNameInput.addEventListener("input", (e) => {
    prodNameIsValid = checkNameField(e.target);
  });

  priceInput.addEventListener("input", (e) => {
    priceIsValid = checkNumField(e.target);
  });

  quantityInput.addEventListener("input", (e) => {
    quantityIsValid = checkNumField(e.target);
  });

  prodEditForm.addEventListener("submit", (e) => {
    if (!prodNameIsValid || !priceIsValid || !quantityIsValid) {
      e.preventDefault();
    }
  });
}

function checkNameField(input) {
  if (input.value) {
    input.nextElementSibling.style.display = "none";
    return true;
  } else {
    input.nextElementSibling.style.display = "block";
    return false;
  }
}

function checkNumField(input) {
  const onlyNums = /\D/;
  if (input.value) {
    const hasOtherChars = onlyNums.test(input.value);
    if (hasOtherChars) {
      input.nextElementSibling.textContent = "Only Numerical Digits!";
      input.nextElementSibling.style.display = "block";
      return false;
    } else {
      input.nextElementSibling.style.display = "none";
      return true;
    }
  } else {
    input.nextElementSibling.textContent = "Field Cannot Be Blank!";
    input.nextElementSibling.style.display = "block";
    return false;
  }
}
