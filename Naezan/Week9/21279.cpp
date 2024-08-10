#include <bits/stdc++.h>

using namespace std;

int N, C;

// 14/16

/*
파산하지 않고 얻을 수 있는 아름다움최댓값
50만번 안에 해결필요
*/

struct Stone
{
	int x, y;
	long long vf;
};

struct PqCmp
{
	bool operator()(const Stone& ls, const Stone& rs)
	{
		return ls.y < rs.y;
	}
};

//x -> y 큰값이 뒤로가도록 정렬
vector<Stone> vec;
// y값을 기준으로 정렬
priority_queue<Stone, vector<Stone>, PqCmp> pq;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> C;

	vec.resize(N, Stone());
	for (int i = 0; i < N; ++i)
	{
		int x, y, v;

		cin >> x >> y >> v;
		vec[i].x = x;
		vec[i].y = y;
		vec[i].vf = v;
	}

	sort(vec.begin(), vec.end(), [](const Stone& ls, const Stone& rs)
		{
			if (ls.x == rs.x)
			{
				return ls.y < rs.y;
			}

			return ls.x < rs.x;
		});

	long long ans = 0;
	//C만큼 초반엔 입력받음
	for (int i = 0; i < C; ++i)
	{
		pq.push({ vec[i] });
		ans += vec[i].vf;
	}

	//다음값 검사
	long long tempans = ans;
	int en = C;
	while (en < N)
	{
		Stone s = pq.top();
		pq.pop();

		//en에 있는 y값이 최댓값보다 크면 무시
		while (en < N && s.y <= vec[en].y)
		{
			++en;
		}

		if (en >= N)
		{
			break;
		}

		tempans -= s.vf;

		//최댓값 y와 같은 pq요소 제거
		Stone temps = pq.top();
		while (s.y == temps.y)
		{
			pq.pop();
			tempans -= temps.vf;
			temps = pq.top();
		}

		//s.y보다 작은값들을 모두 추가해서 더해주기
		while (en < N && vec[en].y < s.y)
		{
			pq.push({ vec[en] });
			tempans += vec[en].vf;
			++en;

			//크기가 C가 되면 중단
			if (pq.size() == C)
			{
				break;
			}
		}

		ans = max(ans, tempans);
	}

	cout << ans;

	return 0;
}