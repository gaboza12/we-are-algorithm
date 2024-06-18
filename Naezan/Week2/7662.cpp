#include <bits/stdc++.h>

using namespace std;

int T;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> T;

	// T 케이스 반복
	for (int i = 0; i < T; ++i)
	{
		int k;
		cin >> k;
		multiset<int> dqlist;

		for (int j = 0; j < k; ++j)
		{
			char c;
			int n;
			cin >> c >> n;

			if (c == 'I')
			{
				dqlist.emplace(n);
			}
			else if (c == 'D')
			{
				if (dqlist.empty())
				{
					continue;
				}

				// 최댓값 삭제
				if (n == 1)
				{
					auto iter = dqlist.end();
					--iter;
					dqlist.erase(iter);
				}
				// 최솟값 삭제
				else if (n == -1)
				{
					dqlist.erase(dqlist.begin());
				}
			}
		}

		if (dqlist.empty())
		{
			cout << "EMPTY" << '\n';
		}
		else
		{
			cout << *dqlist.rbegin() << " " << *dqlist.begin() << '\n';
		}
	}

	return 0;
}