#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
int map[21][21];
int visited[21][21];
int desert[101];

int sy, sx;
int result;

// 방향: 오른쪽위, 오른쪽아래, 왼쪽아래, 왼쪽위
int dy[4] = { -1,1,1,-1 };
int dx[4] = { 1,1,-1,-1 };

void dfs(int cy, int cx, int cd, int cnt) {
	// 다음위치 계산 (직진, 회전)
	for (int turn = 0; turn <= 1; turn++) {
		int nd = cd + turn;

		// 방향은 0- > 1 -> 2 -> 3 까지만 허용
		if (nd >= 4)continue; // 재귀이기에 return 사용하면 하는중간에 끊킴

		int ny = cy + dy[nd];
		int nx = cx + dx[nd];

		// 시작점으로 돌아오는 경우
		if (sy == ny && sx == nx) {
			if (cnt >= 4 && nd == 3) {
				result = max(cnt, result);
			}
			continue; // 아래부분 무시
		}

		// 막힌경우 continue로 그 경우에 대해서 무시하고 계속 진행 !!
		if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
		if (visited[ny][nx]) continue;
		if (desert[map[ny][nx]]) continue;

		visited[ny][nx] = 1;
		desert[map[ny][nx]] = 1;

		dfs(ny, nx, nd, cnt + 1);

		visited[ny][nx] = 0;
		desert[map[ny][nx]] = 0;
	}
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		// 초기화
		memset(visited,0, sizeof(visited));
		memset(desert, 0, sizeof(desert));
		result = 0;
		// 입력
		cin >> n;
		for (int y = 0; y < n; y++)
			for (int x = 0; x < n; x++)
				cin >> map[y][x];

		// 함수(시작점 전달)
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				for (int d = 0; d < 4; d++) { // 방향 시작점
					sy = y, sx = x;
					visited[y][x] = 1;
					desert[map[y][x]] = 1;
					dfs(y, x, d, 1); // cnt =1 이다 (시작지점 세기)!!
					visited[y][x] = 0;
					desert[map[y][x]] = 0;
				}
			}
		}
		if (result == 0) cout << '#' << tc << ' ' << -1 << '\n';
		else cout << '#' << tc << ' ' << result << '\n';
	}
}