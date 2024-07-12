#include <bits/stdc++.h>

using namespace std;

long long N;
long long ans;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	long long cA, cB, pA, pB;
	cin >> N >> cA >> pA >> cB >> pB;

	ans = pow(10, 18);

	// 큰 값이 가성비가 더 좋음(장매 개수 기준)
	if (cA * pB < cB * pA)
	{
		// 가성비 좋은 값을 A에 저장
		swap(cA, cB);
		swap(pA, pB);
	}

	//가성비 안좋은 장미의 묶음 개수는 아무리 많아봐야 cA보다 작다
	//그 이유는 최소공배수가 cA * cB이므로 가성비 좋은 녀석을 다쓰고나면 최소 남은 N개는 cA * cB이고
	//해당 장미를 cB를 통해 묶을 경우 cA보다 적게 쓸 수 밖에 없음
	for (long long i = 0; i < cA; ++i)
	{
		//가성비 안좋은 장미를 산 후 남은 장미 수
		long long extrRose = N - i * cB;
		//나머지는 가성비 좋은 장미 묶음 개수
		long long tempA = (long long)ceil((double)extrRose / cA);

		if (tempA >= 0)
		{
			ans = min(ans, tempA * pA + i * pB);
		}
		else
		{
			ans = min(ans, i * pB);
			break;
		}
	}

	cout << ans;

	return 0;
}