// 푸는중
#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

struct Stem {
	int y, x; // 좌표
	int life; // 생명력 수치
	int time; // 얼마나 시간이 지났는지
	int state;// 줄기세포 상태 (0: 없음, 1: 비활성, 2: 활성, -1: 죽음)
};

int n, m, k; // 세로(n), 가로(m), 배양 시간(k)
Stem grid[351][351]; 

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0, -1,1 };

struct cmp {
	bool operator()(Stem a, Stem b) {
		// 생명력이 높은 순서대로 정렬
		return a.life < b.life;
	}
};

// 활성화 된 줄기 세포를 넣어서 정렬되는 PQ
priority_queue<Stem, vector<Stem>, cmp> pq;
// 시간에 대해 넣는 queue
queue<Stem> q;

int func() {
	int cntTime = 0;
	while (cntTime < k) {
		// 1. 시간 한 cycle
		int qNum = q.size();
		for (int i = 0; i < qNum; i++) {
			Stem now = q.front();
			q.pop();

			now.time++; // 한시간 지남

			// 활성화
			if (now.time == now.life) {
				now.state = 2;
			}

			// 번식
			if (now.time == now.life + 1) {
				pq.push(now);
			}

			// 죽음
			if (now.time == now.life * 2) {
				now.state = -1;
			}
			else {
				q.push(now);
			}

			// 현재 상태 저장
			grid[now.y][now.x] = now;
		}
		// 2. PQ 우선순위대로 적용
		while (!pq.empty()) {
			Stem now = pq.top();
			pq.pop();

			for (int d = 0; d < 4; d++) {
				int ny = now.y + dy[d];
				int nx = now.x + dx[d];

				if (grid[ny][nx].state != 0) continue;

				grid[ny][nx].state = 1;
				grid[ny][nx].life = now.life;
				grid[ny][nx].y = ny, grid[ny][nx].x = nx;
				grid[ny][nx].time = 0;

				q.push(grid[ny][nx]);
			}
		}

		// 3. 시간 지남
		cntTime++;
	}
	return q.size();
}


int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		// 초기화 하기
		memset(grid, 0, sizeof(grid));
		while (!q.empty()) q.pop();
		while (!pq.empty()) pq.pop();

		// 입력
		cin >> n >> m >> k;
		for (int y = 150; y < 150 + n; y++) {
			for (int x = 150; x < 150 + m; x++) {
				cin >> grid[y][x].life;
				if (grid[y][x].life) {
					grid[y][x].y = y, grid[y][x].x = x;
					grid[y][x].state = 1;
					grid[y][x].time = 0;
					q.push(grid[y][x]);
				}
			}
		}

		int result = func();

		cout << '#' << tc << ' ' << result << '\n';
	}
}