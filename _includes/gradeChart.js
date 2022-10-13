
<script>
    // TODO: Use different colors for each bar
    var barColors = [
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(54, 162, 235, 0.8)',
    ];
    let dataPoints_{{ include.year }} =[{% for m in include.data reversed %} "{{ m[1] }}", {% endfor %} ]
    new Chart("chart-{{ include.year }}", {
        type: "bar",
        data: {
            labels: ["E", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
            datasets: [{
                backgroundColor: barColors,
                data: dataPoints_{{ include.year }}
    }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
                x: {

                }
            },
            legend: { display: false },
            title: {
                display: true,
                text: "Grade Distribution"
            }
        }
    });
</script>