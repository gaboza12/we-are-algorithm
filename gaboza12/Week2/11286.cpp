#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, x;
	
	priority_queue<int, vector<int>, greater<int>> positive; //양수
	priority_queue<int> negative;//음수

	vector<int> ans;
	
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> x;

		if (x > 0)
		{
			positive.push(x);
		}
		else if (x < 0)
		{
			negative.push(x);
		}
		else
		{
			//둘다 비어있을때
			if (positive.size() == 0 && negative.size() == 0)
			{
				cout << "0\n";
			}
			//양수배열은 비어있고 음수배열은 비어있지않을때 
			else if (positive.size() == 0 && negative.size() != 0)
			{
				cout << negative.top() << "\n";
				negative.pop();
			}
			//양수배열은 비어있지않고 음수배열은 비어있을때
			else if (positive.size() != 0 && negative.size() == 0)
			{
				cout << positive.top() << "\n";
				positive.pop();
			}
			//배열 두개다 비어있지 않을때
			else
			{
				if (abs(negative.top()) <= positive.top())
				{
					cout << negative.top() << "\n";
					negative.pop();
				}
				else
				{
					cout << positive.top() << "\n";
					positive.pop();
				}
			}
		}
	}

	return 0;
}
