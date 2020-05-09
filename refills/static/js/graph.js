function parseJSON(jsonString) {
    return JSON.parse(jsonString.replace(/&quot;/g,'"'));
}

function daytotal(data) {
    for(i = 0; i<Object.keys(data).length; i++) {
        if(i != 0) {
            data[i].value = data[i].value - data[i-1].value
            console.log(data[i].value)
        }
    }
}
function makegraph(name, data, element) {
    var labels;
    if(data[0].timestamp){
        labels = data.map((item) => new Date(item.timestamp))
    } else if (data[0].date) {
        labels = data.map((item) => item.date);
    } else {
        labels = null;
    }
    var values = data.map((item) => item.value);
    var ctx = document.getElementById(element).getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data:  {
            labels: labels,
            x: labels,
            datasets: [{
                label: name,
                data: values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                
                xAxes: [{
                    type: 'time',
                    distribution: 'linear',
                    time: {
                        displayFormats: {
                            day: 'll h:mm a'                              }
                    }
                    
                }]
            }
        }
    });
}