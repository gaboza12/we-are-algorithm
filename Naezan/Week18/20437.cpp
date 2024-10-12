#include <bits/stdc++.h>

using namespace std;

int T;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		string s;
		int k;
		cin >> s >> k;

		queue<int> que[26];
		int maxl = -1;
		int minl = s.size() + 1;

		for (int j = 0; j < s.size(); ++j)
		{
			char idx = s[j] - 'a';

			//해당 알파벳의 인덱스 번호를 축적시킴
			if (que[idx].size() < k)
			{
				que[idx].push(j);

				if (que[idx].size() == k)
				{
					int curl = que[idx].back() - que[idx].front() + 1;
					maxl = max(curl, maxl);
					minl = min(curl, minl);
				}
			}
			else
			{
				//k개만큼 채워지면 문자열의 길이를 비교하여 최대 길이와 최소길이를 정함
				que[idx].pop();
				que[idx].push(j);

				int curl = que[idx].back() - que[idx].front() + 1;
				maxl = max(curl, maxl);
				minl = min(curl, minl);
			}
		}

		if (maxl == -1)
		{
			cout << -1 << '\n';
		}
		else
		{
			cout << minl << ' ' << maxl << '\n';
		}
	}

	return 0;
}