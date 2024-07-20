#include<bits/stdc++.h>

using namespace std;

int n, k;
int ans = 0;

vector<int> v, dist;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	sort(v.begin(), v.end());

	//센서 사이의 거리
	for (int i = 0; i < n - 1; i++)
	{
		dist.push_back(v[i + 1] - v[i]);
	}

	//크기가 큰순서대로
	sort(dist.begin(), dist.end(), greater<int>());

	//큰 순서부터 k-1개를 제외하면 최소거리(k개의 집중국을 세우면 집중국 사이의 빈공간은 k-1개)
	for (int i = k - 1; i < dist.size(); i++)
	{
		ans += dist[i];
	}

	cout << ans;

	return 0;
}