#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

// 격자 n, 거북이 m, 화산수 k
int n, m, k;
int turn;

// 방향: 우(0), 하(1), 좌(2), 상(3) - 시계방향
int dy[4] = { 0,1,0,-1 };
int dx[4] = { 1,0,-1,0 };

struct Point {
    int y, x;
};

// 거북이위치 y,x, time(화석 -1, 도달 못했음 0, 도달한시간)
struct Turtle {
    int y, x;
    int time;
};

// 화산위치 y,x, 분출임계치 p, 마그마 압력 v
struct Mount {
    int y, x, p,v;
};

// 산호초 -1
int grid[20][20];
Turtle turtles[11];
Mount mounts[11];
int result[11] = { -1 };

// 1단계: 바다거북 이동 (역 BFS이용)
void turtleMove() {

    // 1-2) 거북이 id 작은 순서대로 이동 
    for (int id = 1; id <= m; id++) {
        if (turtles[id].time != 0) continue;

        // 1-1) 역 BFS로 거북이 경로 파악
        int visited[20][20];
        memcpy(visited, grid, sizeof(grid));

        // 거북이있는곳도 못 지나간다고 처리
        for (int id = 1; id <= m; id++) {
            // 도착한 거북이는 지도에서 사라짐
            if (turtles[id].time > 0) continue;

            int ty = turtles[id].y, tx = turtles[id].x;
            visited[ty][tx] = -1;
        }

        queue<Point> q;
        visited[n - 1][n - 1] = 1;
        q.push({ n - 1, n - 1 });

        while (!q.empty()) {
            Point now = q.front();
            q.pop();

            for (int d = 0; d < 4; d++) {
                int ny = now.y + dy[d];
                int nx = now.x + dx[d];

                if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
                if (visited[ny][nx] != 0) continue;

                visited[ny][nx] = visited[now.y][now.x] + 1;
                q.push({ ny, nx });
            }
        }

        // 거북이 이동
        int dist = 999;
        int my=-1, mx=-1;

        for (int d = 0; d < 4; d++) {
            int ny = turtles[id].y + dy[d];
            int nx = turtles[id].x + dx[d];

            if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
            if (visited[ny][nx] <= 0) continue;

            if (dist > visited[ny][nx]) {
                my = ny, mx = nx;
                dist = visited[ny][nx];
            }
        }

        if (dist == 999) continue;

        turtles[id].y = my, turtles[id].x = mx;
        visited[my][mx] = -1;

        // 1-3) 안식처 도착하면 시간 기록,지도에서 제외
        if (my == n-1 && mx == n-1) {
            turtles[id].y = -1, turtles[id].x = -1;
            turtles[id].time = turn;
            visited[my][mx] = 0;
        }
    }
}

// 2~4 단계: 화산 압력증가, 분출 및 연쇄반응, 환경 초기화
void mountsUp() {
    // 2. 화산 압력 증가
    for (int id = 1; id <= k; id++) {
        mounts[id].v += 10;
    }

    // 3. 화산 분출
    int hotgrid[20][20];
    bool mnt[11] = { false }; // 화산 분출 여부
    memset(hotgrid, 0, sizeof(hotgrid));
    queue<int> q;

    for (int id = 1; id <= k; id++) {
        if (mounts[id].v >= mounts[id].p) {
            mnt[id] = true;
            q.push(id);
        }
    }
    
    // 3-1, 3-2) 열기 전파, 연쇄작용
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        hotgrid[mounts[now].y][mounts[now].x] += mounts[now].p;

        // 3-1) 열기 전파
        for (int d = 0; d < 4; d++) {
            int hot = mounts[now].p;
            for (int mux = 1; mux <= n; mux++) {
                int ny = mounts[now].y + dy[d] * mux;
                int nx = mounts[now].x + dx[d] * mux;

                if (ny < 0 || nx < 0 || ny >= n || nx >= n) break;
                if (grid[ny][nx] == -1) break;

                hot /= 2;
                if (hot == 0) break;

                hotgrid[ny][nx] += hot;
            }
        }

        // 3-2) 연쇄 작용
        for (int id = 1; id <= k; id++) {
            // (현재 마그마 압력 + 해당 칸에 누적된 외부 열기) ≥ 분출 임계치(P) 
            if (!mnt[id] && mounts[id].v + hotgrid[mounts[id].y][mounts[id].x] >= mounts[id].p) {
                mnt[id] = true;
                q.push(id);
            }
        }
    }

    // 3-3) 바다거북의 위기(화석화)
    for (int id = 1; id <= m; id++) {
        if (turtles[id].time != 0) continue;

        if (hotgrid[turtles[id].y][turtles[id].x] >= 20) {
            turtles[id].time = -1;
        }
    }

    // 4단계: 환경 초기화
    for (int id = 1; id <= k; id++) {
        if (mnt[id]) mounts[id].v = 0;
    }

}


int main() {
    cin >> n >> m >> k;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cin >> grid[y][x];
            if (grid[y][x])grid[y][x] = -1;
        }
    }
    for (int id = 1; id <= m; id++) {
        cin >> turtles[id].y >> turtles[id].x;
        turtles[id].time = 0;
    }
    for (int id = 1; id <= k; id++) {
        cin >> mounts[id].y >> mounts[id].x >> mounts[id].p;
        mounts[id].v = 0;
    }

    while (turn < 100) {
        turn++;
        turtleMove();
        mountsUp();
    }
    
    for (int id = 1; id <= m; id++) {
        if (turtles[id].time == 0) turtles[id].time = -1;
        cout << turtles[id].time << '\n';
    }
}