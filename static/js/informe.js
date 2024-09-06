

  function mostrarInformePDF() {
    // Puedes utilizar una biblioteca para generar el PDF, como jsPDF
    // Asegúrate de incluir la biblioteca en tu proyecto
    contenido = []

    //ventas = localStorage.getItem("ventas")
    if(localStorage.getItem("transferenc-autos")){
      contenido.push(localStorage.getItem("transferenc-autos"))
    }
    if(localStorage.getItem("ventas-autos")){
      contenido.push(localStorage.getItem("ventas-autos"))
    }
    if(localStorage.getItem("base-imponible")){
      contenido.push(localStorage.getItem("base-imponible"))
    }
    if(localStorage.getItem("base-imponible-evolucion")){
        contenido.push(localStorage.getItem("base-imponible-evolucion"))
      }
    if(localStorage.getItem("recaudacion")){
      contenido.push(localStorage.getItem("recaudacion"))
    }
    if(localStorage.getItem("empresas-contructoras")){
      contenido.push(localStorage.getItem("empresas-contructoras"))
    }
    if(localStorage.getItem("evolucion-empleo")){
      contenido.push(localStorage.getItem("evolucion-empleo"))
    }
    if(localStorage.getItem("por-rama")){
      contenido.push(localStorage.getItem("por-rama"))
    }
    if(localStorage.getItem("puesto-trabajo")){
      contenido.push(localStorage.getItem("puesto-trabajo"))
    }
    if(localStorage.getItem("puesto-trabajo-variacion")){
        contenido.push(localStorage.getItem("puesto-trabajo-variacion"))
      }
    if(localStorage.getItem("remuneracion-ipc")){
      contenido.push(localStorage.getItem("remuneracion-ipc"))
    }
    if(localStorage.getItem("remuneracion-promedio")){
      contenido.push(localStorage.getItem("remuneracion-promedio"))
    }
    if(localStorage.getItem("salario-prom-construccion")){
      contenido.push(localStorage.getItem("salario-prom-construccion"))
    }
    if(localStorage.getItem("ipc-nea")){
      contenido.push(localStorage.getItem("ipc-nea"))
    }
    if(localStorage.getItem("ipc")){
      contenido.push(localStorage.getItem("ipc"))
    }
    if(localStorage.getItem("transferencia-moto")){
      contenido.push(localStorage.getItem("transferencia-moto"))
    }
    if(localStorage.getItem("venta-moto")){
      contenido.push(localStorage.getItem("venta-moto"))
    }
    if(localStorage.getItem("ventas-ipc-region")){
      contenido.push(localStorage.getItem("ventas-ipc-region"))
    }
    if(localStorage.getItem("ventas-porcentaje")){
      contenido.push(localStorage.getItem("ventas-porcentaje"))
    }
    if(localStorage.getItem("ventas-sin-inflacion")){
      contenido.push(localStorage.getItem("ventas-sin-inflacion"))
    }
    

    
    
    const list = document.getElementById("content");
    list.innerHTML = contenido;
    
}

 function reiniciar(){
  btn_reiniciar = document.getElementById('btn-informe-reiniciar')
  localStorage.clear();
  alert("informe borrado, ya puede cargarlo nuevamente")
  location.reload()
 }

 function ImprimirPDF() {
  row = document.getElementById('row')
 
  row.style.visibility = "hidden"
  
  window.print()
 }

 function alert_datos_guardados(){
    alert ("Agregado al informe")
 }