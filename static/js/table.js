new DataTable('#example', {
    
    fixedColumns: {
        start: 0
    },
    layout: {
      topStart: {
        buttons: [
            {
                extend: 'colvis',
                text: 'Esconder columna' 
            }
        ]
    }
    },
    order: [],
    paging: true,
    scrollCollapse: true,
    scrollX: true,
    scrollY: 300

});

new DataTable('#example2', {
  fixedColumns: {
      start: 0
  },
  layout: {
    topStart: {
      buttons: [
          {
              extend: 'colvis',
              text: 'Esconder columna' 
          }
      ]
  }
  },
  order: [],
  paging: true,
  scrollCollapse: true,
  scrollX: true,
  scrollY: 300

});