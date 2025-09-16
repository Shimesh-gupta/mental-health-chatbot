function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const userMessage = input.value;
    if (!userMessage) return;

    chatBox.innerHTML += `<div class="user-msg">${userMessage}</div>`;
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: userMessage})
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot-msg">${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}