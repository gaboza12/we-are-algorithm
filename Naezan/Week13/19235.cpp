#include <bits/stdc++.h>

using namespace std;

int N;

int blue[4][6];
int green[6][4];

int score;
int bgcount;

struct DInfo
{
	int x, y, t;
};

void movetile(int x, int y, int t)
{
	if (t == 1)
	{
		//블루는 가로
		int idx = 5;
		for (int i = 0; i < 6; ++i)
		{
			if (blue[y][i] > 0 && i > 0)
			{
				idx = i - 1;
				break;
			}
		}
		blue[y][idx] = 1;

		//그린은 세로
		idx = 5;
		for (int i = 0; i < 6; ++i)
		{
			if (green[i][x] > 0 && i > 0)
			{
				idx = i - 1;
				break;
			}
		}
		green[idx][x] = 1;
	}
	else if (t == 2)//가로블럭
	{
		//블루는 가로2
		int idx = 4;
		for (int i = 0; i < 6; ++i)
		{
			if (blue[y][i] > 0)
			{
				idx = i - 2;
				break;
			}
		}

		blue[y][idx] = 2;
		blue[y][idx + 1] = 2;

		//그린
		idx = 5;
		for (int i = 0; i < 6; ++i)
		{
			if (green[i][x] > 0 || green[i][x + 1] > 0)
			{
				idx = i - 1;
				break;
			}
		}

		green[idx][x] = 2;
		green[idx][x + 1] = 2;
	}
	else if (t == 3)//세로블럭
	{
		//블루
		int idx = 5;
		for (int i = 0; i < 6; ++i)
		{
			if (blue[y][i] > 0 || blue[y + 1][i] > 0)
			{
				idx = i - 1;
				break;
			}
		}

		blue[y][idx] = 3;
		blue[y + 1][idx] = 3;

		//그린은 세로2
		idx = 4;
		for (int i = 0; i < 6; ++i)
		{
			if (green[i][x] > 0)
			{
				idx = i - 2;
				break;
			}
		}

		green[idx][x] = 3;
		green[idx + 1][x] = 3;
	}
}

void tetrisblue()
{
	bool ischanged = false;
	//없애기
	for (int i = 2; i < 6; ++i)
	{
		bool isbg = true;
		for (int j = 0; j < 4; ++j)
		{
			if (blue[j][i] == 0)
			{
				isbg = false;
				break;
			}
		}

		if (isbg)
		{
			ischanged = true;
			++score;
			for (int j = 0; j < 4; ++j)
			{
				blue[j][i] = 0;
			}
		}
	}

	//방향으로 다운
	if (ischanged)
	{
		for (int i = 4; i >= 0; --i)
		{
			queue<DInfo> cq;
			//q에 내릴 녀석을 등록
			if (blue[1][i] == 3 && blue[2][i] == 3)
			{
				cq.push({ i, 1, 3 });
			}
			else
			{
				if (blue[0][i] == 3 && blue[1][i] == 3)
				{
					cq.push({ i, 0, 3 });
				}
				if (blue[2][i] == 3 && blue[3][i] == 3)
				{
					cq.push({ i, 2, 3 });
				}
			}

			for (int j = 0; j < 4; ++j)
			{
				if (blue[j][i] != 3)
				{
					cq.push({ i, j, blue[j][i] });
				}
			}

			while (!cq.empty())
			{
				DInfo info = cq.front();
				cq.pop();

				int dx = info.x;
				int dy = info.y;

				int tempx = 5;
				//q에서 해당 좌표의 아랫방향을 모두 검사하여 내려줌
				for (int j = i + 1; j < 6; ++j)
				{
					//다른 블럭이 있으면 루프 종료

					//3인 경우 y좌표 + 1까지 비교
					if (info.t == 3)
					{
						if (blue[dy][j] || blue[dy + 1][j])
						{
							tempx = j - 1;
							break;
						}
					}
					else
					{
						if (blue[dy][j])
						{
							tempx = j - 1;
							break;
						}
					}
				}

				if (info.t == 3)
				{
					swap(blue[dy][tempx], blue[dy][dx]);
					swap(blue[dy + 1][tempx], blue[dy + 1][dx]);
				}
				else
					swap(blue[dy][tempx], blue[dy][dx]);
			}
		}

		tetrisblue();
	}
}

