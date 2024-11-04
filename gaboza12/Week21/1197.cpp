#include <bits/stdc++.h>

using namespace std;

int v, e;
int ans = 0;

int parent[10005];

vector<pair<int, pair<int, int>>> vec;

int find(int x)
{
	if (parent[x] == x)
		return x;

	return parent[x] = find(parent[x]);
}

void uni(int x, int y)
{
	x = find(x);
	y = find(y);

	if (x == y)
		return;

	if (parent[x] < parent[y])
		swap(x, y);

	parent[y] = x;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> v >> e;

	for (int i = 1; i <= v; i++)
		parent[i] = i;

	for (int i = 0; i < e; i++)
	{
		int a, b, c;

		cin >> a >> b >> c;

		vec.push_back({ c,{a, b} });
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); i++)
	{
		int from = vec[i].second.first;
		int to = vec[i].second.second;
		int cost = vec[i].first;

		int a = find(from);
		int b = find(to);

		if (a != b)
		{
			uni(a, b);
			ans += cost;
		}
	}
	
	cout << ans;

	return 0;
}