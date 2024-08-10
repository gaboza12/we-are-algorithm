#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

int n, d, k, c;

int ans = 0;

int arr[3000005];

unordered_map<int, int> um;//map으로 하면 시간초과

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> d >> k >> c;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < k - 1; i++)
	{
		um[arr[i]]++;
	}

	int st = 0, ed = k - 1;

	for (int i = 0; i < n; i++)
	{
		int del = arr[st];//제일처음초밥(삭제)
		int cur = arr[ed % n];

		um[cur]++;

		int num = um.size();

		if (um.find(c) == um.end())//쿠폰 초밥이 없으면
			ans = max(ans, num + 1);
		else
			ans = max(ans, num);

		um[del]--;
		if (um[del] == 0)
		{
			um.erase(um.find(del));
		}

		st++;
		ed++;
	}

	cout << ans;

	return 0;
}