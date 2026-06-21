#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m, c;
int grid[11][11];
int result;


int getHoney(int y, int x, int depth, int sum, int profit) {

	// 합이 c를 넘으면 가지치기
	if (sum > c) return 0;
	// m개의 칸(depth)을 모두 확인했으면 수익 리턴
	if (depth == m) return profit;
	
	// 현재 벌통을 선택하는 경우의 재귀호출
	int pick = getHoney(y, x + 1, depth + 1, sum + grid[y][x], profit + grid[y][x] * grid[y][x]);
	// 현재 벌통을 선택하지 않는 경우의 재귀호출
	int skip = getHoney(y, x + 1, depth +1, sum, profit);

	// 둘 중 더 큰 수익을 리턴
	return max(pick, skip);
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		result = 0;

		cin >> n >> m >> c;

		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				cin >> grid[y][x];
			}
		}

		// 일꾼이 선택한 벌통
		for (int sy = 0; sy < n; sy++) {
			for (int sx = 0; sx <= n-m; sx++) {
				for (int sy2 = sy; sy2 < n; sy2++) {
					for (int sx2 = 0; sx2 <= n-m; sx2++) {
						if (sy2 == sy && sx2 < sx + m) continue;
						int profit1 = getHoney(sy, sx, 0, 0, 0);
						int profit2 = getHoney(sy2, sx2, 0, 0, 0);
						result = max(result, profit1 + profit2);
					}
				}
			}
		}
		cout << '#' << tc << ' ' << result << '\n';
	}
}