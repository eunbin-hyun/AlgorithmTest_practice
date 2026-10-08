#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

// 마을의 크기n, 전사의 수 m
int n, m;

struct Point {
    int y, x;
};

// dir: 상(0), 하(1), 좌(2), 우(3)
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

// 두번째 이동 (좌우상하)
int secondMove[4] = { 2,3,0,1 };

// 도로0, 도로 아님 1
int grid[51][51];
// 메두사가 보는칸
bool sight[51][51];


// 메두사 집 start, 공원 위치 park
Point start, park;
// 전사 몇명이 위치에 있는지 warriorCnt
int warriorCnt[51][51];

// 메두사 위치
int cy, cx, cd;

// 출력값: warriorMoveSum, stoneWarriorNum, attachWarrior 
int warriorMoveSum, stoneWarriorNum, attachWarrior;

// 메두사 이동경로
int dist[51][51] = { 0 };

// 1. 메두사의 이동경로 역 BFS
bool madusaPath() {
    dist[park.y][park.x] = 1;

    queue<Point> q;
    q.push({ park.y, park.x });

    while (!q.empty()) {
        Point now = q.front();
        q.pop();

        for (int d = 0; d < 4; d++) {
            int ny = now.y + dy[d];
            int nx = now.x + dx[d];

            if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
            if (dist[ny][nx] || grid[ny][nx])continue;

            dist[ny][nx] = dist[now.y][now.x] + 1;
            q.push({ ny,nx });
        }
    }

    if (dist[start.y][start.x])return true;
    return false;
}

// 1-2. 메두사 이동
void madusaMove() {
    for (int d = 0; d < 4; d++) {
        int ny = cy + dy[d];
        int nx = cx + dx[d];

        if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
        if (grid[ny][nx]) continue;

        if (dist[ny][nx] == dist[cy][cx] - 1) {
            cy = ny, cx = nx;
            break;
        }
    }

    // 메두사 이동한곳에 전사있으면 전사 사라짐
    if (warriorCnt[cy][cx]) warriorCnt[cy][cx] = 0;

}

// 상대 좌표를 진짜 좌표에 적용가능하도록 변환
Point convert(int d, int front, int side) {
    if (d == 0) return { cy - front, cx + side }; // 상
    else if (d == 1) return  { cy + front,  cx + side }; // 하
    else if (d == 2) return { cy + side, cx - front }; // 좌
    else return { cy + side, cx + front };        // 우
}

// 2. 메두사 시선
void madusaSight() {
    bool bestSight[51][51] = { 0 };
    int bestStoneCnt = -1; // stone이 0인경우 우선 배정이되어야하니까.

    int bestDir = 0;

    for (int d = 0; d < 4; d++) {
        bool tmpSight[51][51] = { 0 }; // 시야
        int block[51][51] = { 0 }; // 가려지는 부분
        int tmpStoneCnt = 0; // 돌이되는 전사

        // 방향마다 적용가능하도록 
        // 2-1. 가까운 줄부터 먼 줄까지 탐색
        for (int front = 1; front < n; front++) {
            for (int side = -front; side <= front; side++) {
                // 상하좌우에 따라 y,x변환
                Point p = convert(d, front, side);

                if (p.y < 0 || p.x < 0 || p.y >= n || p.x >= n) continue;

                // 전사 때문에 가려진칸
                if (block[p.y][p.x]) continue;

                // 여기까지 왔으면 실제 보이는칸
                tmpSight[p.y][p.x] = 1;

                if (warriorCnt[p.y][p.x] > 0) {
                    tmpStoneCnt += warriorCnt[p.y][p.x];

                    // 2-2. 이 전사 뒤쪽은 block 처리
                    // 1) 정면
                    if (side == 0) {
                        for (int nf = front + 1; nf < n; nf++) {
                            Point np = convert(d, nf, side);
                            if (np.y < 0 || np.x < 0 || np.y >= n || np.x >= n) continue;
                            block[np.y][np.x] = 1;
                        }
                    }
                    // 2) 왼쪽
                    else if (side < 0) {
                        for (int nf = front + 1; nf < n; nf++) {
                            int diff = nf - front; // 가려짐 기준
                            for (int ns = side - diff; ns <= side; ns++) {
                                Point np = convert(d, nf, ns);
                                if (np.y < 0 || np.x < 0 || np.y >= n || np.x >= n) continue;
                                block[np.y][np.x] = 1;
                            }
                        }
                    }
                    // 3) 오른쪽
                    else {
                        for (int nf = front + 1; nf < n; nf++) {
                            int diff = nf - front;
                            for (int ns = side; ns <= side + diff; ns++) {
                                Point np = convert(d, nf, ns);
                                if (np.y < 0 || np.x < 0 || np.y >= n || np.x >= n) continue;
                                block[np.y][np.x] = 1;
                            }
                        }
                    }
                }
            }
        }

        if (tmpStoneCnt > bestStoneCnt) {
            memcpy(bestSight, tmpSight, sizeof(tmpSight));
            bestStoneCnt = tmpStoneCnt;
            bestDir = d;
        }
    }
    memcpy(sight, bestSight, sizeof(bestSight));
    stoneWarriorNum = bestStoneCnt;
    cd = bestDir;
}

