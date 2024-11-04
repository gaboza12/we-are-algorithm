#include <bits/stdc++.h>

using namespace std;

int n;
long long ans = 0;

int parent[1005];

vector<pair<int, pair<int, int>>> v;

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

	cin >> n;

	for (int i = 1; i <= n; i++)
		parent[i] = i;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			int cost;
			cin >> cost;

			v.push_back({ cost, {i, j}});
		}
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++)
	{
		int from = v[i].second.first;
		int to = v[i].second.second;
		int cost = v[i].first;

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