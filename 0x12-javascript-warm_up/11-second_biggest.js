#!/usr/bin/node
/* comment */
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const cont = process.argv.sort();
  console.log(cont.reverse()[1]);
}
