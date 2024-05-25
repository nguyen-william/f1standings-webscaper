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
        const races = [...new Set(data.map(item => item.race))];
        const drivers = [...new Set(data.map(item => item.driver_name))];
    
        const datasets = drivers.map(driver => {
            const driverData = data.filter(item => item.driver_name === driver);
            var color_legend = getRandomColor();
            return {
                label: driver,
                data: races.map(race => {
                    const raceData = driverData.find(item => item.race === race);
                    return raceData ? raceData.position : null;
                }),
                borderWidth: 1,
                fill: false,
                
                borderColor: color_legend, // Use the color from colors array
                backgroundColor: color_legend, // Use getRandomColor() here
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
                    
                    title: {
                        display: true,
                        text: 'F1 Standings Graph',
                        position: 'top',
                        font: {
                            size: 10
                        },
                        padding: {
                            top: 10,
                            bottom: 30
                        },
                    },
                   
                    legend: {
                        position: 'bottom', // Move legend to the bottom
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        ticks: {
                            font: {
                                size: 7, // Adjust the font size of the race names here
                            }
                        }
                    },
                    y: {
                        min: 0,
                        max: 20,
                        reverse: true,
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