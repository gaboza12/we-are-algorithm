#include <bits/stdc++.h>

using namespace std;

int n;

void func(int num)
{
	if (num == 0)
	{
		cout << "-";
		return;
	}

	func(num - 1);
	
	for (int i = 0; i < pow(3, num - 1); i++)
	{
		cout << " ";
	}

	func(num - 1);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	

	while (1)
	{
		cin >> n;

		if (cin.eof())
			break;

		func(n);
		cout << "\n";
	}

	return 0;
}