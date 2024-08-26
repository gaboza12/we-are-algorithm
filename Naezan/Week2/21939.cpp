#include <bits/stdc++.h>

using namespace std;

int N, M;

set<pair<int, int>> recolist;
unordered_map<int, int> plist;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int p, l;
		cin >> p >> l;
		plist[p] = l;
		recolist.emplace(l, p);
	}

	cin >> M;

	for (int i = 0; i < M; ++i)
	{
		string s;

		cin >> s;

		if (s == "add")
		{
			int p, l;
			cin >> p >> l;
			plist[p] = l;
			recolist.emplace(l, p);
		}
		else if (s == "recommend")
		{
			int n;
			cin >> n;

			// 가장 어려운 문제 번호 추천
			if (n == 1)
			{
				cout << recolist.rbegin()->second << '\n';
			}
			// 가장 쉬운 문제 번호 추천
			else if (n == -1)
			{
				cout << recolist.begin()->second << '\n';
			}
		}
		else if (s == "solved")
		{
			int p;
			cin >> p;

			recolist.erase({plist[p], p});
			plist.erase(p);
		}
	}

	return 0;
}