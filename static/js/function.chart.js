function draw_line_chart(data_intermensual,data_interanual,titulo,meses,max,min,id)
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
      top: 10,
      left: 7,
      blur: 7,
      opacity: 0.2
    },
    zoom: {
      enabled: true
    },
    toolbar: {
      show: true
    }
  },
  colors: ['#007D9D', '#859222'],
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
    size: 0
  },
  xaxis: {
    categories: meses,
    title: {
      text: 'Meses'
    }
  },
  yaxis: {
    min: min,
    max: max,
    tickAmount: 4, // Define la cantidad de marcas en el eje Y, ajusta este valor según lo necesites
    forceNiceScale: true, // Mantener esta opción por si ayuda en la escala
    labels: {
      formatter: function(value) {
        return value.toFixed(0); // Mostrar solo enteros
      }
    },
  },
  
  grid: {
    show: true,
    position: 'back',
    yaxis: {
      lines: {
        show: true
      }
    },
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -20,
    offsetX: -0
  },
  annotations: {
    yaxis: [{
      y: 0,
      borderColor: '#000000',  // Color de la línea
      strokeDashArray: 0,       // Línea punteada
      
    }]
  }
  };

  var chart = new ApexCharts(document.querySelector('#'+id), options);
  chart.render();
}


function draw_line_column(data, meses, title, id){
 
  var options = {
    series: [{
    name: 'Total',
    data: data
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
  colors: ['#007D9D'],
  plotOptions: {
    bar: {
      borderRadius: 10,
      dataLabels: {
        position: 'top', // top, center, bottom
      },
    }
  },
  dataLabels: {
    enabled: true,
    
    offsetY: -20,
    style: {
      fontSize: '12px',
      colors: ["#859222"]
    }
  },
  
  xaxis: {
    categories: meses,
    position: 'buttom',
    offsetY: -8,
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    },
    crosshairs: {
      fill: {
        type: 'gradient',
        gradient: {
          colorFrom: '#D8E3F0',
          colorTo: '#BED1E6',
          stops: [0, 100],
          opacityFrom: 0.4,
          opacityTo: 0.5,
        }
      }
    },
    tooltip: {
      enabled: true,
    }
  },
  yaxis: {
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false,
    },
    labels: {
      show: false,
      formatter: function (val) {
        return val + "%";
      }
    }
  
  },
  title: {
    text: title,
    position: 'top',
    floating: false,
  
    align: 'left',
    style: {
      color: '#444'
    }
  }
  };
  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();

}



// function draw_pie_chart(lista1, lista2, id){
//   var options = {
//     series: lista2,
//     chart: {
//     width: 100,
//     type: 'pie',
//   },
//   labels: lista1,
//   responsive: [{
//     breakpoint: 10000,
//     options: {
//       chart: {
//         width: 650
//       },
//       legend: {
//         position: 'bottom'
//       }
//     }
//   }]
//   };
  
  
//   var chart = new ApexCharts(document.querySelector("#"+id), options);
//   chart.render();
// }


// function draw_column_chart(lista1, lista2, id){
 
//   var options = {
//     series: [{
//     name: 'Net Profit',
//     data: lista2
//   }], 
//     chart: {
//     type: 'bar',
//     height: 300
//   },
//   plotOptions: {
//     bar: {
//       horizontal: false,
//       columnWidth: '40%',
//       endingShape: 'rounded'
//     },
//   },
//   dataLabels: {
//     enabled: false
//   },
//   stroke: {
//     show: true,
//     width: 2,
//     colors: ['transparent']
//   },
//   xaxis: {
//     categories: lista1,
//   },
//   yaxis: {
//     title: {
//       text: '$ (thousands)'
//     }
//   },
//   fill: {
//     opacity: 1
//   },

//   };
  

//   var chart = new ApexCharts(document.querySelector("#"+id), options);
//   chart.render();
// }

// //CHART MODULO 


