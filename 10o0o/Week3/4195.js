/* eslint-disable no-plusplus */
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

let t = +inputs[0];
let pointer = 1;
let id = 0;
const result = [];

const getId = (name, idMap) => {
  if (idMap.has(name)) {
    return idMap.get(name);
  }

  idMap.set(name, id++);
  return id - 1;
};

while (t) {
  const uf = new UnionFind(10 ** 6);
  const idMap = new Map();
  const n = +inputs[pointer++];
  for (let i = pointer; i < pointer + n; i += 1) {
    const [a, b] = inputs[i].split(' ');
    const aId = getId(a, idMap);
    const bId = getId(b, idMap);

    uf.union(aId, bId);

    result.push(uf.query(aId));
  }

  pointer += n;
  t -= 1;
  id = 0;
}

console.log(result.join('\n'));
