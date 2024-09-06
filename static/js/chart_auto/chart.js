function draw_venta_auto(){
    chart= draw_line_chart(data_intermensual,data_interanual,meses,'AutoNuevoChart')
    
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ventasChartHistorico')
    
}

function draw_transferencia_auto_usado(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'UsadoTransfChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'UsadosHistoricoChart')
   

}