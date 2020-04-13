var BASE_URL="http://localhost:8000/";
function graph(name, endpoint, parameters, element) {
    var request = new XMLHttpRequest()
    request.open('GET', BASE_URL + endpoint + (parameters? "?" + parameters : ""))
    request.onload = function() {
        makegraph(name, JSON.parse(this.response), element)
    }
    request.send()
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