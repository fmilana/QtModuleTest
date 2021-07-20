import { generateTable } from 'table.js';


d3.select('#main-button')
    .on('click', () => {
        generateTable();
    });