// 3. 전사들의 이동, 4. 전사의 공격
void warriorMove() {
    int tmpCnt[51][51] = { 0 };
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {

            // 전사가 아닌경우 패스
            if (warriorCnt[y][x] == 0) continue;

            // 석화된 전사는 그대로
            if (sight[y][x]) {
                tmpCnt[y][x] += warriorCnt[y][x];
                continue;
            }

            // 1번째 이동
            bool move1 = false;
            int fy = -1, fx = -1;
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];

                if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
                if (sight[ny][nx]) continue; // 메두사 시야로는 못들어감

                int curDist = abs(y - cy) + abs(x - cx);
                int nxtDist = abs(ny - cy) + abs(nx - cx);

                if (nxtDist < curDist) {
                    warriorMoveSum += warriorCnt[y][x];
                    move1 = true;
                    fy = ny, fx = nx;

                    break;
                }
            }

            // 1번째 이동 없으면 그대로 복사
            if (!move1) {
                tmpCnt[y][x] += warriorCnt[y][x];
                continue;
            }
            // 1차공격 받으면 전사는 사라짐
            if (fy == cy && fx == cx) {
                attachWarrior += warriorCnt[y][x];
                continue;
            }

            // 2번째 이동
            bool move2 = false;
            int sy = fy, sx = fx;
            for (int d = 0; d < 4; d++) {
                int ny = fy + dy[secondMove[d]];
                int nx = fx + dx[secondMove[d]];

                if (ny < 0 || nx < 0 || ny >= n || nx >= n)continue;
                if (sight[ny][nx]) continue; // 메두사 시야로는 못들어감

                int curDist = abs(fy - cy) + abs(fx - cx);
                int nxtDist = abs(ny - cy) + abs(nx - cx);

                // 2차이동
                if (nxtDist < curDist) {
                    sy = ny, sx = nx;
                    move2 = true;
                    warriorMoveSum += warriorCnt[y][x];
                    break;
                }
            }
            // 2차 이동 후 공격
            if (move2 && sy == cy && sx == cx) {
                attachWarrior += warriorCnt[y][x];
                continue;
            }
            // 2차 이동 못했으면 sy,sx 그대로
            tmpCnt[sy][sx] += warriorCnt[y][x];
        }
    }
    memcpy(warriorCnt, tmpCnt, sizeof(tmpCnt));
}


int main() {
    cin >> n >> m;
    cin >> start.y >> start.x >> park.y >> park.x;
    int ay, ax;
    for (int i = 0; i < m; i++) {
        cin >> ay >> ax;
        warriorCnt[ay][ax]++; // 같은 위치의 전사 같이 이동하기에.. 함께해도됌
    }
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cin >> grid[y][x];
        }
    }

    cy = start.y, cx = start.x;

    // 1. 메두사 경로
    if (!madusaPath()) {
        cout << -1;
        return 0;
    }

    while (true) {
        warriorMoveSum = 0, stoneWarriorNum = 0, attachWarrior = 0;
        // 1-2. 메두사의 이동
        madusaMove();

        // 메두사 공원 도착 시 종료
        if (cy == park.y && cx == park.x) {
            cout << 0;
            break;
        }

        // 2. 메두사 시선
        madusaSight();
        // 3. 전사들의 이동,  4. 전사의 공격
        warriorMove();
        cout << warriorMoveSum << ' ' << stoneWarriorNum << ' ' << attachWarrior << '\n';
    }
}