#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int n, m; // n: grid크기, m: 비용
vector<pair<int, int>> houses;

int main() {
	//freopen("sample_input.txt", "r", stdin);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> n >> m;
		houses.clear();
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				int v;
				cin >> v;
				if (v==1) houses.push_back({ y,x });
			}
		}

		int result = 0;
		// 중심점이 모든 구역 한번씩 순회
		for (int cy = 0; cy < n; cy++) {
			for (int cx = 0; cx < n; cx++) {

				// k가 1~N+1까지 운영영역일 때를 순회
				for (int k = 1; k <= n + 1; k++) {
					int cnt = 0; // 집개수 cnt

					// 맨하탄 거리(k)안에 집이 있는지
					for (auto house : houses) {
						int dist = abs(cy - house.first) + abs(cx - house.second);

						if (dist < k) cnt++;
					}

					// cost: 운영비용
					int cost = k * k + (k - 1) * (k - 1);

					// 보안회사가 손해가 안나는 경우
					if (cnt * m >= cost)
						result = max(cnt, result);
				}
			}
		}
		cout << '#' << tc << ' ' << result << '\n';
	}
}