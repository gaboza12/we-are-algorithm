#include <iostream>
#include <vector>

using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);            \
  cout.tie(nullptr);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int t, n;

// 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
// 2, 5, 5, 4, 5, 6, 3, 7, 6, 6

void solve() {
  int minR = n % 7;
  int minRepeat = n / 7;

  if (!minR) {
    F(i, 0, minRepeat) cout << 8;
  } else if (!minRepeat) {
    if (minR == 2) cout << 1;
    if (minR == 3) cout << 7;
    if (minR == 4) cout << 4;
    if (minR == 5) cout << 2;
    if (minR == 6) cout << 6;
  } else {
    int remains = 7 - minR;
    if (remains >= 5) {
      remains -= 5;
      cout << 1;
    } else if (remains >= 2) {
      remains -= 2;
      cout << 2;
    } else if (remains == 1) {
      remains = 0;
      cout << 6;
    }

    F(i, 0, minRepeat - 1) {
      if (remains) {
        remains -= 1;
        cout << 0;
      } else {
        cout << 8;
      }
    }

    if (remains) {
      if (remains == 1) cout << 0;
      if (remains == 2) cout << 2;
      if (remains == 3) cout << 4;
      if (remains == 4) cout << 7;
      if (remains == 5) cout << 1;
    } else {
      cout << 8;
    }
  }

  cout << " ";

  int maxR = n % 2;
  int maxRepeat = n / 2 - 1;

  cout << (maxR ? 7 : 1);
  F(i, 0, maxRepeat) cout << 1;

  cout << "\n";
}

int main() {
  FASTIO
  cin >> t;

  while (t--) {
    cin >> n;
    solve();
  }

  return 0;
}
