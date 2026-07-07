// 푸는중
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int wheel[6][9]; // 4개 바퀴, 8개 날 (N극 0, S극 1)
int k; // 자석 회전 횟수
int order[21][2]; // 자석번호, 회전방향 (시계 1, 반시계 -1)
int visited[6]; // 회전여부

// 자석 회전
void rotate() {
	for (int i = 0; i < k; i++) {
		memset(visited, 0, sizeof(visited));
		int mag_num = order[i][0]; // 자석 번호
		int spin_dir = order[i][1]; // 회전 방향
		queue<int> q;
		q.push(mag_num);
		visited[mag_num] = spin_dir;

		// 한번 회전
		while (!q.empty())
		{
			int now_num = q.front();
			int now_dir = visited[now_num];
			q.pop();

			// 왼쪽 날 확인 (3 <- 7)
			if (now_num != 1) {
				int left_num = now_num - 1;
				if (visited[left_num] == 0) { // 이미 회전 안한경우
					// 자석 번호가 다른경우 반대방향회전
					if (wheel[left_num][3] != wheel[now_num][7]) {
						visited[left_num] = -now_dir;
						q.push(left_num);
					}
				}
			}
			// 오른쪽 날 확인 (3 -> 7)
			if (now_num != 4) {
				int right_num = now_num + 1;
				if (visited[right_num] == 0) { // 이미 회전 안한경우
					// 자석 번호가 다른경우 반대방향회전
					if (wheel[right_num][7] != wheel[now_num][3]) {
						visited[right_num] = -now_dir;
						q.push(right_num);
					}
				}
			}
		}

		// 회전 업데이트
		for (int i = 1; i <= 4; i++) {
			if (visited[i] == 0) continue;
			int temp[6][9];
			memcpy(temp, wheel, sizeof(wheel));
			// 시계방향회전
			if (visited[i] == 1) {
				int tmp = wheel[i][8];
				for (int j = 1; j < 8; j++) {
					temp[i][j + 1] = wheel[i][j];
				}
				temp[i][1] = tmp;
				memcpy(wheel, temp, sizeof(temp));
			}
			else {	// 반시계 회전
				int tmp = wheel[i][1];
				for (int j = 8; j > 1; j--) {
					temp[i][j - 1] = wheel[i][j];
				}
				temp[i][8] = tmp;
				memcpy(wheel, temp, sizeof(temp));
			}
		}

	}
}

// 계산 결과
int calcul() {
	int result = 0;
	for (int i = 1; i <= 4; i++) {
		int tmp = 0;
		if (wheel[i][1]==1) {
			if (i == 1) tmp = 1;
			else if (i == 2) tmp = 2;
			else if (i == 3) tmp = 4;
			else if (i == 4) tmp = 8;
		}
		result += tmp;
	}
	return result;
}

int main() {
	//freopen("sample_input.txt", "r", stdin);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		// 입력
		cin >> k;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 8; j++) {
				cin >> wheel[i][j];
			}
		}
		for (int i = 0; i < k; i++) {
			cin >> order[i][0] >> order[i][1];
		}

		rotate();
		cout << '#' << tc << ' ' << calcul() << '\n';
	}

}