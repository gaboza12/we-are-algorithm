#include <array>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

struct Greater {
  bool operator()(array<int, 2>& a, array<int, 2>& b) {
    if (a[1] != b[1]) return a[1] < b[1];

    return a[0] < b[0];
  }
};

struct Less {
  bool operator()(array<int, 2>& a, array<int, 2>& b) {
    if (a[1] != b[1]) return a[1] > b[1];

    return a[0] > b[0];
  }
};

void heapPush(
    priority_queue<array<int, 2>, vector<array<int, 2>>, Less>& minHeap,
    priority_queue<array<int, 2>, vector<array<int, 2>>, Greater>& maxHeap,
    array<int, 2>& v) {
  minHeap.push(v);
  maxHeap.push(v);
}

void setMap(unordered_map<int, int>& map, int v) {
  auto it = map.find(v);

  if (it != map.end()) {
    it->second += 1;
  } else {
    map[v] = 1;
  }
}

template <typename T>
int recommand(priority_queue<array<int, 2>, vector<array<int, 2>>, T>& heap,
              unordered_map<int, int>& map) {
  while (!heap.empty() && map.find(heap.top()[0]) != map.end()) {
    auto it = map.find(heap.top()[0]);
    it->second -= 1;

    if (it->second == 0) {
      map.erase(it);
    }

    heap.pop();
  }

  return heap.top()[0];
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m, v1, v2;
  string s;

  cin >> n;

  priority_queue<array<int, 2>, vector<array<int, 2>>, Greater> maxHeap;
  priority_queue<array<int, 2>, vector<array<int, 2>>, Less> minHeap;
  unordered_map<int, int> maxMap;
  unordered_map<int, int> minMap;

  for (int i = 0; i < n; i += 1) {
    array<int, 2> arr;
    cin >> arr[0] >> arr[1];
    heapPush(minHeap, maxHeap, arr);
  }

  cin >> m;

  for (int i = 0; i < m; i += 1) {
    cin >> s;

    if (s == "add") {
      array<int, 2> arr;
      cin >> arr[0] >> arr[1];
      heapPush(minHeap, maxHeap, arr);
    } else if (s == "recommend") {
      cin >> v1;

      if (v1 == -1) {
        cout << recommand(minHeap, minMap) << '\n';
      } else {
        cout << recommand(maxHeap, maxMap) << '\n';
      }
    } else if (s == "solved") {
      cin >> v1;

      setMap(minMap, v1);
      setMap(maxMap, v1);
    }
  }

  return 0;
}