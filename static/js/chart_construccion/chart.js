function construccion(){
    chartConstruccion = graficos(datosVariacionConstruccion, 'salario','salario')
    chartConstruccion2 = graficos(datosVariacionConstruccion, 'salario','salario2')

  }

  function puestosTrabajo(){
    chartPuestrosTrabajo = graficos(datosVariacionPuestos,'Puestos de trabajo','puestos-trabajo-var')
    chartPuestoTrabajoColumna = graficos_columna(puestosTrabajoData,'Evolucion de los puestos de trabajo','puestos-trabajo' )
  
    chartPuestrosTrabajo = graficos(datosVariacionPuestosHistorico,'Puestos de trabajo historico','puestos-trabajo-var-historico')
    chartPuestoTrabajoColumna = graficos_columna(puestosTrabajoDataHistorico,'Evolucion de los puestos de trabajo historico','puestos-trabajo-historico' )

  }