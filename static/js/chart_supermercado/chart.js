function precio_corriente(){

  //Variacion corriente
  chartVariacionCorriente = graficos(obtenerVariaciones, 'Variacion intermensual / interanual precios corriente','chart-precio-corriente')

  chartCorrientelHistorico = graficos(ObtenerVariacionesHistoricas,'Variacion intermensual / interanual precios corriente historico ','chart-precio-corriente-historico')
  
}

function precio_constante(){
  //Variacion constante
  chartVariacionConstante = graficos(obtenerVariaciones,'Variacion intermensual / interanual precios constante','chart-precio-constante')
  
  chartConstanteHistorico = graficos(ObtenerVariacionesHistoricas,'Variacion intermensual / interanual precios constante historico ','chart-precio-constante-historico')


}

