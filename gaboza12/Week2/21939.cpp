#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	int N, M, L, P;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> easy;
	priority_queue<pair<int, int>> hard;
	map<pair<int, int>, bool> vis;
	map<int, int> PL;//번호와 레벨 묶기

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> P >> L;

		easy.push({ L, P });
		hard.push({ L, P });
		vis[{L, P}] = false;
		PL[P] = L;
	}

	cin >> M;

	for (int i = 0; i < M; i++)
	{
		while (vis[easy.top()])
		{
			easy.pop();
		}

		while (vis[hard.top()])
		{
			hard.pop();
		}

		string cmd;
		int x;

		cin >> cmd;

		if (cmd == "add")
		{
			cin >> P >> L;

			easy.push({ L, P });
			hard.push({ L, P });
			vis[{L, P}] = false;
			PL[P] = L;
		}
		else if (cmd == "recommend")
		{
			cin >> x;
			if (x == 1)
			{
				cout << hard.top().second << "\n";
			}
			else
			{
				cout << easy.top().second << "\n";
			}
		}
		else
		{
			cin >> P;

			vis[{PL[P], P}] = true;
		}
	}

	return 0;
}