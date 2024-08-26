/* eslint-disable no-lonely-if */
/* eslint-disable prefer-destructuring */
const fs = require('fs');

const str = fs.readFileSync(process.env.LOGNAME === 'jake'
  ? './input.txt' : 0, 'utf-8').toString().trim();

const stack = [];
let pr = 1;
let result = 0;
let fl = 0;

for (let i = 0; i < str.length; i += 1) {
  if (['(', '['].includes(str[i])) {
    stack.push(str[i]);
    pr *= str[i] === '(' ? 2 : 3;
    fl = 1;
  } else {
    if (str[i] === ']') {
      if (!stack.length || stack.pop() !== '[') {
        console.log(0);
        process.exit(0);
      }

      if (fl) {
        result += pr;
        fl = 0;
      }
      pr /= 3;
    } else if (str[i] === ')') {
      if (!stack.length || stack.pop() !== '(') {
        console.log(0);
        process.exit(0);
      }

      if (fl) {
        result += pr;
        fl = 0;
      }
      pr /= 2;
    }
  }
}

if (stack.length) {
  console.log(0);
  process.exit(0);
}

console.log(result);
