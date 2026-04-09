#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

struct Point {
	int y, x;
};

int N, M;	// 맵크기(N), 치킨집 최대 개수(M)
int map[51][51]; // 집(1), 치킨집(2) 저장맵
vector<Point> chickens; // 모든 치킨집
vector<Point> homes; // 모든 집
int chicken_idx[20]; // 방문할 치킨집 인덱스(dfs 조합)
int min_result = 21e8;

// 최단거리 계산
int shortDist(Point home, Point ck) {
	int dist = abs(home.y - ck.y) + abs(home.x - ck.x);
	return dist;
}

// 최단거리 합
int sumDist() {
	int sum_dist = 0;

	for (int j = 0; j < homes.size(); j++) {
		int tmp_dist = 0;
		int min_dist = 21e8;
		Point home = homes[j]; // 최단거리 계산할 집
		for (int i = 0; i < chickens.size(); i++) {
			if (chicken_idx[i]) {	// 방문할 치킨집
				Point ck = chickens[i];
				tmp_dist = shortDist(home, ck);
				min_dist = min(min_dist, tmp_dist);
			}
		}
		sum_dist += min_dist;
	}
	return sum_dist;
}

// 치킨집 조합
void dfs(int lev, int idx) {
	// 치킨집 최대 M까지 다 선택함
	if (lev == M) {
		// 각 집에서 가장 가까운거리(맨하탄) 계산
		int temp = sumDist();
		min_result = min(min_result, temp);
		return;
	}


	// 조합 (중복 x, 순서x)
	for (int i = idx; i < chickens.size(); i++) {
		if (chicken_idx[i] == 0) {
			chicken_idx[i] = 1;
			dfs(lev + 1, i+1);
			chicken_idx[i] = 0;
		}
	}
}

int main(){
	// 시간 단축
	ios::sync_with_stdio(0);
	cin.tie(0);

	// 입력
	cin >> N >> M;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			cin >> map[y][x];
			if (map[y][x] == 2) {
				chickens.push_back({ y,x });
			}
			else if (map[y][x] == 1) {
				homes.push_back({ y,x });
			}
		}
	}
	
	dfs(0,0);
	cout << min_result;
}