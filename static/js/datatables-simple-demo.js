window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    const datatablesSimpledos = document.getElementById('datatablesSimpledos');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    if (datatablesSimpledos) {
        new simpleDatatables.DataTable(datatablesSimpledos);
    }
});
