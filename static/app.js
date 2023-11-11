const form = document.querySelector("form");

if (form) {
  const selectMenus = document.querySelectorAll("select");
  const textInputs = document.querySelectorAll("input.name-search");
  const numInputs = document.querySelectorAll("input.num");

  // REAL TIME ERRORS
  if (textInputs.length) {
    textInputs.forEach((input) => {
      input.addEventListener("input", () => {
        checkNameField(input);
      });
    });
  }

  if (numInputs.length) {
    numInputs.forEach((input) => {
      input.addEventListener("input", () => {
        checkNumField(input);
      });
    });
  }

  // FORM SUBMIT
  form.addEventListener("submit", (e) => {
    let invalidMenus = [];

    // CHECK SELECT MENUS
    selectMenus.forEach((menu) => {
      if (!checkSelectField(menu)) {
        invalidMenus.push(menu);
      }
    });

    // CHECK TEXT INPUTS
    textInputs.forEach((input) => {
      if (!checkNameField(input)) {
        invalidMenus.push(input);
      }
    });

    // CHECK NUMBER INPUTS
    numInputs.forEach((input) => {
      if (!checkNumField(input)) {
        invalidMenus.push(input);
      }
    });

    if (invalidMenus.length) {
      e.preventDefault();
    }
  });
}

// HELPER FUNCTIONS
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

function checkSelectField(menu) {
  if (menu.value === "") {
    menu.nextElementSibling.style.display = "block";
    return false;
  } else {
    menu.nextElementSibling.style.display = "none";
    return true;
  }
}
