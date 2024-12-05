function sector_privado(){

    //Variacion corriente
    chartVariacionActual = graficos(variacionPrivadoActual, 'Variacion intermensual / interanual evolucion del empleo en sector privado','%','evolucion-privado')
  
    chartVariacionHistorico = graficos(variacionPrivadoHistorico,'Variacion intermensual / interanual evolucion del empleo en sector privado','%','evolucion-privado-historico')
    
  }


function sector_privado_rama(){

    //Variacion corriente
    chartRamaActual = graficos_circle(ramaPrivadoActual, ' Trabajadores por rama','trabajadores-privado')
    chartRamaHistorico = graficos_circle(ramaPrivadoHistorico, ' Trabajadores por rama historico','trabajadores-privado-historico')
    
  }