const guessButton = document.getElementById('guessButton');
const submit = document.getElementById('summonerName');

guessButton.addEventListener("click", function () {
    const userInput = submit.value;
  
    const xhr = new XMLHttpRequest();
  
    xhr.open('GET', 'http://127.0.0.1:8000/api/match/' + userInput);
  
    xhr.setRequestHeader('Content-Type', 'application/json');
  
    xhr.send();
  
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            // Atualize a página com os dados recebidos da API
            updatePage(response);
            submit.value = ""; // Limpar o campo de texto após o envio bem-sucedido
        } else {
            consolelog('Informe um nome válido');
        }
    };
});

  function updatePageWithData(data) {
    // Clear existing participant containers
    const participantsContainer = document.querySelector('.participants-container');
    participantsContainer.innerHTML = '';

    // Add new participant containers with the received data
    data.forEach(participant => {
        const participantDiv = document.createElement('div');
        participantDiv.classList.add('participant');

        participantDiv.innerHTML = `
            <h2>${participant.nick}</h2>
            <img class="icon" src="${participant.icon}" alt="${participant.champion}">
            <p>Champion: ${participant.champion}</p>
            <p>Team: ${participant.team}</p>
            <div class="items">
                <p>Items:</p>
                ${participant.items_icons.map(item_icon => `<img src="${item_icon}" alt="Item">`).join('')}
            </div>
        `;

        participantsContainer.appendChild(participantDiv);
    });
}