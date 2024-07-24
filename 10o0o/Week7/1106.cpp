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

const int MAX = 101010;
int n, c, result = MAX;
vector<int> fees, customers, dists;
priority_queue<pii, vector<pii>, greater<pii>> minHeap;

int main() {
  FASTIO
  cin >> c >> n;
  fees.resize(n);
  customers.resize(n);
  dists.resize(c, MAX);
  F(i, 0, n) cin >> fees[i] >> customers[i];
  dists[0] = 0;
  minHeap.push({0, 0});

  while (minHeap.size()) {
    pii top = minHeap.top();
    minHeap.pop();
    if (dists[top.second] < top.first) continue;
    F(i, 0, n) {
      const int newFee = top.first + fees[i];
      const int newCustomer = top.second + customers[i];

      if (newCustomer >= c) {
        result = min(result, newFee);
      } else {
        if (dists[newCustomer] <= newFee) continue;
        dists[newCustomer] = newFee;
        minHeap.push({newFee, newCustomer});
      }
    }
  }

  cout << result;

  return 0;
}
