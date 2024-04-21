import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

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

const Stats = () => {
    const [selectedGame, setSelectedGame] = useState('game1');

    const handleGameChange = (event) => {
        setSelectedGame(event.target.value);
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

    return (
        <div className="container">
            {Object.keys(teamStats).map((team) => (
                <div key={team} className="mt-4">
                    <h2>{team}</h2>
                    <select className="form-select" value={selectedGame} onChange={handleGameChange}>
                        <option value="game1">Game 1</option>
                        <option value="game2">Game 2</option>
                    </select>
                    <div className="mt-2">{displayStats(team, selectedGame)}</div>
                </div>
            ))}
        </div>
    );
};

export default Stats;
