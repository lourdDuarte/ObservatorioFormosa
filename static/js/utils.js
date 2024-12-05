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

function graficos(funcion, titulo,tipo, id_grafico){

    let [intermensual, interanual, meses,anio, valor] = funcion();
    console.log(intermensual)

    let[maximo,minimo] = max_min(intermensual, interanual)

    if (tipo === '$'){
        return draw_line_chart(intermensual ,interanual, titulo + ' ' + anio +' ' + valor, meses,maximo,minimo,'$', id_grafico)
    }else{
        return draw_line_chart(intermensual ,interanual, titulo + ' ' + anio +' ' + valor, meses,maximo,minimo,'%',id_grafico)
    }
    
    

}

function graficos_columna(funcion, titulo, id_grafico){

    let [numeros, meses,anio, valor] = funcion();

   

    return draw_line_column(numeros,meses, titulo + ' ' + anio + ' ' + valor,id_grafico)
}

function graficos_circle(funcion, titulo, id_grafico){

    let [numeros, ramas,anio, valor] = funcion();

   

    return draw_pie(numeros,ramas, titulo + ' ' + anio + ' ' + valor,id_grafico)
}

