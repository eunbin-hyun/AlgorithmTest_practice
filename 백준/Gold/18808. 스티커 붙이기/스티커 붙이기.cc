#include <iostream>
#include <algorithm>	// swap

using namespace std;

int N, M, K; // 노트북의 가로(N), 세로(M), 스티커 개수(K)
int R, C; // 스티커가 붙여진 모눈종이의 행(R), 열(C) 

int notebook[41][41]; // 노트북 상태
int sticker[11][11]; // 스티커 붙여진 모눈종이


// 노트북의 (y,x) 위치에 스티커를 붙일 수 있는지 확인하는 함수
bool canStick(int sy, int sx) {
	for (int y = 0; y < R; y++) {
		for (int x = 0; x < C; x++) {
			if (sticker[y][x] == 1 && notebook[y + sy][x + sx] == 1)
				return false;
		}
	}
	return true;
}

// 실제로 노트북에 스티커를 붙이는 함수
void attach(int sy, int sx) {
	for (int y = 0; y < R; y++) {
		for (int x = 0; x < C; x++) {
			if (sticker[y][x] == 1)
				notebook[y + sy][x + sx] = 1;
		}
	}
}

// 현재 스티커를 90도 회전시키는 함수
void rotate() {
	int temp[11][11];
	for (int y = 0; y < R; y++) {
		for (int x = 0; x < C; x++) {
			temp[x][R - 1 - y] = sticker[y][x];
		}
	}
	// 행과 열의 크기를 바꾸고 다시 sticker 배열로 복사
	swap(R, C);
	for (int y = 0; y < R; y++) {
		for (int x = 0; x < C; x++) {
			sticker[y][x] = temp[y][x];
		}
	}
}

int main() {
	// 빠른 입출력
	ios::sync_with_stdio(0);
	cin.tie(0);

	// 입력
	cin >> N >> M >> K;
	for (int t = 0; t < K; t++) {
		cin >> R >> C;
		for (int y = 0; y < R; y++) {
			for (int x = 0; x < C; x++) {
				cin >> sticker[y][x];
			}
		}
		
		// 메인문
		bool is_attached = false;
		for (int rot = 0; rot < 4; rot++) {	// 1순위: 방향 (0, 90. 180, 270)
			for (int y = 0; y <= N - R; y++) {  // 2순위: 위쪽부터(행)
				for (int x = 0; x <= M - C; x++) {  // 3순위: 왼쪽부터(열)

					// y,x는 스티커의 시작점
					if (canStick(y, x)) {	// 붙일 수 있는지 확인
						attach(y, x);		// 실제로 붙이기
						is_attached = true;
						break;		// x 루프 탈출
					}
				}
				if (is_attached) break;		// y 루프 탈출
			}
			if (is_attached) break;		// rot 루프 탈출

			rotate();	// 이 방향에서 못 붙였다면 90도 회전
		}
	}

	// 결과 계산: 붙은 칸(1)의 개수 세기
	int ans = 0;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M; x++) {
			ans += notebook[y][x];
		}
	}

	cout << ans << '\n';
}