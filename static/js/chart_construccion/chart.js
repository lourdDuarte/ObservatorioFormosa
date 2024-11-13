function construccion(){
    chartConstruccion = graficos(datosSalarioConstruccion, 'salario','$','salario')
    chartConstruccion2 = graficos(datosSalarioConstruccionHistorico, 'salario','$','salario-historico')
   
  }

  function puestosConstruccion(){
    chartPuestrosTrabajo = graficos(datosVariacionPuestos,'Puestos de trabajo','%','puestos-trabajo-var')
    
    chartPuestrosTrabajo = graficos(datosVariacionPuestosHistorico,'Puestos de trabajo historico','%','puestos-trabajo-var-historico')

  }


  function evolucionConstruccion(){
    chartPuestoTrabajoColumna = graficos_columna(puestosTrabajoData,'Evolucion de los puestos de trabajo','puestos-trabajo' )
    
    chartPuestoTrabajoColumna = graficos_columna(puestosTrabajoDataHistorico,'Evolucion de los puestos de trabajo historico','puestos-trabajo-historico' )

  }

  function empresasConstruccion(){
    chartEmpresasColumna = graficos_columna(empresasData,'Cantidad empresas constructoras en territorio provincial/Formosa','empresas' )
    
    chartEmpresasColumna = graficos_columna(empresasDataHistorico,'Historico de cantidad empresas constructoras en territorio ','empresas-historico' )

  }