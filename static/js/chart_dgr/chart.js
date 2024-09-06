function draw_base_imponible(){
    chart = draw_column_chart(meses,data_evolucion,  'BaseImponibleChart')
    chart_historico = draw_column_chart(meses_historico,data_evolucion_historico, 'BaseHistoricoChart')

}

function draw_base_imponible_contribuyente(){
    chart = draw_column_chart(meses,data_evolucion,  'BaseImponibleEvoChart')
    chart_historico = draw_column_chart(meses_historico,data_evolucion_historico, 'BaseHistoricoEvoChart')

}

function draw_recaudacion(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'RecaudacionChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'RecaudacionHistoricaChart')

}

