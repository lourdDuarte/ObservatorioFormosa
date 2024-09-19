function draw_line_chart(data_intermensual,data_interanual,titulo,meses, id)
{

  var options = {
    series: [
    {
      name: "Intermensual",
      data: data_intermensual
    },
    {
      name: "Interanual",
      data: data_interanual
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
    zoom: {
      enabled: false
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
    text: titulo,
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
    categories: meses,
    title: {
      text: 'Meses'
    }
  },
  yaxis: {
    min: -30,
    max: 150
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  }
  };

  var chart = new ApexCharts(document.querySelector('#'+id), options);
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


