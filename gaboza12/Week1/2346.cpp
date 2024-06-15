#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;

	cin >> n;

	deque<pair<int, int>> dq;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		dq.push_back({ temp, i + 1 });
	}

	while (!dq.empty())
	{
		int num = dq.front().first;
		cout << dq.front().second << " ";
		dq.pop_front();

		if (dq.empty()) break;

		if (num > 0)
		{
			for (int i = 0; i < num - 1; i++)
			{
				dq.push_back(dq.front());
				dq.pop_front();
			}
		}
		else
		{
			num = abs(num);
			for (int i = 0; i < num; i++)
			{
				dq.push_front(dq.back());
				dq.pop_back();
			}
		}
	}

	return 0;
}