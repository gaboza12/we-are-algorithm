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

int n;
vector<int> t, p, dp;
int result = 0;

int main() {
  FASTIO
  cin >> n;
  t.resize(n);
  p.resize(n);
  dp.resize(n + 1, 0);
  F(i, 0, n) cin >> t[i] >> p[i];

  F(i, 0, n) {
    const int day = i + t[i];
    const int money = dp[i] + p[i];
    if (day <= n) {
      dp[day] = max(dp[day], money);
    }

    dp[i + 1] = max(dp[i + 1], dp[i]);
  }

  F(i, 0, n + 1) { result = max(result, dp[i]); }
  cout << result;

  return 0;
}
