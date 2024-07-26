#include <bits/stdc++.h>

// 출발지역 기준으로 풀어서 시간초과 -> 도착지역 기준으로 풀면 풀린다는 글을 봄
// (생각했던 방법이긴했으나 도착지역 기준으로 해도 반복이 많을 것 같아 못풀릴 거라고 생각함..)
//  -> multimap사용했으나 정렬이 불안정 -> pair로 변경해서 품

using namespace std;

int N, C, M, ans;

int arr[2001][2001];
//담은 택배 수
int hold[2001];
vector<pair<int, int>> vec;

bool compare(pair<int, int> l, pair<int, int> r)
{
	if (l.second == r.second)
	{
		return l.first < r.first;
	}

	return l.second < r.second;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> C >> M;

	for (int i = 0; i < M; ++i)
	{
		int s, r, c;

		cin >> s >> r >> c;
		vec.push_back({ s, r });
		arr[s][r] = c;
	}

	//도착 지역 기준 오름차순 정렬
	sort(vec.begin(), vec.end(), compare);

	for (int i = 0; i < vec.size(); ++i)
	{
		//이 부분에서 반복이 많을 것이라고 생각했음..
		int biggest = 0;
		for (int j = vec[i].first; j < vec[i].second; ++j)
		{
			//경유지 중 가장 많이 담긴 경유지의 택배량
			biggest = max(biggest, hold[j]);
		}

		//담을 수 있는 수용량
		int anscap = min(C - biggest, arr[vec[i].first][vec[i].second]);
		//경유지에 총 수용중인 양 갱신
		for (int j = vec[i].first; j < vec[i].second; ++j)
		{
			hold[j] += anscap;
		}

		ans += anscap;
	}

	cout << ans;

	return 0;
}