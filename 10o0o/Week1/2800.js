/* eslint-disable prefer-destructuring */
const fs = require('fs');

const str = fs.readFileSync(process.env.LOGNAME === 'jake'
  ? './input.txt' : 0, 'utf-8').toString().trim();

const stack = [];
const couples = [];

for (let i = 0; i < str.length; i += 1) {
  if (str[i] === '(') stack.push(i);
  if (str[i] === ')') {
    couples.push([stack.pop(), i]);
  }
}

const cs = [];

const s = (ii, acc) => {
  if (acc.length) {
    cs.push(new Set(acc));
  }

  if (ii === couples.length) {
    return;
  }

  for (let i = ii; i < couples.length; i += 1) {
    acc.push(...couples[i]);
    s(i + 1, acc);
    acc.pop();
    acc.pop();
  }
};

s(0, []);

const rs = new Set();

for (const c of cs) {
  let cstr = '';

  for (let i = 0; i < str.length; i += 1) {
    if (!c.has(i)) {
      cstr += str[i];
    }
  }

  rs.add(cstr);
}

const result = [...rs].sort();

console.log(result.join('\n'));
