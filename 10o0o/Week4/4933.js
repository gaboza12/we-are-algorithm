/* eslint-disable no-continue */
/* eslint-disable no-plusplus */
const fs = require('fs');

const inputs = fs.readFileSync(0, 'utf-8').split('\n');
let t = +inputs[0];
let pointer = 1;

class TreeNode {
  constructor(value) {
    this.value = value;
    this.parent = null;
    this.left = null;
    this.right = null;
  }
}

const makeTree = (treeInput) => {
  treeInput.pop();

  const rootNode = new TreeNode(treeInput.pop());
  let targetNode = rootNode;

  while (treeInput.length) {
    const popped = treeInput.pop();
    while (targetNode.right && targetNode.left) targetNode = targetNode.parent;

    if (popped === 'nil') {
      if (!targetNode.right) targetNode.right = 'nil';
      else targetNode.left = 'nil';

      continue;
    }

    const newNode = new TreeNode(popped);

    if (!targetNode.right) {
      targetNode.right = newNode;
    } else {
      targetNode.left = newNode;
    }

    newNode.parent = targetNode;
    targetNode = newNode;
  }

  return rootNode;
};

const treeCompare = (tree1, tree2) => {
  if (!tree1 && !tree2) return true;
  if ((tree1 && !tree2) || (tree2 && !tree1)) return false;
  if (tree1.value !== tree2.value) return false;

  return (
    (
      treeCompare(tree1.left, tree2.left) && treeCompare(tree1.right, tree2.right)
    ) || (
      (treeCompare(tree1.right, tree2.left) && treeCompare(tree1.left, tree2.right))
    )

  );
};

const rets = [];

while (t) {
  t -= 1;

  const tree1 = makeTree(inputs[pointer].split(' '));
  const tree2 = makeTree(inputs[pointer + 1].split(' '));

  const result = treeCompare(tree1, tree2);
  rets.push(result);

  pointer += 2;
}

console.log(rets.join('\n'));
