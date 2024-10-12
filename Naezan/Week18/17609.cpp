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
		cin >> s;

		int ans = 0;

		int half = s.size() / 2;
		int en = s.size() - 1;
		bool bsim = false;
		int cachej = -1;
		for (int j = 0; j < half;)
		{
			if (s[j] == s[en - j])
			{
				++j;
				continue;
			}

			if (bsim)
			{
				ans = 2;
				break;
			}
			else
			{
				ans = 1;
				bsim = true;
				--en;

				//반대편 유사회문 체크할때 사용
				cachej = j;
			}
		}

		if (cachej != -1 && ans == 2)
		{
			//임시 시작점
			int stoffset = 0;
			en = s.size() - 1;
			bsim = false;
			for (int j = cachej; j < half;)
			{
				if (s[stoffset + j] == s[en - j])
				{
					++j;
					continue;
				}

				if (bsim)
				{
					ans = 2;
					break;
				}
				else
				{
					ans = 1;
					bsim = true;
					++stoffset;
				}
			}
		}

		cout << ans << '\n';
	}

	return 0;
}