#include <iostream>
#include <vector>

using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);            \
  cout.tie(nullptr);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int n, m, dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
vector<vector<int>> map;
vector<vector<int>> dpMap;

bool isValidPos(int i, int j) { return i >= 0 && j >= 0 && i < n && j < m; }

int dp(int i, int j) {
  if (!i && !j) return 1;
  if (dpMap[i][j] != -1) return dpMap[i][j];

  int ret = 0;

  F(k, 0, 4) {
    int mi = i + dx[k];
    int mj = j + dy[k];

    if (!isValidPos(mi, mj) || map[i][j] >= map[mi][mj]) continue;
    ret += dp(mi, mj);
  }

  dpMap[i][j] = ret;
  return ret;
}

int main() {
  FASTIO
  cin >> n >> m;
  map.resize(n, vector<int>(m));
  dpMap.resize(n, vector<int>(m, -1));

  F(i, 0, n) F(j, 0, m) cin >> map[i][j];

  cout << dp(n - 1, m - 1);
  return 0;
}
