#include<bits/stdc++.h>
using namespace std;

int robot[1000005];
int cnt[1000005];

int find(int x)
{
	if (robot[x] == x)
		return x;
	
	return robot[x] = find(robot[x]);
}

void Union(int a, int b)
{
	a = find(a);
	b = find(b);

	if (a == b)
		return;

	cnt[a] += cnt[b];
	robot[b] = robot[a];
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, a, b;
	char input_char;
	
	cin >> N;

	for (int i = 0; i < 1000005; i++)
	{
		robot[i] = i;
		cnt[i] = 1;
	}

	while (N--)
	{
		cin >> input_char;

		if (input_char == 'I')
		{
			cin >> a >> b;
			Union(a, b);
		}
		else if (input_char == 'Q')
		{
			cin >> a;
			cout << cnt[find(a)] << "\n";
		}
	}

	return 0;
}