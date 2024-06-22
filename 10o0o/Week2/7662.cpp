#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

void heapPush(priority_queue<long, vector<long>, greater<long>>& minHeap,
              priority_queue<long>& maxHeap, long v) {
  minHeap.push(v);
  maxHeap.push(v);
}

template <typename T>
string heapPop(priority_queue<long, vector<long>, T>& heap,
               unordered_map<long, int>& map, unordered_map<long, int>& map2) {
  while (!heap.empty() && map.find(heap.top()) != map.end()) {
    auto it = map.find(heap.top());
    it->second -= 1;

    if (it->second == 0) {
      map.erase(it);
    }

    heap.pop();
  }

  if (!heap.empty()) {
    long rv = heap.top();
    auto it = map2.find(rv);

    if (it != map2.end()) {
      it->second += 1;
    } else {
      map2[rv] = 1;
    }

    heap.pop();
    return to_string(rv);
  }

  return "EMPTY";
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int t;
  int n;
  char f;
  long v;

  cin >> t;

  while (t) {
    priority_queue<long, vector<long>, greater<long>> minHeap;
    priority_queue<long, vector<long>> maxHeap;
    unordered_map<long, int> minMap;
    unordered_map<long, int> maxMap;

    cin >> n;

    for (int i = 0; i < n; i += 1) {
      cin >> f >> v;

      if (f == 'I') {
        heapPush(minHeap, maxHeap, v);
      } else {
        if (v == -1) {
          heapPop(minHeap, minMap, maxMap);
        } else {
          heapPop(maxHeap, maxMap, minMap);
        }
      }
    }

    string minV = heapPop(minHeap, minMap, maxMap);
    string maxV = heapPop(maxHeap, maxMap, minMap);

    if (minV == "EMPTY" && maxV == "EMPTY") {
      cout << "EMPTY" << '\n';
    } else if (minV == "EMPTY" || maxV == "EMPTY") {
      string v = minV == "EMPTY" ? maxV : minV;
      cout << v << " " << v << '\n';
    } else {
      cout << maxV << " " << minV << '\n';
    }

    t -= 1;
  }

  return 0;
}