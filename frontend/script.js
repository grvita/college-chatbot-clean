const API_URL = "/chat";

const chatArea = document.getElementById("chatArea");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const suggestions = document.getElementById("suggestions");

async function sendMessage(message) {
    // Add user message
    addMessage(message, "user");
    
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        addMessage(data.answer, "bot");
        updateSuggestions(data.suggestions);
    } catch (error) {
        addMessage("Sorry, I'm having trouble connecting. Please check if the backend is running on port 5000.", "bot");
    }
    
    messageInput.value = "";
}

function addMessage(text, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `${sender}-message message`;
    messageDiv.innerHTML = text;
    chatArea.appendChild(messageDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function updateSuggestions(suggestionList) {
    suggestions.innerHTML = "";
    suggestionList.slice(0, 5).forEach(suggestion => {
        const chip = document.createElement("span");
        chip.className = "suggestion-chip";
        chip.dataset.question = suggestion;
        chip.textContent = suggestion.split(" ").slice(0, 3).join(" ") + "...";
        chip.onclick = () => sendMessage(suggestion);
        suggestions.appendChild(chip);
    });
}

// Event listeners
sendBtn.onclick = () => {
    const message = messageInput.value.trim();
    if (message) sendMessage(message);
};

messageInput.onkeypress = (e) => {
    if (e.key === "Enter") {
        const message = messageInput.value.trim();
        if (message) sendMessage(message);
    }
};

// Suggestion chips
suggestions.addEventListener("click", (e) => {
    if (e.target.classList.contains("suggestion-chip")) {
        const question = e.target.dataset.question;
        sendMessage(question);
    }
});
