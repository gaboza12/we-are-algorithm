#include <iostream>
#include <vector>

using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);            \
  cout.tie(nullptr);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int t, n, m;

void solve() {
  long long dp[n + 1][m + 1] = {0};
  F(i, 1, m + 1) dp[1][i] = 1LL;

  F(i, 1, n) {
    F(j, 1, m + 1) {
      if (j * 2 > m) break;

      F(k, j * 2, m + 1) dp[i + 1][k] += dp[i][j];
    }
  }

  long long sum = 0;
  F(i, 1, m + 1) sum += dp[n][i];
  cout << sum << "\n";
}

int main() {
  FASTIO
  cin >> t;
  while (t--) {
    cin >> n >> m;
    solve();
  }

  return 0;
}
