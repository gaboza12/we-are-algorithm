/* eslint-disable no-continue */
/* eslint-disable prefer-destructuring */
const fs = require('fs');

const inputs = fs.readFileSync(0, 'utf-8').trim().split('\n');
class UnionFind {
  constructor(size) {
    this.root = new Array(size).fill().map((_, index) => index);
    this.rank = new Array(size).fill(0);
    this.counts = new Array(size).fill(1);
  }

  find(x) {
    if (this.root[x] === x) return x;

    const found = this.find(this.root[x]);
    this.root[x] = found;

    return found;
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX === rootY) return;

    if (this.rank[rootX] > this.rank[rootY]) {
      this.root[rootY] = rootX;
      this.counts[rootX] += this.counts[rootY];
    } else if (this.rank[rootX] < this.rank[rootY]) {
      this.root[rootX] = rootY;
      this.counts[rootY] += this.counts[rootX];
    } else {
      this.rank[rootX] += 1;
      this.root[rootY] = rootX;
      this.counts[rootX] += this.counts[rootY];
    }
  }

  query(x) {
    const root = this.find(x);
    return this.counts[root];
  }
}

const n = +inputs[0];
const uf = new UnionFind(10 ** 6);
const result = [];

for (let i = 1; i <= n; i += 1) {
  const [f, a, b] = inputs[i].split(' ');

  if (f === 'I') {
    uf.union(+a - 1, +b - 1);
  } else {
    result.push(uf.query(+a - 1));
  }
}

console.log(result.join('\n'));
