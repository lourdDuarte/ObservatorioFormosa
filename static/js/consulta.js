function grafico(funcion, titulo, id_grafico){
    let [intermensual, interanual, meses, modelo, anio, valor] = funcion();
    
    let[maximo,minimo] = max_min(intermensual, interanual)
    
   
 

    return draw_line_chart( intermensual ,interanual, titulo + ' ' + modelo + ' ' + anio + ' ' + valor,
        meses,maximo,minimo, id_grafico)
    

}


function GraficoUno(){

    chartGraficoUno = grafico( obtenerGraficoUno,'Datos','chart-comparativo-uno')
  
}

function GraficoDos(){

    chartGraficoDos = grafico( obtenerGraficoDos,'Datos', 'chart-comparativo-dos')
 
}
