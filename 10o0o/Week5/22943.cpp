#include <algorithm>
#include <cmath>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(NULL);               \
  cout.tie(NULL);

#define F(i, a, b) for (int i = a; i < b; i += 1)
#define FR(i, b, a) for (int i = b; i >= a; i -= 1)

int k, m, t, counts, numMax;
unordered_set<int> primesSet;
vector<int> primes;
vector<int> et;
vector<int> nums;
int digits[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int visited[10] = {};

void build() {
  et.resize(numMax);
  fill(et.begin(), et.end(), 0);
  F(i, 2, numMax) {
    if (!et[i]) {
      primes.push_back(i);
      primesSet.insert(i);
      for (int j = i; j < et.size(); j += i) et[j] = 1;
    }
  }
}

void makeNums(int acc, int counts) {
  if (counts == k) {
    nums.push_back(acc);
    return;
  }

  acc *= 10;

  F(i, 0, 10) {
    if (visited[i]) continue;
    if (counts == 0 && (i == 0 && k != 1)) continue;
    visited[i] = 1;
    makeNums(acc + digits[i], counts + 1);
    visited[i] = 0;
  }
}

bool condition1(int num) {
  F(j, 0, primes.size()) {
    if (primes[j] >= num / 2) break;
    const int diff = num - primes[j];
    if ((primesSet.find(diff) != primesSet.end())) {
      return true;
    }
  }

  return false;
}

bool condition2(int x) {
  F(i, 0, primes.size()) {
    if (pow(x, 2) < primes[i]) break;
    while (x % m == 0) x /= m;
    const int remains = x % primes[i];
    if (remains) continue;
    const int divided = x / primes[i];
    if (primesSet.find(divided) != primesSet.end()) {
      return true;
    }
  }

  return false;
}

int main() {
  FASTIO;
  cin >> k >> m;
  counts = 0;
  numMax = pow(10, k);
  build();
  makeNums(0, 0);

  F(i, 0, nums.size()) {
    if (condition1(nums[i]) && condition2(nums[i])) {
      counts += 1;
    }
  }

  cout << counts;
  return 0;
}
