#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int m, a; // m(총 이동시간), a(BC의 개수)

// 0:정지, 1: 상, 2: 우, 3: 하, 4:좌
int dy[5] = { 0,-1,0,1,0 };
int dx[5] = { 0,0,1,0,-1 };

struct BC {
	int y, x; // 좌표
	int c, p; // 충전범위(c), 처리량(p)
};

// bfs로 찾아가기
// 최대 충전량이니까 경우의 수 확인
// BC 맨하탄거리로 확인하기

int moveOrd[2][101]; // 이동명령저장
BC charge[9]; // 충전정보

// 맨해튼 거리 계산 함수
int getDistance(int y1, int x1, int y2, int x2) {
	return abs(y1 - y2) + abs(x1 - x2);
}


int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {

		cin >> m >> a;
		for (int j = 0; j < 2; j++) {
			for (int i = 1; i <= m; i++) {
				cin >> moveOrd[j][i];
			}
		}
		for (int i = 1; i <= a; i++) {
			cin >> charge[i].x >> charge[i].y >> charge[i].c >> charge[i].p;
 		}

		// 초기 위치 설정
		int ay = 1, ax = 1;
		int by = 10, bx = 10;

		int total_sum = 0;

		// 0초(초기 위치)부터 M초까지 매초 시뮬레이션
		for (int t = 0; t <= m; t++) {
			// 1. 이동 (0초일 때는 이동하지 않음)
			if (t > 0) {
				ay += dy[moveOrd[0][t]];
				ax += dx[moveOrd[0][t]];
				by += dy[moveOrd[1][t]];
				bx += dx[moveOrd[1][t]];
			}

			int max_power = 0;

			// 2. 현재 위치에서 A와 B가 접속할 수 있는 모든 BC 조합 확인
			for (int i = 1; i <= a; i++) {		// A가 접속할 BC 번호
				for (int j = 1; j <= a; j++) {	// B가 접속할 BC 번호

					// 각 사용자가 해당 BC에 접속 가능한지 거리 체크
					bool a_can = getDistance(ay, ax, charge[i].y, charge[i].x) <= charge[i].c;
					bool b_can = getDistance(by, bx, charge[j].y, charge[j].x) <= charge[j].c;

					// 접속 가능 여부에 따른 충전량 설정
					int power_a = 0;
					if (a_can) power_a = charge[i].p;
					int power_b = 0;
					if (b_can) power_b = charge[j].p;

					int current_power = 0;
					// 둘 다 같은 BC에 접속 가능한 경우 (충전량을 반씩 나눔)
					if (i == j && a_can && b_can) current_power = charge[i].p; // 총합
					else current_power = power_a + power_b;
					 
					max_power = max(max_power, current_power);

				}
			}
			total_sum += max_power;
		}
		cout << '#' << tc << " " << total_sum << '\n';
	}
}