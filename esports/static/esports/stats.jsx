import React, { useState, useEffect } from 'react';
import Chart from 'chart.js/auto'; // Import Chart.js
import 'bootstrap/dist/css/bootstrap.min.css';

const teamStats = {
    manshawdies: {
        game1: { wins: 5, losses: 3, draws: 2, playerStats: [10, 15, 20, 25] },
        game2: { wins: 7, losses: 1, draws: 4, playerStats: [12, 18, 22, 28] }
    },
    "tehs-angels": {
        game1: { wins: 3, losses: 5, draws: 1, playerStats: [8, 14, 18, 22] },
        game2: { wins: 6, losses: 2, draws: 3, playerStats: [11, 16, 21, 26] }
    },
    doganators: {
        game1: { wins: 4, losses: 4, draws: 2, playerStats: [9, 16, 19, 24] },
        game2: { wins: 8, losses: 0, draws: 2, playerStats: [14, 20, 24, 30] },
        playerData: [
            { name: 'Papa Pookie', stats: [12, 18, 20, 25] },
            { name: 'Robert McLintock', stats: [11, 17, 19, 23] },
            { name: 'Alex Rivera', stats: [14, 21, 25, 31] },
            { name: 'PookieBear Pablo', stats: [10, 15, 18, 22] }
        ]
    },
    astrofees: {
        game1: { wins: 6, losses: 2, draws: 2, playerStats: [11, 17, 21, 26] },
        game2: { wins: 4, losses: 4, draws: 3, playerStats: [13, 19, 23, 28] }
    }
};


const Stats = () => {
    const [selectedGame, setSelectedGame] = useState('game1');
    const [chart, setChart] = useState(null);

    useEffect(() => {
        // Initial chart creation when component mounts
        const initialPlayerStats = teamStats[Object.keys(teamStats)[0]][selectedGame].playerStats;
        createChart(initialPlayerStats);
    }, []);

    const handleGameChange = (event) => {
        setSelectedGame(event.target.value);
        const playerStats = teamStats[event.target.dataset.team][event.target.value].playerStats;
        updateChart(playerStats);
    };

    const displayStats = (team, game) => {
        const stats = teamStats[team][game];
        return (
            <>
                <p>Wins: {stats.wins}</p>
                <p>Draws: {stats.draws}</p>
                <p>Losses: {stats.losses}</p>
            </>
        );
    };

    const createChart = (playerStats) => {
        const ctx = document.getElementById('playerStatsChart').getContext('2d');
        const newChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Player 1', 'Player 2', 'Player 3', 'Player 4'],
                datasets: [{
                    label: 'Player Stats',
                    data: playerStats,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        setChart(newChart);
    };

    const updateChart = (playerStats) => {
        if (chart) {
            chart.data.datasets[0].data = playerStats;
            chart.update();
        }
    };

    return (
        <div className="container">
            {Object.keys(teamStats).map((team) => (
                <div key={team} className="mt-4">
                    <h2>{team}</h2>
                    <select className="form-select" value={selectedGame} onChange={handleGameChange} data-team={team}>
                        <option value="game1">Game 1</option>
                        <option value="game2">Game 2</option>
                    </select>
                    <div className="mt-2">{displayStats(team, selectedGame)}</div>
                </div>
            ))}
            <canvas id="playerStatsChart" width="400" height="200"></canvas>
        </div>
    );
};

export default Stats;
