#include <bits/stdc++.h>

using namespace std;

int N, P, Q;

vector<int> vec;
vector<vector<bool>> opers;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	vec.resize(N, 0);
	for (int i = 0; i < N; ++i)
	{
		cin >> vec[i];
	}

	sort(vec.begin(), vec.end());

	cin >> P >> Q;

	//true이면 *연산이고 연산위치는 인덱스 + 1
	vector<bool> oper;
	oper.resize(N - 1, false);
	for (int i = 0; i < Q; ++i)
	{
		oper[i] = true;
	}

	//모든 조합 저장
	do
	{
		opers.push_back(oper);
	} while (prev_permutation(oper.begin(), oper.end()));

	// next_permutation으로 모든 순열 구함(시간복잡도 N * N!, 여기선 32만)
	int ans = 1;
	do
	{
		//Q의 갯수만큼 *를 임의의 위치에 넣고 연산결과 저장
		for (const vector<bool>& op : opers)
		{
			vector<int> tempvec;
			int temp = vec[0];
			for (int i = 0; i < op.size(); ++i)
			{
				//곱셈인 경우
				if (op[i])
				{
					//temp에 있는 값 vector에 축척
					tempvec.push_back(temp);
					temp = vec[i + 1];
				}
				else
				{
					temp += vec[i + 1];
				}
			}

			tempvec.push_back(temp);

			int tempans = 1;
			for (int i = 0; i < tempvec.size(); ++i)
			{
				tempans *= tempvec[i];
			}

			ans = max(ans, tempans);
		}

	} while (next_permutation(vec.begin(), vec.end()));

	if (N == 1)
	{
		ans = vec[0];
	}

	cout << ans;

	return 0;
}