void tetrisgreen()
{
	bool ischanged = false;
	for (int i = 2; i < 6; ++i)
	{
		bool isbg = true;
		for (int j = 0; j < 4; ++j)
		{
			if (green[i][j] == 0)
			{
				isbg = false;
				break;
			}
		}

		if (isbg)
		{
			ischanged = true;
			++score;
			for (int j = 0; j < 4; ++j)
			{
				green[i][j] = 0;
			}
		}
	}

	//내리기
	if (ischanged)
	{
		for (int i = 4; i >= 0; --i)
		{
			queue<DInfo> cq;
			//q에 내릴 녀석을 등록
			if (green[i][1] == 2 && green[i][2] == 2)
			{
				cq.push({ 1, i, 2 });
			}
			else
			{
				if (green[i][0] == 2 && green[i][1] == 2)
				{
					cq.push({ 0, i, 2 });
				}
				if (green[i][2] == 2 && green[i][3] == 2)
				{
					cq.push({ 2, i, 2 });
				}
			}

			for (int j = 0; j < 4; ++j)
			{
				if (green[i][j] != 2)
				{
					cq.push({ j, i, green[i][j] });
				}
			}

			while (!cq.empty())
			{
				DInfo info = cq.front();
				cq.pop();

				int dx = info.x;
				int dy = info.y;

				int tempy = 5;
				//q에서 해당 좌표의 아랫방향을 모두 검사하여 내려줌
				for (int j = i + 1; j < 6; ++j)
				{
					//다른 블럭이 있으면 루프 종료

					//2인 경우 x좌표 + 1까지 비교
					if (info.t == 2)
					{
						if (green[j][dx] || green[j][dx + 1])
						{
							tempy = j - 1;
							break;
						}
					}
					else
					{
						if (green[j][dx])
						{
							tempy = j - 1;
							break;
						}
					}
				}

				if (info.t == 2)
				{
					swap(green[tempy][dx], green[dy][dx]);
					swap(green[tempy][dx + 1], green[dy][dx + 1]);
				}
				else
					swap(green[tempy][dx], green[dy][dx]);
			}
		}

		tetrisgreen();
	}
}

void pushblue()
{
	int pushc = 0;
	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (blue[j][i] > 0)
			{
				++pushc;
				break;
			}
		}
	}

	if (pushc > 0)
	{
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 5; j >= 2; --j)
			{
				blue[i][j] = blue[i][j - pushc];
			}
		}
	}

	//연한칸 비우기
	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			blue[j][i] = 0;
		}
	}
}

void pushgreen()
{
	int pushc = 0;
	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (green[i][j] > 0)
			{
				++pushc;
				break;
			}
		}
	}

	if (pushc > 0)
	{
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 5; j >= 2; --j)
			{
				green[j][i] = green[j - pushc][i];
			}
		}
	}

	//연한칸 비우기
	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			green[i][j] = 0;
		}
	}
}

void calc()
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 2; j < 6; ++j)
		{
			if (blue[i][j] > 0)
			{
				++bgcount;
			}
		}
	}

	for (int i = 2; i < 6; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (green[i][j] > 0)
			{
				++bgcount;
			}
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int t, x, y;
		cin >> t >> y >> x;

		//각 타일 방향 이동
		movetile(x, y, t);

		//행 및 열 테트리스 진행
		tetrisblue();
		tetrisgreen();

		//연한칸 있으면 밀기
		pushblue();
		pushgreen();
	}

	calc();

	cout << score << '\n';
	cout << bgcount << '\n';

	return 0;
}