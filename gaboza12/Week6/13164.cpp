#include<bits/stdc++.h>

using namespace std;

int n, k;
int student[300005];
int diff[300005];

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	for (int i = 0; i < n; i++)
	{
		cin >> student[i];
	}
	
	for (int i = 0; i < n - 1; i++)
	{
		diff[i] = student[i + 1] - student[i];
	}

	sort(diff, diff + n - 1);

	for (int i = 0; i < n - k; i++)
	{
		ans += diff[i];
	}

	cout << ans;

	return 0;
}