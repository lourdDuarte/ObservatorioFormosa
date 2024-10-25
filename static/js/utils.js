function max_min(intermensual,interanual){
    
    const indicadores = intermensual.concat(interanual);
    
    maximo = (Math.max(...indicadores));
    minimo = (Math.min(...indicadores));

   

    return [maximo,minimo]
}

function validation(anio,valor){
    
    if (anio != undefined && valor != undefined){
        console.log(anio)
        anio = anio
        valor = valor
    }else{
         console.log(anio)
          anio = ' '
          valor = ' '
    }
    return { anio, valor };
}

function graficos(funcion, titulo, id_grafico){

    let [intermensual, interanual, meses,anio, valor] = funcion();

    let[maximo,minimo] = max_min(intermensual, interanual)

    return draw_line_chart(intermensual ,interanual, titulo + ' ' + anio +' ' + valor, meses,maximo,minimo, id_grafico)
}

