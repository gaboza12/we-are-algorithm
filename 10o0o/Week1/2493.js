/* eslint-disable prefer-destructuring */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake'
  ? './input.txt' : 0, 'utf-8').toString().trim().split('\n');

const n = +inputs[0];
const tops = inputs[1].split(' ').map(Number);
const stack = [];
const result = new Array(n);

for (let i = 0; i < n; i += 1) {
  const v = tops[i];

  while (stack.length && stack[stack.length - 1][0] < v) stack.pop();

  if (!stack.length) {
    result[i] = 0;
  } else {
    result[i] = stack[stack.length - 1][1];
  }

  stack.push([v, i + 1]);
}

console.log(result.join(' '));
