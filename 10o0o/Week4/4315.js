/* eslint-disable no-continue */
/* eslint-disable no-plusplus */
const fs = require('fs');

const inputs = fs.readFileSync(0, 'utf-8').split('\n');

let pointer = 0;
const rets = [];

while (inputs[pointer] !== '0') {
  const n = +inputs[pointer++];
  const childrenCounts = new Array(n + 1);
  const parents = new Array(n + 1).fill(null);
  const values = new Array(n + 1);

  for (let i = 0; i < n; i += 1) {
    const [v, c, d, ...children] = inputs[i + pointer].split(' ').map(Number);
    childrenCounts[v] = d;
    values[v] = c;

    for (let j = 0; j < d; j += 1) {
      parents[children[j]] = v;
    }
  }

  let queue = [];

  for (let i = 1; i <= n; i += 1) {
    if (!childrenCounts[i]) {
      queue.push(i);
    }
  }

  let result = 0;

  while (queue.length) {
    if (queue[0] === undefined) break;
    const newQueue = [];

    for (let i = 0; i < queue.length; i += 1) {
      const leafNode = queue[i];
      const diff = values[leafNode] - 1;
      result += Math.abs(diff);
      const parent = parents[leafNode];
      values[parent] += diff;
      childrenCounts[parent] -= 1;

      if (childrenCounts[parent] === 0) {
        newQueue.push(parent);
      }
    }

    queue = newQueue;
  }

  rets.push(result);
  pointer += n;
}

console.log(rets.join('\n'));
