

function draw_venta_moto(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'MotoNuevoChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'MotoChartHistorico')
}

function draw_transferencia_moto_usado(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'MotoUsadaChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'MotoUsadaHistorico')

}