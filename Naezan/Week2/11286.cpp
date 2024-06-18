#include <bits/stdc++.h>

using namespace std;

int N;

struct Compare
{
	bool operator()(const pair<int, int>& lp, const pair<int, int>& rp)
	{
		if (lp.first != rp.first)
		{
			return lp.first > rp.first;
		}
		
		return lp.second > rp.second;
	}
};

priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int n;
		cin >> n;

		if (n != 0)
		{
			pq.emplace(abs(n), n);
		}
		else
		{
			if (!pq.empty())
			{
				cout << pq.top().second << '\n';
				pq.pop();
			}
			else
			{
				cout << "0" << '\n';
			}
		}
	}

	return 0;
}