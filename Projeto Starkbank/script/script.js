document.getElementById('send-button').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;

    if (userInput.trim() === '') return;

    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'user');
    messageDiv.textContent = userInput;
    document.getElementById('chatbot-messages').appendChild(messageDiv);

    // Função para identificar a intenção do usuário
    function getIntent(userInput) {
        const lowerCaseInput = userInput.toLowerCase();

        // Verifica palavras-chave soltas
        if (lowerCaseInput.includes('ids') || lowerCaseInput.includes('transacao') || lowerCaseInput.includes('suspeitas')) {
            return 'request_transaction_ids';
        } else if (lowerCaseInput.includes('dashboard') || lowerCaseInput.includes('interativo')) {
            return 'request_dashboard';
        } else {
            return 'generic';
        }
    }

    const intent = getIntent(userInput);

    // Responde com base na intenção identificada
    let botMessage = '';

    switch (intent) {
        case 'request_transaction_ids':
            botMessage = 'Aqui está: <a href="Dados/invoice.xlsx" download><img src="script/download.png" alt="Download" style="width: 24px; height: 24px;"></a>';
            break;
        case 'request_dashboard':
            botMessage = 'Aqui está o dashboard:<br><img src="script/stark.png" alt="Dashboard" style="width: 100%; height: auto;">';
            break;
        default:
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userInput })
            })
            .then(response => response.json())
            .then(data => {
                botMessage = data.response;
            })
            .catch(error => {
                console.error('Error:', error);
            });
            break;
    }

    var botMessageDiv = document.createElement('div');
    botMessageDiv.classList.add('message', 'bot');
    botMessageDiv.innerHTML = botMessage;
    document.getElementById('chatbot-messages').appendChild(botMessageDiv);

    document.getElementById('user-input').value = '';
});
