function variantes_temporales(){
  let [meses, var_interanual, var_intermensual] = data_variacion();
  chartVariacion = draw_line_chart(var_intermensual,var_interanual,'Cantidad de operaciones intermensual / interanual', meses,'chart')
}