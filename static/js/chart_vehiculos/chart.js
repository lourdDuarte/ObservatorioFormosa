
function moto(){

    

    //Patentamiento
    chartActualPatentamiento = graficos(datosVehiculoActual,'Datos patentamiento año actual','%','patentamiento-moto' )


    chartHistoricoPatentamiento = graficos(datosVehiculoHistorico,'Datos patentamiento historico','%','patentamiento-moto-historico' )
 

    //Transferencia
    chartActualTransferencia = graficos( datosVehiculoActual,'Datos transferencia año actual ' ,'%','transferencia-moto')
    
    chartHistoricoTransferencia = graficos (datosVehiculoHistorico,'Datos transferencia historico ','%','transferencia-moto-historico')
}


function auto(){

    

    //Patentamiento
    chartActualPatentamiento = graficos( datosVehiculoActual,'Datos patentamiento año actual ','%','patentamiento-auto')

    chartHistoricoPatentamiento = graficos (datosVehiculoHistorico,'Datos patentamiento historico ','%','patentamiento-auto-historico')

    //Transferencia
    chartActualTransferencia = graficos( datosVehiculoActual,'Datos transferencia año actual ','%','transferencia-auto')
    
    chartHistoricoTransferencia = graficos (datosVehiculoHistorico,'Datos transferencia historico ','%','transferencia-auto-historico')
}


