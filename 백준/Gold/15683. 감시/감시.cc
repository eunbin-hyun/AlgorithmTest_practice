#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// cctv의 y,x, type(몇번째 cctv)
struct Point {
	int y, x, type;
};

int N, M;  // 맵 크기 (N x M)
int map[10][10];  // 맵

// 왼, 위, 오, 아 (시계방향)
int dy[4] = { 0, -1, 0, 1 };
int dx[4] = { -1, 0, 1, 0 };

vector<Point> v; // cctv 좌표와 타입이 들어있는 vector
int minResult = 21e8; // 사각지대 최소 크기

// 특정 방향으로 감시 진행 (벽을 만나기 전까지)
void watch(int y, int x, int dir, int tmpMap[10][10]) {
	int ny = y, nx = x;

	while (true) {
		ny += dy[dir], nx += dx[dir];

		// 범위를 벗어나거나 벽(6)을 만나면 중단
		if (ny < 0 || nx < 0 || ny >= N || nx >= M || tmpMap[ny][nx] == 6)
			break;
		// CCTV가 있는 칸은 통과하지만, 빈칸(0)은 감시중(-1)으로 표시
		if (tmpMap[ny][nx] == 0)tmpMap[ny][nx] = -1;
	}
}

void solve(int cnt, int currentMap[10][10]) {
	// 종료조건 
	if (cnt == v.size()) {
		int zeroCount = 0;
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < M; x++) {
				if (currentMap[y][x] == 0) zeroCount++;
			}
		}
		minResult = min(minResult, zeroCount);
		return;
	}

	int y = v[cnt].y;
	int x = v[cnt].x;
	int type = v[cnt].type;

	// 현재 cctv가 가질 수 있는 방향의 경우의 수 
	// (1, 3, 4번은 4방향, 2번은 2방향, 5번은 1방향)
	for (int dir = 0; dir < 4; dir++) {
		int nextMap[10][10];
		// 1. 현재 맵 상태 복사
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < M; x++) 
				nextMap[y][x] = currentMap[y][x];
		}

		// 2. CCTV 종류별 감시 방향 설정
		if (type == 1) {
			watch(y, x, dir, nextMap);
		}
		else if (type == 2) {
			if (dir >= 2) break;	// 2번은 상하/좌우 두가지만 확인하면 됨
			watch(y, x, dir, nextMap);
			watch(y, x, dir + 2, nextMap);
		}
		else if (type == 3) {
			watch(y, x, dir, nextMap);
			watch(y, x, (dir + 1) % 4, nextMap);
		}
		else if (type == 4) {
			watch(y, x, dir, nextMap);
			watch(y, x, (dir + 1) % 4, nextMap);
			watch(y, x, (dir + 2) % 4, nextMap);
		}
		else if (type == 5) {
			if (dir >= 1)break;	// 5번은 전방향이라 한번만 하면 끝
			watch(y, x, 0, nextMap);
			watch(y, x, 1, nextMap);
			watch(y, x, 2, nextMap);
			watch(y, x, 3, nextMap);
		}

		// 3. 다음 CCTV로 진행
		solve(cnt + 1, nextMap);
	}
	
}

int main() {
	cin >> N >> M;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M; x++) {
			cin >> map[y][x];
			if (map[y][x] && map[y][x] != 6) {
				v.push_back({ y,x, map[y][x]});
			}
		}
	}
	
	solve(0, map);
	cout << minResult;
}