function construccion(){
    chartConstruccion = graficos(datosVariacionConstruccion, 'salario','salario')
    chartConstruccion2 = graficos(datosVariacionConstruccion, 'salario','salario2')

  }

  function puestosTrabajo(){
    chartPuestrosTrabajo = graficos(datosVariacionPuestos,'Puestos de trabajo','puestos-trabajo-var')
    chartPuestoTrabajoColumna = graficos_columna(puestosTrabajoData,'Evolucion de los puestos de trabajo','puestos-trabajo' )
  }