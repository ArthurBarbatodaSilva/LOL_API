document.addEventListener('DOMContentLoaded', (event) => {
    const inputBox = document.getElementById('summonerName');
    const inputBoxTag = document.getElementById('tagLine');
    const guessButton = document.getElementById('guess_summoner');
    const games = document.getElementById('partidas');

    guessButton.addEventListener('click', () => {
        const summonerName = inputBox.value;
        const tagLine = inputBoxTag.value;
        const gamesSummoner = games.value;
        if (summonerName, tagLine, gamesSummoner) {
            window.location.href = `http://127.0.0.1:8000/api/match/${summonerName}/${tagLine}/${gamesSummoner}`;
        } else {
            mostrarNotificacao('PorFavor, coloque o Summoner Name, TagLine ou a Qtd de partidas');
        }
    });
});

function checkInput(event) {
    if (event.key === '#') {
        event.preventDefault();
    }
}

function removeHash() {
    const inputField = document.getElementById('tagLine');
    inputField.value = inputField.value.replace(/#/g, '');
}

function mostrarNotificacao(e) {
    Toastify({
        text: e,
        duration: 5000,
        className: "info",
        gravity: 'bottom',
        style: {
          background: "#bd360d",
          color: "#ffffff",
          border: "2px solid #bd360d"
        }
      }).showToast();
  }