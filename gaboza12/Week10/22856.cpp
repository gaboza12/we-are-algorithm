#include <bits/stdc++.h>

using namespace std;

int n;

vector<int> graph[100005];

bool flag = true;

int end_node;
int ans = 0;

void find_end(int x)
{
	int left_node = graph[x][0];
	int right_node = graph[x][1];

	if (left_node != -1)
		find_end(left_node);

	end_node = x;

	if (right_node != -1)
		find_end(right_node);
}

void func(int x)
{
	int left_node = graph[x][0];
	int right_node = graph[x][1];

	if (left_node != -1)
	{
		ans++;
		func(left_node);

		if (flag)
			ans++;
	}

	if (right_node != -1)
	{
		ans++;
		func(right_node);

		if (flag)
			ans++;
	}

	if (x == end_node)
	{
		flag = false;
		return;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int a, b, c;

		cin >> a >> b >> c;
		graph[a].push_back(b);
		graph[a].push_back(c);
	}

	find_end(1);

	func(1);

	cout << ans;

	return 0;
}