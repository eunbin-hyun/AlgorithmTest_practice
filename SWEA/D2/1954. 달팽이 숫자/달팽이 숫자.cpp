#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	// 방향 (오, 아, 왼, 위)
	int dy[4] = {0, 1, 0, -1};
	int dx[4] = {1, 0, -1, 0};
	for (int test =1; test <=t; test++)
	{
		int n;
		cin >> n;
		int x =0;
		int y =0;
		// 배열 n말고 최대수로 선언하기..! 
		int arr[11][11] = {0};
		arr[0][0] = 1;
		int d =0;
		int num =2;
		while (num <= n*n)
		{
			int ny = y + dy[d%4];
			int nx = x + dx[d%4];
			// 배열 범위  벗어나지 않는다면 
			if (nx >= 0 && nx <n && ny >=0 && ny <n)
			{
				// 이미 방문하지 않았다면 방문하기
				 if (arr[ny][nx] == 0)
				 {
				 	arr[ny][nx] = num;
				 	num++;
				 	y = ny;
				 	x = nx;
				 }
				 else
				 {
				 	d++;
				 }
			}
			else
			{
				d++;
			}
		}
		// 출력하기
		cout << "#" << test << "\n";
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<n; j++)
			{
				cout << arr[i][j] << " ";
			}
			cout << "\n";
		} 
	}
}