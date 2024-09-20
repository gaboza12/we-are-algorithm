#include <bits/stdc++.h>

using namespace std;

int n;

vector<int> v;

int ans1 = 0, ans2 = 0;
int num = 2000000000;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	sort(v.begin(), v.end());

	int st = 0, en = n - 1;

	while (st < en)
	{
		int sum = v[st] + v[en];

		if (abs(sum) < num)
		{
			num = abs(sum);

			ans1 = v[st];
			ans2 = v[en];

			if (sum == 0)
				break;
		}

		if (sum < 0)
			st++;
		else
			en--;
	}

	cout << ans1 << " " << ans2;

	return 0;
}
