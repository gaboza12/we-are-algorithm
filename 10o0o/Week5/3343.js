/* eslint-disable prefer-const */
/* eslint-disable no-param-reassign */
const fs = require('fs');

let [n, a, b, c, d] = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);

const getGCD = (max, min) => {
  while (min) {
    const r = max % min;
    max = min;
    min = r;
  }

  return max;
};

const gcd = getGCD(a, c);
const lcm = (a * c) / gcd;

if (a * d < c * b) {
  [a, b, c, d] = [c, d, a, b];
}

const cCounts = lcm / c;
let min = Infinity;

for (let i = 0; i <= cCounts; i += 1) {
  const remains = Math.max(0, n - i * c);
  const mul = Math.ceil(remains / a);
  const sum = BigInt(b) * BigInt(mul) + BigInt(i * d);

  if (min > sum) min = sum;
  if (remains <= 0) break;
}

console.log(min.toString());
