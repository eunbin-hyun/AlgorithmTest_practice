#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	//freopen("input.txt", "r", stdin);
	for (int tc = 1; tc <= 10; tc++) {
		int n;
		cin >> n;

		vector<int> v(n);
		for (int i = 0;i < n; i++) {
			cin >> v[i];
		}

		int m;
		cin >> m;
		for (int i = 0; i < m; i++) {
			char cmd;
			cin >> cmd;

			if (cmd == 'I') {
				int x, y;
				cin >> x >> y;

				vector<int> temp(y);
				for (int j = 0; j < y; j++) {
					cin >> temp[j];
				}
				v.insert(v.begin() + x, temp.begin(), temp.end());
			}
			else if (cmd == 'D') {
				int x, y;
				cin >> x >> y;

				v.erase(v.begin() + x, v.begin() + x + y);
			}
			else if (cmd == 'A') {
				int y;
				cin >> y;

				for (int j = 0; j < y; j++) {
					int num;
					cin >> num;
					v.push_back(num);
				}

			}
		}
		cout << '#' << tc << " ";
		for (int i = 0; i < 10; i++) cout << v[i] << " ";
		cout << '\n';
	}
}
