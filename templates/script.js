fetch('standings.json')
    .then(function(response) {
        if (response.ok) {
            return response.json();
        }
    })
    .then(function(data) {
        createChart(data, 'line');
    });

function createChart(data, type) {
    const races = [...new Set(data.map(item => item.race))]; // Get unique races
    const drivers = [...new Set(data.map(item => item.driver_name))]; // Get unique drivers

    const datasets = drivers.map(driver => {
        const driverData = data.filter(item => item.driver_name === driver);
        return {
            label: driver,
            data: races.map(race => {
                const raceData = driverData.find(item => item.race === race);
                return raceData ? raceData.position : null;
            }),
            borderWidth: 1,
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1
        };
    });

    const ctx = document.getElementById('myChart').getContext('2d');

    new Chart(ctx, {
        type: type,
        data: {
            labels: races,
            datasets: datasets
        },
        options: {
            plugins: {
                legend: {
                    position: 'bottom', // Move legend to the bottom
                }
            },
            scales: {
                x: {
                    beginAtZero: true
                },
                y: {
                    min: 1, // Set minimum value to 1
                    max: 20, // Set maximum value to 20
                    reverse: true, // Reverse the order
                    ticks: {
                        stepSize: 1
                    }    
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
