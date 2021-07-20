import { generateTable } from 'main.js';


d3.select('#main-button')
    .on('click', () => {
        generateTable();
    });