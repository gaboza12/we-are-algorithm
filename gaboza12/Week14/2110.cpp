#include <bits/stdc++.h>

using namespace std;

int n, c;

vector<int> house;

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> n >> c;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;

		house.push_back(temp);
	}

	sort(house.begin(), house.end());

	int start = 0, end = house[n - 1];

	while (start <= end)
	{
		int install = 1;//설치한 공유기

		int dist = (start + end) / 2;

		int st = house[0];

		for (int i = 1; i < n; i++)
		{
			int ed = house[i];

			if (ed - st >= dist)
			{
				install++;
				st = ed;
			}
		}

		if (install >= c)
		{
			ans = dist;

			start = dist + 1;
		}
		else
		{
			end = dist - 1;
		}
	}

	cout << ans;

	return 0;
}
