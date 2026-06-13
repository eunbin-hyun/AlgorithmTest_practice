#include <iostream>
#include <set>
#include <string>
#include <algorithm>

using namespace std;


int n, k; // n: 주어지는 숫자 개수, k: 회전 후 k번째로 큰 숫자

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> n >> k;
		string num_16th;
		cin >> num_16th;

		// 회전해야되는 횟수세기
		int rotate = n / 4;

		// 회전할 만큼 회전해서 set에 넣기 (내림차순 정렬)
		set<int, greater<int>> nums;
		for (int rn = 0; rn < rotate; rn++) { // 회전횟수
			// 1. 현재 문자열 상태에서 4개의 변 추출하기
			for (int i = 0; i < 4; i++) { 
				// i * rotate 인덱스부터 rotate 길이만큼 자르기
				string sub = num_16th.substr(i * rotate, rotate);

				// 16진수 문자열을 10진수 정수로 변환하여 set에 삽입
				nums.insert(stoi(sub, nullptr, 16));
			}
			
			// 2. 시계방향으로 한 칸 회전 (맨 뒤 문자를 맨 앞으로 이동)
			num_16th = num_16th.back() + num_16th.substr(0, n - 1);
		}

		// K번째 큰 값 출력하기
		// set의 시작점(가장 큰 값)부터 K-1번 뒤로 이동
		auto it = nums.begin();
		for (int i = 0; i < k - 1; i++) it++;
		cout << '#' << tc << ' ' << *it << "\n";
	}
}