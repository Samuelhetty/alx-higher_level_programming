#!/usr/bin/node
// script that imports an array and computes a new array.

const mainList = require('./100-data').list;
console.log(mainList);
const mapList = mainList.map (function (e, index) {
    return (e * index);
});
console.log(mapList);
