function draw_ipc(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'ipcChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ipcChartHistorico')
    
}

function draw_ipc_nea(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'ipcNeaChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'ipcNeaChartHistorico')
   

}