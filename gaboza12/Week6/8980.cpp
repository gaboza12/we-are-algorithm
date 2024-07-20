#include<bits/stdc++.h>

using namespace std;

int n, c, m;//마을 수, 트럭 용량, 박스 정보 개수

vector<pair<pair<int, int>, int>> box;//<<보내는 마을, 받는 마을>, 상자개수>

int dest[2005];
int ans = 0;

bool compare(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b)
{
	return a.first.second < b.first.second;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> c;
	cin >> m;
	
	for (int i = 0; i < m; i++)
	{
		int from, to, num;

		cin >> from >> to >> num;

		box.push_back({ {from, to}, num });
	}


	sort(box.begin(), box.end(), compare);

	for (int i = 0; i < box.size(); i++)
	{
		int from = box[i].first.first;
		int to = box[i].first.second;
		int num = box[i].second;
		int mx_box = 0;

		for (int j = from; j < to; j++)
		{
			mx_box = max(mx_box, dest[j]);
		}

		int take_box = min(num, c - mx_box);

		for (int j = from; j < to; j++)
		{
			dest[j] += take_box;
		}
		ans += take_box;
	}

	cout << ans;

	return 0;
}