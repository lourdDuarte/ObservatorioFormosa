function variantes_temporales(){
  let [intermensual_corriente, interanual_corriente,meses_corriente] = obtenerVariaciones();
  let [intermensual_constante, interanual_constante,meses_constante] = obtenerVariaciones();

  let [intermensual_corriente_historico, interanual_corriente_historico,meses_corriente_historico] = ObtenerVariacionesHistoricas();
  let [intermensual_constante_historico, interanual_constante_historico,meses_constante_historico] = ObtenerVariacionesHistoricas();
  
  
  
  
  chartVariacionCorriente = draw_line_chart(intermensual_corriente,interanual_corriente,'Variacion intermensual / interanual precios corriente',meses_corriente,'chart-precio-corriente')
  chartVariacionConstante = draw_line_chart(intermensual_constante,interanual_constante,'Variacion intermensual / interanual precios constante',meses_constante,'chart-precio-constante')
  chartCorrientelHistorico = draw_line_chart(intermensual_corriente_historico, interanual_corriente_historico,'Variacion intermensual / interanual precios corriente historico',meses_corriente_historico,'chart-precio-corriente-historico')
  chartConstanteHistorico = draw_line_chart(intermensual_constante_historico, interanual_constante_historico,'Variacion intermensual / interanual precios constante',meses_constante_historico,'chart-precio-constante-historico')


}

function variantes_totales(){
  let [categoria,total,precio,mes] = obtenerTotalArticulo();
  let [categoria_total,total_total,precio_total,mes_total] = obtenerTotal();
  
  
  chartTotalProducto = draw_line_column(total,categoria,precio,mes,'Venta por producto pecio','chart-total-producto')
  chartTotal = draw_line_column(total_total,categoria_total,precio_total,mes_total,'Ventas totales precio','chart-total')


}

function indicadores(){
  let [intermensual, interanual,meses] = obtenerIndicadores();
  let [intermensual_historico , interanual_historico ,meses_historico] = ObtenerIndicadoresHistoricos();
  let [total_operaciones, meses_operaciones, valor] = obtenerTotalOperaciones();

  chartIndicador = draw_line_chart(intermensual, interanual,'Variacion intermensual / interanual de operaciones',meses,'chart-operaciones-variante')
  chartIndicadorHistorico = draw_line_chart(intermensual_historico , interanual_historico,'Variacion intermensual / interanual de operaciones historico',meses_historico,'chart-operaciones-variante-historico')

  chartTotalProducto = draw_line_column(total_operaciones,meses_operaciones,'',valor,'Total cantidad de operaciones','chart-cantidad-operaciones')
}