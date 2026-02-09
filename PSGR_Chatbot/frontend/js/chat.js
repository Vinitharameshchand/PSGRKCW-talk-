function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage("You", message, "user");
    input.value = "";

    fetch("http://127.0.0.1:5001/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
        .then(res => res.json())
        .then(data => {
            addMessage(
                "Bot",
                data.reply,
                "bot",
                `Domain: ${data.domain} | Confidence: ${data.confidence}`
            );
        })
        .catch(() => {
            addMessage("Bot", "Server not reachable.", "bot");
        });
}

function addMessage(sender, text, cls, meta = "") {
    const box = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = cls;
    div.innerHTML = `<strong>${sender}:</strong> ${text}`;
    box.appendChild(div);

    if (meta) {
        const metaDiv = document.createElement("div");
        metaDiv.className = "meta";
        metaDiv.innerText = meta;
        box.appendChild(metaDiv);
    }

    box.scrollTop = box.scrollHeight;
}
