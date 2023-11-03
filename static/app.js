const mainSelect1 = document.querySelector("#mainSelect1");
const select2Div = document.querySelector("#serviceSelect");
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
