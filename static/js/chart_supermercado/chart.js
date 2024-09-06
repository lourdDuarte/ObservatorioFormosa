
function draw_supermercado(){
  chart = draw_line_chart(data_intermensual,data_interanual,meses,'ventasChartUltimoAño')
  chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ventasChart')
}




function draw_supermercado_sin_inflacion(){
  chart = draw_line_chart(data_intermensual,data_interanual,meses,'ventaSinInflacion')
  chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ventasChart')
}

function draw_supermercado_ipc()
{
  chart = draw_line_chart(data_intermensual,data_interanual,meses,'ventasChartIPC')
  chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ventasChartipcHistorico')
}



