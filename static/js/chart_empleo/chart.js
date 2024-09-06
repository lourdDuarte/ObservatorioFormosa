

function draw_evolucion_empleo(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'EvolucionChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'EvolucionChartHistorico')
}


function draw_remuneracion_empleo(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'RemuneracionChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'RemuneracionChartHistorico')
}

function draw_remuneracion_ipc(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'RemuneracionIpChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'HistoricoRemunIpcChart')
}

function draw_empleo_ramas(){
   
    
    draw_pie_chart(data_nombres,data_numerico,'RamasChart')
  
    
}

function draw_puestos_trabajo(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'PuestoTrabajoChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'HistoricoPuestosChart')
}

function draw_puestos_column(){
    chart = draw_column_chart(meses,data_evolucion,  'PuestosColumnChart')
    chart_historico = draw_column_chart(meses_historico,data_evolucion_historico, 'PuestosColumnHistorico')
    
}

function draw_promedio_construccion(){
    chart = draw_line_chart(data_intermensual,data_interanual,meses,'SalarioPromedioConstruccionChart')
    chart_historico = draw_line_chart(data_intermensual_historico,data_interanual_historico,meses_historico,'HistoricoSalarioPromChart')
}

function draw_empresas_constructoras(){
    chart = draw_column_chart(meses, data_evolucion,  'ConstructorasChart')
    chart_historico = draw_column_chart(meses_historico,data_evolucion_historico, 'HistoricoPuestosChart')
}


