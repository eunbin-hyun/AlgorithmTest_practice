#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

// 한 변의 길이가 n인 2차원 평면
// 한 변의 길이가 m인 시간의 벽
// 시간 이상 현상 총 f개
int n, m, f;

// 1. 미지의 공간의 평면도(n*n)
// 빈 공간(0), 장애물(1), 시간의 벽(3), 탈출구(4)
int grid[21][21];

// 2. 시간의 벽의 단면도
// 0: 동, 1: 서, 2: 남, 3: 북, 4: 윗면
int wall[5][11][11];

// 시간의 벽 BFS 최단거리
int dist[5][11][11];

// 평면 BFS 도착 시각
int groundDist[21][21];

// 시간 이상 현상
struct Time {
    int r, c; // 좌표 r, c
    int d, v; // d 방향으로 v의 배수 턴마다 확산
};
Time timeStrange[11];

struct Point {
    int y, x;
};

struct WallPoint {
    int face, y, x;
};

Point start;                       // 윗면의 타임머신 시작 위치
Point escapePos;                   // 평면의 최종 탈출구(4)
Point wallPos = { -1, -1 };          // 평면에서 3 영역의 왼쪽 위 좌표
Point exitPos;                     // 시간의 벽에서 내려온 평면 위치
int exitFace;                      // 출구와 맞닿은 옆면
int exitX;                         // 해당 옆면 아래쪽의 x 좌표

const int INF = 1e9;
int dangerTime[21][21];

// 동 서 남 북
int dy[4] = { 0, 0, 1, -1 };
int dx[4] = { 1, -1, 0, 0 };

// 1. 입력 받기
void input() {
    cin >> n >> m >> f;

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cin >> grid[y][x];

            if (grid[y][x] == 4)
                escapePos = { y, x };

            if (grid[y][x] == 3 && wallPos.y == -1)
                wallPos = { y, x };
        }
    }

    for (int face = 0; face < 5; face++) {
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < m; x++) {
                cin >> wall[face][y][x];

                if (wall[face][y][x] == 2)
                    start = { y, x };
            }
        }
    }

    for (int i = 0; i < f; i++) {
        cin >> timeStrange[i].r >> timeStrange[i].c
            >> timeStrange[i].d >> timeStrange[i].v;
    }
}

// 2. 평면에서 시간의 벽 출구 찾기
void findExit() {
    int sy = wallPos.y;
    int sx = wallPos.x;

    // 북쪽
    for (int x = sx; x < sx + m; x++) {
        int y = sy - 1;

        if (y >= 0 && grid[y][x] == 0) {
            exitPos = { y, x };
            exitFace = 3;
            exitX = m - 1 - (x - sx);
            return;
        }
    }

    // 남쪽
    for (int x = sx; x < sx + m; x++) {
        int y = sy + m;

        if (y < n && grid[y][x] == 0) {
            exitPos = { y, x };
            exitFace = 2;
            exitX = x - sx;
            return;
        }
    }

    // 동쪽
    for (int y = sy; y < sy + m; y++) {
        int x = sx + m;

        if (x < n && grid[y][x] == 0) {
            exitPos = { y, x };
            exitFace = 0;
            exitX = m - 1 - (y - sy);
            return;
        }
    }

    // 서쪽
    for (int y = sy; y < sy + m; y++) {
        int x = sx - 1;

        if (x >= 0 && grid[y][x] == 0) {
            exitPos = { y, x };
            exitFace = 1;
            exitX = y - sy;
            return;
        }
    }
}

// 3. 각 평면 칸이 위험해지는 최초 시각 계산
void calcDangerTime() {
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            dangerTime[y][x] = INF;
        }
    }

    for (int i = 0; i < f; i++) {
        Time t = timeStrange[i];

        int y = t.r;
        int x = t.c;
        int turn = 0;

        while (true) {
            dangerTime[y][x] = min(dangerTime[y][x], turn);

            int ny = y + dy[t.d];
            int nx = x + dx[t.d];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n)
                break;

            if (grid[ny][nx] != 0)
                break;

            turn += t.v;
            y = ny;
            x = nx;
        }
    }
}

