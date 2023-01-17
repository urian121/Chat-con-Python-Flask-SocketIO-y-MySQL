
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  const email = emailInput.value;
  const password = passwordInput.value;

  axios.post("https://reqres.in/api/login", {
      email: email,
      password: password
    })
    .then((response) => {
      console.log(response);
    });
});