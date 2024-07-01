/* eslint-disable no-continue */
/* eslint-disable no-plusplus */
const fs = require('fs');

const inputs = fs.readFileSync(0, 'utf-8').split('\n');
let t = +inputs[0];
let pointer = 1;

const ret = [];

while (t) {
  const n = +inputs[pointer++];
  const parents = new Array(n + 1);

  for (let i = 0; i < n - 1; i += 1) {
    const [p, c] = inputs[pointer + i].split(' ').map(Number);
    parents[c] = p;
  }

  pointer += n - 1;

  const [a, b] = inputs[pointer++].split(' ').map(Number);
  const aSet = new Set();

  let target = a;

  while (target) {
    aSet.add(target);
    target = parents[target];
  }

  let target2 = b;

  while (target2) {
    if (aSet.has(target2)) {
      ret.push(target2);
      break;
    }

    target2 = parents[target2];
  }

  t -= 1;
}

console.log(ret.join('\n'));
