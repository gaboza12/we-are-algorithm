#include <bits/stdc++.h>

using namespace std;

int n, m;
int parent[1005];

vector<pair<int, int>> v1, v2;
vector<pair<double, pair<int, int>>> vec;

double ans = 0;

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

	//소수점 고정
	cout << fixed;
	cout.precision(2);

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		parent[i] = i;

	for (int i = 0; i < n; i++)
	{
		int x, y;

		cin >> x >> y;

		v1.push_back({ x, y });
	}

	for (int i = 0; i < m; i++)
	{
		int a, b;

		cin >> a >> b;

		a = find(a);
		b = find(b);

		if (a != b)
			uni(a, b);
	}

	for (int i = 0; i < n - 1; i++)
	{
		int x1 = v1[i].first;
		int y1 = v1[i].second;

		for (int j = i + 1; j < n; j++)
		{
			int x2 = v1[j].first;
			int y2 = v1[j].second;

			double d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
			
			vec.push_back({ d, {i + 1, j + 1} });
		}
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); i++)
	{
		int from = vec[i].second.first;
		int to = vec[i].second.second;
		double cost = vec[i].first;

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