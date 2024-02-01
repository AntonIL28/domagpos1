import DataTable from 'datatables.net-dt';
import $ from jquery;

var $ = require('jquery')
var DataTable =require('datatables.net-dt')(window, $);

let table =new DataTable('#dynamic-table',{
    //config options
});

$(document).ready( function () {
    $('#dynamic-table').DataTable();
} );