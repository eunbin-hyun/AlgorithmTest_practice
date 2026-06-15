#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>

using namespace std;

int d, w, k;
int grid[14][21];
int copyGrid[14][21];
int endlev;
int result = 21e8;

bool bfs() {
	for (int x = 0; x < w; x++) {
		bool check = false;
		int connect = 1;
		for (int y = 1; y < d; y++) {
			if (copyGrid[y - 1][x] == copyGrid[y][x]) connect++;
			else {
				if (connect >= k) { // 중간경우 확인
					check = true;
					break;
				}
				connect = 1;
			}
		}
		if (connect >= k) check = true; // 마직막 경우도 확인!
		if (!check) return false;
	}
	return true;
}

// 조합(순서X, 중복 X)
void dfs(int lev, int st_idx) {
	// 종료조건
	if (lev == endlev) {
		if (bfs()) result = lev;
		return; // end지점 오면 무조건 리턴 !!
	}


	for (int y = st_idx; y < d; y++) {

		for (int x = 0; x < w; x++) copyGrid[y][x] = 0; // A투입
		dfs(lev + 1, y+1);
		for (int x = 0; x < w; x++) copyGrid[y][x] = 1; // B투입
		dfs(lev + 1, y+1);

		for (int x = 0; x < w; x++) copyGrid[y][x] = grid[y][x];

	}
}

int main() {
	//freopen("sample_input.txt", "r", stdin);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {

		// 입력
		cin >> d >> w >> k;
		for (int y = 0; y < d; y++)
			for (int x = 0; x < w; x++)
				cin >> grid[y][x]; 

		// 초기화
		memcpy(copyGrid, grid, sizeof(grid)); // grid 입력받고 복사하기
		result = 21e8;		// testcase마다 result 초기화

		// 함수
		for (int lev = 0; lev <= k; lev++) {
			endlev = lev;
			dfs(0, 0);
			if (result != 21e8) break;
		}
		cout << '#' << tc << ' ' << result << '\n';
	}
}