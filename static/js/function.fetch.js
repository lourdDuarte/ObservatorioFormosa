sin_datos = document.getElementById("alert-datos")


if(typeof data_intermensual !== 'undefined' && typeof data_interanual !== 'undefined'){
    if(data_intermensual.length == 0 && data_interanual.length == 0 || data_evolucion.length == 0  ){
    
        chart.style.display = "none"
        sin_datos.style.visibility = "visible"
        
    }
}else if(typeof data_evolucion !== 'undefined'){
    if(data_evolucion.length == 0  ){
        chart.style.display = "none"
        sin_datos.style.visibility = "visible"
        

    }
}

