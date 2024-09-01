#include <bits/stdc++.h>

using namespace std;

int n, p, q;
vector<int> num;
int ans = 1;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		num.push_back(temp);
	}

	sort(num.begin(), num.end());

	cin >> p >> q;

	vector<int> v;
	vector<vector<int>> v2;

	for (int i = 0; i < p; i++)
	{
		v.push_back(0);
	}

	for (int i = 0; i < q; i++)
	{
		v.push_back(1);
	}

	do
	{
		v2.push_back(v);
	} while (next_permutation(v.begin(), v.end()));

	do
	{
		for (auto nxt : v2)
		{
			vector<int> vec;
			int temp = num[0];
			for (int i = 0; i < nxt.size(); ++i)
			{
				if (nxt[i])
				{
					vec.push_back(temp);
					temp = num[i + 1];
				}
				else
				{
					temp += num[i + 1];
				}
			}

			vec.push_back(temp);

			int sum = 1;
			for (int i = 0; i < vec.size(); ++i)
			{
				sum *= vec[i];
			}

			ans = max(ans, sum);
		}

	} while (next_permutation(num.begin(), num.end()));

	if (n == 1)
		ans = num[0];

	cout << ans;

	return 0;
}