#include <bits/stdc++.h>

using namespace std;

int t, k;

string w;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t;

	while (t--)
	{
		cin >> w >> k;

		vector<int> alpha[26];

		int mn = 10005, mx = -1;

		for (int i = 0; i < w.size(); i++)
		{
			alpha[w[i] - 'a'].push_back(i);
		}

		for (int i = 0; i < 26; i++)
		{
			if (alpha[i].size() >= k)
			{
				for (int j = 0; j <= alpha[i].size() - k; j++)
				{
					mn = min(mn, alpha[i][j + k - 1] - alpha[i][j] + 1);
					mx = max(mx, alpha[i][j + k - 1] - alpha[i][j] + 1);
				}
			}
		}

		if (mn == 10005 || mx == -1)
			cout << "-1\n";
		else
			cout << mn << " " << mx << "\n";
	}

	return 0;
}