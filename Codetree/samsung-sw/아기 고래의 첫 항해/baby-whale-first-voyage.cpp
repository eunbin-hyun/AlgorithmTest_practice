#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, r, c, d; // n격자, r,c,d: 아기고래 위치

// dir 방향: 
// 이동좌표: 서(0), 남(1), 동(2), 북(3) - 시계방향
int dy[4] = { 0, 1, 0, -1 }, dx[5] = { -1, 0, 1, 0 };

// 인접 탐험 방향에 따른 이동좌표
int offset[4] = { 0,1,3,2 };

// 바다 0, 암초 -1
int grid[51][51] = { 0 };
// 방문 안한바다 0, 암초 -1, 방문한 바다 숫자
int visited[51][51] = { 0 };

struct Point {
    int y, x, d;
};

// 1. 인접 탐험
bool adj(int sy, int sx, int sd, int visit) {
    for (int i = 0; i < 4; i++) {
        int cd = (sd+offset[i]) % 4;
        int cy = sy+ dy[cd], cx = sx+ dx[cd];

        if (cy <= 0 || cx <= 0 || cy > n || cx > n) continue;

        if (visited[cy][cx] == 0) {
            visited[cy][cx] = visited[sy][sx] + 1;
            r = cy, c = cx, d = cd;
            return true;
        }
    }
    return false;
}

// 2. 가장 가까운 바다로 이동
void moveSea(int sy, int sx, int sd, int visit) {
    int tmpvisited[51][51];
    memcpy(tmpvisited, grid, sizeof(grid));

    // 1) 후보찾기 
    int canY = -1, canX = -1, canD = 0;
    int distance = 0;
    queue<Point> q;
    q.push({ sy,sx,sd });
    tmpvisited[sy][sx] = 1;
    bool is_val = false;

    while (!q.empty()) {
        Point now = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nd = i;
            int ny = now.y + dy[i];
            int nx = now.x + dx[i];

            if (ny <= 0 || nx <= 0 || ny > n || nx > n) continue;

            // 이동 가능한 경우
            if (tmpvisited[ny][nx] == 0) {
                q.push({ ny,nx,nd });
                tmpvisited[ny][nx] = tmpvisited[now.y][now.x] + 1;
            }
            
            // 이동 바다 후보인경우
            if (visited[ny][nx] == 0) {
                if (distance == 0) {
                    canD = nd, canY = ny, canX = nx;
                    distance = tmpvisited[canY][canX];
                    continue;
                }
                if (distance < tmpvisited[ny][nx]) {
                    is_val = true;
                    break;
                }

                if (canY >= ny) {
                    if (canY > ny) {
                        canD = nd, canY = ny, canX = nx;
                        distance = tmpvisited[canY][canX];
                        continue;
                    }
                    if (canX > nx) {
                        canD = nd, canY = ny, canX = nx;
                        distance = tmpvisited[canY][canX];
                    }
                }
            }

        }
        if (is_val) break;
    }

    // 2) 이동
    r = canY, c = canX, d = canD;
    visited[r][c] = visited[sy][sx] + 1;
}

int main() {
    cin >> n >> r >> c >> d;
    int grow = 0;
    for (int y = 1; y <=n; y++) {
        for (int x = 1; x <=n; x++) {
            cin >> grid[y][x];
            if (grid[y][x]) {
                visited[y][x] = -1;
                grid[y][x] = -1;
                grow++;
            }
        }
    }
    if (d == 1)d = 3;
    else if (d == 2) d = 1;
    else if (d == 3) d = 0;
    else d = 2;

    visited[r][c] = 1;
    cout << r << ' ' << c << '\n';
    int cnt = 1;
    while (cnt < n * n - grow) {
        if (adj(r,c,d,visited[r][c]) != true) {
            moveSea(r, c, d, visited[r][c]);
        }
        cout << r << ' ' << c << '\n';
        cnt++;
    }
}