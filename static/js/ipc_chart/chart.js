function ipc(){

    //Indice precio al consumidor actual
    chartIpcActual = graficos(datosVariacion, 'Datos IPC año actual','%','ipc-actual')
    
    //Indice precio al consumidor historico
    chartIpcHistorico = graficos(datosVariacionHistorico, 'Datos IPC historico','%', 'ipc-historico')

}