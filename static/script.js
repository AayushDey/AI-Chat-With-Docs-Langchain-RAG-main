document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const input = document.getElementById('query-input');
    const chatHistory = document.getElementById('chat-history');

    function scrollToBottom() {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    function appendMessage(sender, text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender === 'user' ? 'user-message' : 'ai-message'}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = sender === 'user' ? 'U' : 'AI';
        
        const content = document.createElement('div');
        content.className = 'content';
        content.textContent = text;
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        chatHistory.appendChild(messageDiv);
        scrollToBottom();
        
        return messageDiv;
    }

    function appendLoading() {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message ai-message loading-message';
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = 'AI';
        
        const content = document.createElement('div');
        content.className = 'content';
        content.innerHTML = `
            <div class="loading-dots">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        `;
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        chatHistory.appendChild(messageDiv);
        scrollToBottom();
        
        return messageDiv;
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = input.value.trim();
        if (!query) return;

        // 1. Show user message
        appendMessage('user', query);
        input.value = '';
        
        // 2. Show loading indicator
        const loadingDiv = appendLoading();

        try {
            // 3. Make API call
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: query })
            });

            const data = await response.json();
            
            // 4. Remove loading indicator
            loadingDiv.remove();

            // 5. Show AI response
            if (data.error) {
                appendMessage('ai', `Error: ${data.error}`);
            } else {
                appendMessage('ai', data.answer);
            }
            
        } catch (error) {
            loadingDiv.remove();
            appendMessage('ai', `Sorry, something went wrong. Make sure the server is running.`);
            console.error('Error:', error);
        }
    });
});
