function draw_line_chart(lista1,lista2,lista3, id)
{

  var options = {
    series: [
    {
      name: "Interanual",
      data: lista1
    },
    {
      name: "Intermensual",
      data: lista2
    }
  ],
    chart: {
    height: 350,
    type: 'line',
    dropShadow: {
      enabled: true,
      color: '#000',
      top: 18,
      left: 7,
      blur: 10,
      opacity: 0.2
    },
    toolbar: {
      show: false
    }
  },
  colors: ['#77B6EA', '#545454'],
  dataLabels: {
    enabled: true,
  },
  stroke: {
    curve: 'smooth'
  },
  title: {
    text: 'Datos',
    align: 'left'
  },
  grid: {
    borderColor: '#e7e7e7',
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  markers: {
    size: 1
  },
  xaxis: {
    categories: lista3,
    title: {
      text: 'Meses'
    }
  },
  yaxis: {
    title: {
      text: ' '
    },
    min: -30,
    max: 350
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}


function draw_pie_chart(lista1, lista2, id){
  var options = {
    series: lista2,
    chart: {
    width: 100,
    type: 'pie',
  },
  labels: lista1,
  responsive: [{
    breakpoint: 10000,
    options: {
      chart: {
        width: 650
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };
  
  
  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}


function draw_column_chart(lista1, lista2, id){
 
  var options = {
    series: [{
    name: 'Net Profit',
    data: lista2
  }], 
    chart: {
    type: 'bar',
    height: 300
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '40%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  xaxis: {
    categories: lista1,
  },
  yaxis: {
    title: {
      text: '$ (thousands)'
    }
  },
  fill: {
    opacity: 1
  },

  };
  

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}

//CHART MODULO 


