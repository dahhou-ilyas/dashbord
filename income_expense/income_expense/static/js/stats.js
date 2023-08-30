
const chartType=['bar','doughnut','line','polarArea','radar']

var currentIndex = parseInt(localStorage.getItem("currentIndex")) || 0;


const count=document.querySelector('.count')

count.addEventListener('click',()=>{
    currentIndex = (currentIndex + 1) % chartType.length;
    localStorage.setItem("currentIndex", currentIndex.toString());
    location.reload();
})

const renderChart = (data, labels,type) => {
    
    var ctx = document.getElementById("myChart").getContext("2d");
    new Chart(ctx, {
      type: type,
      data: {
        labels: labels,
        datasets: [
          {
            label: "Last 6 months expenses",
            data: data,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Expenses per category",
        },
      },
    });
  };
  
  const getChartData = (type) => {
    
    
    console.log("fetching");
    fetch("/expense_category_summary")
      .then((res) => res.json())
      .then((results) => {
        const category_data = results.expense_category_data;
        const [labels, data] = [
          Object.keys(category_data),
          Object.values(category_data),
        ];
  
        renderChart(data, labels,type);
      }).catch(e=>console.log("error"));
  };

document.onload = getChartData(chartType[currentIndex]);