/* eslint-disable no-continue */
/* eslint-disable prefer-destructuring */
const fs = require('fs');

const inputs = fs.readFileSync(0, 'utf-8').trim().split('\n');

class UnionFind {
  constructor(size, weights) {
    this.weights = weights;
    this.root = new Array(size).fill().map((_, index) => index);
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

    if (this.weights[rootX] < this.weights[rootY]) {
      this.root[rootY] = rootX;
    } else if (this.weights[rootX] > this.weights[rootY]) {
      this.root[rootX] = rootY;
    } else {
      this.root[rootY] = rootX;
    }
  }

  getSum() {
    let sum = 0;

    for (let i = 0; i < this.root.length; i += 1) {
      if (this.root[i] === i) {
        sum += this.weights[i];
      }
    }

    return sum;
  }
}

const [n, m, k] = inputs[0].split(' ').map(Number);
const weights = inputs[1].split(' ').map(Number);
const uf = new UnionFind(n, weights);

for (let i = 2; i < 2 + m; i += 1) {
  const [a, b] = inputs[i].split(' ').map(Number);

  uf.union(a - 1, b - 1);
}

const sum = uf.getSum();

if (sum <= k) {
  console.log(sum);
} else {
  console.log('Oh no');
}
