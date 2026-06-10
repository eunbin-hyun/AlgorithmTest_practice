#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int n, m, r, c, l;
int map[51][51];
int visited[51][51];

// 상(0), 하(1), 좌(2), 우(3)
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

// 각 파이프(0~7)가 상하좌우(0~3) 방향으로 뚫려있는지 여부를 배열로 정의
int pipe[8][4] = {
    {0, 0, 0, 0}, // 0: 빈 공간
    {1, 1, 1, 1}, // 1: 상하좌우
    {1, 1, 0, 0}, // 2: 상하
    {0, 0, 1, 1}, // 3: 좌우
    {1, 0, 0, 1}, // 4: 상우
    {0, 1, 0, 1}, // 5: 하우
    {0, 1, 1, 0}, // 6: 하좌
    {1, 0, 1, 0}  // 7: 상좌
};

struct Point {
    int y, x;
};

int bfs(int sy, int sx, int endtime) {
    queue<Point> q;
    q.push({sy, sx});
    visited[sy][sx] = 1;
    int cnt = 1;

    while (!q.empty()) {
        Point now = q.front();
        q.pop();

        // 주어진 시간이 다 되면 해당 지점에서는 더 이상 퍼져나가지 않음
        if (visited[now.y][now.x] == endtime) continue;

        int cur_pipe = map[now.y][now.x];

        for (int d = 0; d < 4; d++) {
            // 현재 파이프가 d 방향으로 뚫려있지 않으면 패스
            if (!pipe[cur_pipe][d]) continue;

            int ny = now.y + dy[d];
            int nx = now.x + dx[d];

            // 맵을 벗어나거나, 이미 방문했거나, 다음 칸이 빈 공간이면 패스
            if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
            if (visited[ny][nx] || map[ny][nx] == 0) continue;

            int nxt_pipe = map[ny][nx];
            
            // 반대 방향 인덱스 구하기 (0<->1, 2<->3)
            // XOR (^) 이용 : 두 비트가 다르면 1, 같으면 0
            int rev_d = d ^ 1; 

            // 다음 파이프가 현재 이동하는 방향의 '반대 방향'으로 뚫려있다면 연결된 것
            if (pipe[nxt_pipe][rev_d]) {
                visited[ny][nx] = visited[now.y][now.x] + 1;
                q.push({ny, nx});
                cnt++;
            }
        }
    }
    return cnt;
}

int main() {
    // 입출력 속도 향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cin >> n >> m >> r >> c >> l;
        memset(visited, 0, sizeof(visited));
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                cin >> map[y][x];
            }
        }
        cout << "#" << tc << " " << bfs(r, c, l) << '\n';
    }
    return 0;
}