// 면의 경계를 고려한 다음 칸 반환
WallPoint getNext(WallPoint cur, int d) {
    int face = cur.face;
    int y = cur.y;
    int x = cur.x;

    int ny = y + dy[d];
    int nx = x + dx[d];

    // 같은 면에서 이동
    if (0 <= ny && ny < m && 0 <= nx && nx < m)
        return { face, ny, nx };

    // 윗면에서 옆면으로 이동
    if (face == 4) {
        if (d == 0) return { 0, 0, m - 1 - y };
        if (d == 1) return { 1, 0, y };
        if (d == 2) return { 2, 0, x };
        if (d == 3) return { 3, 0, m - 1 - x };
    }

    // 옆면 위쪽에서 윗면으로 이동
    if (ny < 0) {
        if (face == 0) return { 4, m - 1 - x, m - 1 };
        if (face == 1) return { 4, x, 0 };
        if (face == 2) return { 4, m - 1, x };
        if (face == 3) return { 4, 0, m - 1 - x };
    }

    // 옆면 왼쪽 경계로 이동
    if (nx < 0) {
        if (face == 0) return { 2, y, m - 1 };
        if (face == 1) return { 3, y, m - 1 };
        if (face == 2) return { 1, y, m - 1 };
        if (face == 3) return { 0, y, m - 1 };
    }

    // 옆면 오른쪽 경계로 이동
    if (nx >= m) {
        if (face == 0) return { 3, y, 0 };
        if (face == 1) return { 2, y, 0 };
        if (face == 2) return { 0, y, 0 };
        if (face == 3) return { 1, y, 0 };
    }

    // 옆면 아래쪽은 출구가 아니면 이동 불가
    return { -1, -1, -1 };
}

// 4. 시간의 벽에서 평면 입구까지 최단 이동 시각
int wallBFS() {
    queue<WallPoint> q;
    memset(dist, -1, sizeof(dist));

    q.push({ 4, start.y, start.x });
    dist[4][start.y][start.x] = 0;

    while (!q.empty()) {
        WallPoint cur = q.front();
        q.pop();

        int face = cur.face;
        int y = cur.y;
        int x = cur.x;

        // 옆면 아래쪽에서 평면으로 내려가는 이동까지 1턴
        if (face == exitFace && y == m - 1 && x == exitX)
            return dist[face][y][x] + 1;

        for (int d = 0; d < 4; d++) {
            WallPoint next = getNext(cur, d);

            if (next.face == -1)
                continue;

            if (wall[next.face][next.y][next.x] == 1)
                continue;

            if (dist[next.face][next.y][next.x] != -1)
                continue;

            dist[next.face][next.y][next.x] =
                dist[face][y][x] + 1;
            q.push(next);
        }
    }

    return -1;
}

// 5. 평면 입구에서 최종 탈출구까지 BFS
int groundBFS(int startTime) {
    if (startTime >= dangerTime[exitPos.y][exitPos.x])
        return -1;

    queue<Point> q;
    memset(groundDist, -1, sizeof(groundDist));

    q.push(exitPos);
    groundDist[exitPos.y][exitPos.x] = startTime;

    while (!q.empty()) {
        Point cur = q.front();
        q.pop();

        int y = cur.y;
        int x = cur.x;
        int curTime = groundDist[y][x];

        if (y == escapePos.y && x == escapePos.x)
            return curTime;

        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n)
                continue;

            if (grid[ny][nx] != 0 && grid[ny][nx] != 4)
                continue;

            if (groundDist[ny][nx] != -1)
                continue;

            int nextTime = curTime + 1;

            if (nextTime >= dangerTime[ny][nx])
                continue;

            groundDist[ny][nx] = nextTime;
            q.push({ ny, nx });
        }
    }

    return -1;
}

int main() {
    //freopen("sample_input.txt", "r", stdin);
    input();

    findExit();
    calcDangerTime();

    int wallTime = wallBFS();

    if (wallTime == -1) {
        cout << -1 << '\n';
        return 0;
    }

    cout << groundBFS(wallTime) << '\n';
    return 0;
}