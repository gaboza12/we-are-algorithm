#include <iostream>
using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(NULL);               \
  cout.tie(NULL);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int n, m;

int getGCD(int a, int b) {
  while (b) {
    const int r = a % b;
    a = b;
    b = r;
  }

  return a;
}

int main() {
  FASTIO;
  cin >> n >> m;
  cout << m - getGCD(n, m);

  return 0;
}
