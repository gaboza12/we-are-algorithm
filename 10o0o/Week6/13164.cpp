#include <algorithm>
#include <iostream>

using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(NULL);               \
  cout.tie(NULL);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int n, k;

int main() {
  FASTIO
  cin >> n >> k;
  int dists[n], diffs[n - 1];
  F(i, 0, n) cin >> dists[i];
  F(i, 1, n) diffs[i - 1] = dists[i] - dists[i - 1];
  sort(diffs, diffs + n - 1, greater<int>());
  int result = dists[n - 1] - dists[0];
  F(i, 0, k - 1) result -= diffs[i];
  cout << result;
  return 0;
}
