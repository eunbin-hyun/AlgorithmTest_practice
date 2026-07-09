#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>

using namespace std;

int n, L; // 지도 길이(n), 경사로의 길이(l)
int grid[22][22]; // map
int result;

// 0: 가로, 1: 세로
void func(int type) {
	for (int y = 1; y <= n; y++) {
		int cnt = 1;
		bool flag = false;
		for (int x = 1; x <= n; x++) {
			// 1. 가로 탐색
			if (type == 0) {
				// 1) 이전과 다를 때
				if (grid[y][x] != grid[y][x - 1]) {
					if (x == 1) continue;
					else {
						// 1-1) 이전보다 1 큰 경우
						if (grid[y][x] == grid[y][x - 1] + 1) {
							if (cnt >= L) cnt = 1;
							else break;
						}
						// 1-2) 이전보다 1 작은 경우
						else if (grid[y][x] == grid[y][x - 1] - 1) {
							if (x + L - 1 <= n) {
								for (int k = x + 1; k < x + L; k++) {
									if (grid[y][k] != grid[y][x])
										flag = true;
								}
							}
							else break;

							if (flag) break;
							else {
								x = x + L - 1;
								cnt = 0;
							}
						}
						// 1-3) 높이가 2이상 차이나는 경우
						else {
							break;
						}
					}
				}
				// 2) 이전과 같을 때
				else {
					cnt++;
				}
				// 3) 모두 탐색했을때
				if (x == n) result++;
			}
			// 2. 세로 탐색
			else {
				// 1) 이전과 다를 때
				if (grid[x][y] != grid[x-1][y]) {
					if (x == 1) continue;
					else {
						// 1-1) 이전보다 1 큰 경우
						if (grid[x][y] == grid[x-1][y] + 1) {
							if (cnt >= L) cnt = 1;
							else break;
						}
						// 1-2) 이전보다 1 작은 경우
						else if (grid[x][y] == grid[x-1][y] - 1) {
							if (x + L - 1 <= n) {
								for (int k = x + 1; k < x + L; k++) {
									if (grid[k][y] != grid[x][y])
										flag = true;
								}
							}
							else break;

							if (flag) break;
							else {
								x = x + L - 1;
								cnt = 0;
							}
						}
						// 1-3) 높이가 2이상 차이나는 경우
						else {
							break;
						}
					}
				}
				// 2) 이전과 같을 때
				else {
					cnt++;
				}
				// 3) 모두 탐색했을때
				if (x == n) result++;
			}
		}
	}
}


int main() {
	//freopen("sample_input.txt", "r", stdin);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		result = 0;
		cin >> n >> L;
		for (int y = 1; y <= n; y++)
			for (int x = 1; x <= n; x++)
				cin >> grid[y][x];

		func(0);
		func(1);

		cout << '#' << tc << ' ' << result << '\n';
	}
}