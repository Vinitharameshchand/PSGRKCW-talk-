function send() {
  const msg = document.getElementById("message").value;

  fetch("http://127.0.0.1:5001/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("chatbox").innerHTML +=
      `<p><b>You:</b> ${msg}</p>
       <p><b>Bot:</b> ${data.reply}</p>`;
  });
}
