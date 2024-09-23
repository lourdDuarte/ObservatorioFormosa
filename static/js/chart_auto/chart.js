function patentamiento_auto(){
    let [interanual, intermensual, meses] = obtenerDatosPatentamiento();
    chart = draw_line_chart( intermensual ,interanual,' ',meses,'chart-patentamiento-historico')

}

function transferencia_auto(){
    let [interanual, intermensual, meses] = obtenerDatosTransferencia();
    chart = draw_line_chart( intermensual ,interanual,' ',meses,'chart-transferencia-historico')

}