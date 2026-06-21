#include <iostream>
#include <cstring>

using namespace std;

int n;
int grid[21][21];
int result;

// 방향: 오른아래, 왼아래, 왼위, 오른위
int dy[4] = { 1,1,-1,-1 };
int dx[4] = { 1,-1, -1, 1 };


void simulation(int cy, int cx, int len1, int len2) {
	int visited[101] = { 0 };
	bool is_valid = true;

	// 각 방향(0,1,2,3)마다 이동해야 하는 횟수를 배열로 매핑
	int lens[4] = { len1, len2, len1, len2 };

	for (int d = 0; d < 4; d++) {
		for (int step = 1; step <= lens[d]; step++) {
			// 정해진 방향으로 한칸 전진
			cy += dy[d];
			cx += dx[d];

			// 1. 격자 범위 체크 
			if (cy < 0 || cy >= n || cx < 0 || cx >= n) {
				is_valid = false;
				break;
			}

			// 2. 디저트 중복 체크
			int dessert_type = grid[cy][cx];
			if (visited[dessert_type]) {
				is_valid = false;
				break;
			}

			// 방문 표시
			visited[dessert_type] = 1;
		}
		if (!is_valid)break;
	}
	if (is_valid) {
		int total_desserts = (len1 + len2) * 2;
		if (total_desserts > result) {
			result = total_desserts;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		result = -1;
		cin >> n;
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				cin >> grid[y][x];
			}
		}

		// 시작 좌표 (y,x) 설정
		for (int y = 0; y < n - 2; y++) {
			for (int x = 1; x < n - 1; x++) {

				// 우하단 방향길이 (len1), 좌하단 방향길이 (len2)
				for (int len1 = 1; len1 < n; len1++) {
					for (int len2 = 1; len2 < n; len2++) {
						simulation(y, x, len1, len2);
					}
				}
			}
		}
		cout << '#' << tc << ' ' << result << '\n';
	}
}