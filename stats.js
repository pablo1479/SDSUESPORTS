const teamStats = {
    manshawdies: {
        game1: { wins: 5, losses: 3, draws: 2 },
        game2: { wins: 7, losses: 1, draws: 4 }
    },
    "tehs-angels": {
        game1: { wins: 3, losses: 5, draws: 1 },
        game2: { wins: 6, losses: 2, draws: 3 }
    },
    doganators: {
        game1: { wins: 4, losses: 4, draws: 2 },
        game2: { wins: 8, losses: 0, draws: 2 }
    },
    astrofees: {
        game1: { wins: 6, losses: 2, draws: 2 },
        game2: { wins: 4, losses: 4, draws: 3 }
    }
};

function displayStats(team, game) {
    const stats = teamStats[team][game];
    return `
        <p>Wins: ${stats.wins}</p>
        <p>Draws: ${stats.draws}</p>
        <p>Losses: ${stats.losses}</p>
    `;
}

function updateStats(event) {
    const team = event.target.dataset.team;
    const game = event.target.value;
    const statsElement = document.getElementById(`${team}-stats`);
    statsElement.innerHTML = displayStats(team, game);
}

const gameSelects = document.querySelectorAll('.game-select');
gameSelects.forEach(select => {
    select.addEventListener('change', updateStats);
    const team = select.dataset.team;
    const game = select.value;
    const statsElement = document.getElementById(`${team}-stats`);
    statsElement.innerHTML = displayStats(team, game);
});
