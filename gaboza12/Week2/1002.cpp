#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	int T;
	int x1, y1, r1, x2, y2, r2;

	cin >> T;

	while (T--)
	{
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		int d = pow(x1 - x2, 2) + pow(y1 - y2, 2);//두 지점의 거리

		int temp1 = pow(r1 - r2, 2);//반지름의 차
		int temp2 = pow(r1 + r2, 2);//반지름의 합

		if (d == 0)//중심이 같을때
		{
			if (temp1 == 0)//중심이 같고 반지름도 같음
			{
				cout << "-1\n";
			}
			else//중심이 같고 반지름은 다름(원안에 원이 있는형태)
			{
				cout << "0\n";
			}
		}
		else if (d == temp1 || d == temp2)//내접 or 외접
		{
			cout << "1\n";
		}
		else if (temp1 < d && d < temp2)//반지름의 차보다는 크고 합보다는 작을때(두점에서 만남)
		{
			cout << "2\n";
		}
		else//멀리 떨어져 안만남
		{
			cout << "0\n";
		}
	}

	return 0;
}