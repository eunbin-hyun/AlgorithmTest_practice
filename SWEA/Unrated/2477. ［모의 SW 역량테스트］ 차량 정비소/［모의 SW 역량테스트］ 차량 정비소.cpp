#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

// 접수 창구의 개수 n, 정비 창구의 개수 m, 차량 정비소를 방문한 고객의 수 k, 지갑을 두고 간 고객이 이용한 접수 창구번호 a와 정비 창구번호 b
int n, m, k, a, b;  

struct Customer {
	int arr_time; // 도착 시간
	int customer_num;
	int reception_num;
	int repair_num;
};

struct Room {
	int take_time; // 처리시간
	int finish_time; // 끝나는 남은시간
	int customer_num;
};

Customer customer[1001];
Room reception[10];
Room repair[10];

struct customer_cmp
{
	bool operator()(Customer a, Customer b) {
		if (a.arr_time == b.arr_time)
			return a.customer_num > b.customer_num;
		return a.arr_time > b.arr_time;
	}
};

struct recept_cmp {
	bool operator()(Room a, Room b) {
		if (a.finish_time == b.finish_time)
			return customer[a.customer_num].reception_num > customer[b.customer_num].reception_num;
		return a.finish_time > b.finish_time;
	}
};

int solve() {
	int cur_time = 0;
	int cnt = 0;

	priority_queue<Customer, vector<Customer>, customer_cmp> recept_pq;
	priority_queue<Room, vector<Room>, recept_cmp> repair_pq;

	while (cnt != k) {
		// 1. 접수
		// 1-1. 접수대기줄
		for (int id = 1; id <= k; id++) {
			// 현재시간보다 도착시간이 같은 경우
			if (cur_time == customer[id].arr_time) {
				recept_pq.push({ customer[id] }); // 자동으로 작은 고객번호로 들어감
			}
		}

		// 2. 정비
		// 2-1. 정비대기줄 ** 순서가 먼저 올라가야함..!
		for (int i = 1; i <= n; i++) {
			// 접수창구에 사람이 있는데 끝나는시간이 된경우 
			if (reception[i].customer_num && reception[i].finish_time == cur_time) {
				repair_pq.push({ reception[i] }); // 정비 줄서
				// 접수끝난거 처리
				reception[i].customer_num = 0;
			}
		}
		// 1-2. 접수중
		// 접수줄(pq)가 있는경우
		while (!recept_pq.empty()) {
			Customer now = recept_pq.top();
			bool flag = false;
			for (int i = 1; i <= n; i++) {
				// 접수창구가 비어있는경우 접수하기
				if (reception[i].customer_num == 0) {
					recept_pq.pop();
					reception[i].customer_num = now.customer_num;
					reception[i].finish_time = reception[i].take_time + cur_time;
					customer[now.customer_num].reception_num = i;
					break;
				}
				if (i == n) {
					flag = true;
					break;
				}
			}
			if (flag) break;
		}

		// 정비끝 -> 순서 올라감..!
		for (int i = 1; i <= m; i++) {
			// 정비창고에 사람이 있는데 끝날 시간이 된경우
			if (repair[i].customer_num && (repair[i].finish_time == cur_time)) {
				repair[i].customer_num = 0;
				cnt++;
			}
		}

		// 2-2. 정비 중
		// 정비 줄이 있는 경우
		while (!repair_pq.empty()) {
			Room now = repair_pq.top();
			bool flag = false;
			// 정비창구가 비어있는 경우
			for (int i = 1; i <= m; i++) {
				if (repair[i].customer_num == 0) {
					repair_pq.pop();
					repair[i].finish_time = repair[i].take_time + cur_time;
					repair[i].customer_num = now.customer_num;
					customer[now.customer_num].repair_num = i;
					break;
				}
				if (i == m) {
					flag = true;
					break;
				}
			}
			if (flag) break;
		}


		// 3. 시간 업데이트
		cur_time++;
	}

	// 4. 지갑잃어버린사람이랑 동일한지 확인하기
	int result = 0;
	for (int id = 1; id <= k; id++) {
		if (customer[id].reception_num == a && customer[id].repair_num == b)
			result += id;
	}

	if(result) return result;
	else return -1;
}

int main() {
	//freopen("sample_input.txt", "r", stdin);

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		cin >> n >> m >> k >> a >> b;
		memset(customer, 0, sizeof(customer));
		memset(reception, 0, sizeof(reception));
		memset(repair, 0, sizeof(repair));
		for (int i = 1; i <= n; i++) cin >> reception[i].take_time;
		for (int j = 1; j <= m; j++) cin >> repair[j].take_time;
		for (int id = 1; id <= k; id++) {
			customer[id].customer_num = id;
			cin >> customer[id].arr_time;
		}

		cout << '#' << tc << ' ' << solve() << '\n';
	}
}