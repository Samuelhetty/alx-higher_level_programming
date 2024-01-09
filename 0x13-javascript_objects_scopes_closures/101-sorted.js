#!/usr/bin/node
// function that returns the number of occurrences in a list

const mainList = require('./100-data').list;
console.log(mainList);
const mapList = mainList.map (function (e, index) {
  return (e * index);
});
console.log(mapList);
