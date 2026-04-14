function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim().toLowerCase();
    let chatBox = document.getElementById("chat-box");

    if (message === "") return;

    // Show user message
    chatBox.innerHTML += "<p class='user'>" + message + "</p>";

    let response = "";

    if (message.includes("hello") || message.includes("hi")) {
        response = "Hello! How can I assist you?";
    } 
    else if (message.includes("order")) {
        response = "Please provide your order ID.";
    } 
    else if (message.includes("payment")) {
        response = "We accept UPI, cards, and net banking.";
    } 
    else if (message.includes("refund")) {
        response = "Refund will be processed within 5-7 days.";
    } 
    else if (message.includes("contact")) {
        response = "You can contact us at support@example.com.";
    } 
    else if (message.includes("bye")) {
        response = "Goodbye! Have a great day!";
    } 
    else {
        response = "Sorry, I didn’t understand that.";
    }

    // Show bot response
    chatBox.innerHTML += "<p class='bot'>" + response + "</p>";

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}