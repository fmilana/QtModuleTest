//import { generateTable } from 'table.js';

d3.select(window).on("load", function () {

    console.log('on load');

    d3.select('#main-button')
        .on('click', function() {
            //generateTable();
            console.log('on click');
            table_lib.generate_table();
        });


});
