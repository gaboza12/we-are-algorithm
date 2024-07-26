#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(NULL);               \
  cout.tie(NULL);

#define F(i, a, b) for (int i = (a); i < (b); i += 1)
#define FR(i, a, b) for (int i = (b - 1); i >= (a); i -= 1)

int getLeftIndex(int x) { return x * 2 + 1; }
int getRightIndex(int x) { return x * 2 + 2; }
int getMidIndex(int s, int e) { return (s + e) / 2; }
auto compare = [](const array<int, 3>& a, array<int, 3>& b) {
  if (a[1] != b[1]) return a[1] < b[1];

  return a[0] < b[0];
};

class SegmentTree {
 public:
  SegmentTree(const vector<int>& arr) {
    n = arr.size();
    tree.resize(4 * n);
    lazy.resize(4 * n);
    build(arr, 0, 0, n - 1);
  }

  void updateRange(int queryLeft, int queryRight, int add) {
    updateRange(0, 0, n - 1, queryLeft, queryRight, add);
  }

  int query(int left, int right) { return query(0, 0, n - 1, left, right); }

 private:
  int n;
  vector<int> tree;
  vector<int> lazy;

  void build(const vector<int>& arr, int node, int start, int end) {
    if (start == end) {
      tree[node] = arr[start];
    } else {
      const int midIndex = getMidIndex(start, end);
      const int leftIndex = getLeftIndex(node);
      const int rightIndex = getRightIndex(node);

      build(arr, leftIndex, start, midIndex);
      build(arr, rightIndex, midIndex + 1, end);

      tree[node] = max(tree[leftIndex], tree[rightIndex]);
    }
  }

  void updateRange(int node, int left, int right, int queryLeft, int queryRight,
                   int add) {
    if (lazy[node]) {
      tree[node] += lazy[node];
      if (left != right) {
        lazy[getLeftIndex(node)] += lazy[node];
        lazy[getRightIndex(node)] += lazy[node];
      }
      lazy[node] = 0;
    };

    if (left > right || left > queryRight || right < queryLeft) return;
    if (queryLeft <= left && right <= queryRight) {
      tree[node] += add;
      if (left != right) {
        lazy[getLeftIndex(node)] += add;
        lazy[getRightIndex(node)] += add;
      }
      return;
    }

    const int mid = getMidIndex(left, right);
    const int leftIndex = getLeftIndex(node);
    const int rightIndex = getRightIndex(node);
    updateRange(leftIndex, left, mid, queryLeft, queryRight, add);
    updateRange(rightIndex, mid + 1, right, queryLeft, queryRight, add);
    tree[node] = max(tree[leftIndex], tree[rightIndex]);
  }

  int query(int node, int left, int right, int queryLeft, int queryRight) {
    if (left > queryRight || right < queryLeft) return 0;
    if (lazy[node]) {
      tree[node] += lazy[node];
      if (left != right) {
        lazy[getLeftIndex(node)] += lazy[node];
        lazy[getRightIndex(node)] += lazy[node];
      }
      lazy[node] = 0;
    }

    if (left >= queryLeft && right <= queryRight) return tree[node];

    const int mid = getMidIndex(left, right);
    const int leftIndex = getLeftIndex(node);
    const int rightIndex = getRightIndex(node);
    const int leftValue = query(leftIndex, left, mid, queryLeft, queryRight);
    const int rightValue =
        query(rightIndex, mid + 1, right, queryLeft, queryRight);

    return max(leftValue, rightValue);
  };
};

int n, c, m;
int result = 0;
vector<array<int, 3>> infos;
vector<int> acc;

void build() {
  F(i, 0, m) {
    array<int, 3> t;
    F(i, 0, 3) cin >> t[i];
    infos.push_back(t);
  }

  sort(infos.begin(), infos.end(), compare);
}

int getCapacity(int start, int end, SegmentTree& st) {
  return c - st.query(start, end);
}

int main() {
  FASTIO
  cin >> n >> c >> m;
  build();
  acc.resize(n + 1);
  fill(acc.begin(), acc.end(), 0);
  SegmentTree st(acc);

  F(i, 0, m) {
    const int capa =
        min(infos[i][2], getCapacity(infos[i][0], infos[i][1] - 1, st));

    if (capa) {
      st.updateRange(infos[i][0], infos[i][1] - 1, capa);
      result += capa;
    }
  }

  cout << result;

  return 0;
}