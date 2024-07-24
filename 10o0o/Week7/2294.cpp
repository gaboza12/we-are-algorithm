#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(NULL);               \
  cout.tie(NULL);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, a, b) for (int i = b - 1; i >= a; i -= 1)
typedef pair<int, int> pii;

struct Compare {
  bool operator()(const pii &a, const pii &b) {
    if (a.first != b.first) return a.first > b.first;
    return a.second < b.second;
  };
};

const int MAX_DIST = 10'001;
int n, k;
vector<int> coins, dists;
priority_queue<pii, vector<pii>, Compare> minHeap;

int main() {
  FASTIO
  cin >> n >> k;
  coins.resize(n);
  dists.resize(k + 1, MAX_DIST);
  F(i, 0, n) {
    cin >> coins[i];
    if (coins[i] <= k) {
      minHeap.push({1, coins[i]});
      dists[coins[i]] = 1;
    }
  }

  while (minHeap.size()) {
    pii top = minHeap.top();
    minHeap.pop();

    if (dists[top.second] < top.first) continue;
    F(i, 0, n) {
      const int forward = top.second + coins[i];
      if (forward > k) continue;
      if (dists[forward] <= top.first + 1) continue;
      dists[forward] = top.first + 1;
      minHeap.push({top.first + 1, forward});
    }
  }

  cout << (dists[k] == MAX_DIST ? -1 : dists[k]);

  return 0;
}
