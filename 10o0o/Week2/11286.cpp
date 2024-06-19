#include <iostream>
#include <queue>

using namespace std;

struct Compare {
  bool operator()(long a, long b) {
    if (abs(a) != abs(b)) {
      return abs(a) > abs(b);
    }

    return a > b;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  long arr[100110];
  int n;
  cin >> n;

  priority_queue<long, vector<long>, Compare> heap;

  for (int i = 0; i < n; i += 1) {
    long x;
    cin >> x;

    if (x == 0) {
      if (heap.empty()) {
        cout << 0 << '\n';
      } else {
        cout << heap.top() << '\n';
        heap.pop();
      }
    } else {
      heap.push(x);
    }
  }

  return 0;
}