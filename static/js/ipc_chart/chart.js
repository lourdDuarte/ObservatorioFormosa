function ipc_division(){
    let [interanual, intermensual, meses] = obtenerDatosDivision();
    chart = draw_line_chart( intermensual ,interanual,' ',meses,'chartDivision')
    
  }