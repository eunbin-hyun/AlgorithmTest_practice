#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, m, t;
// 상하좌우
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};

int map[21][21];
int chk[21][21]; // 현재 구슬 위치
int nxt_chk[21][21]; // 이동한 구슬 위치

struct Point {
    int y, x;
};

queue<Point> q;

int main(){
    // 입력
    cin >>n >> m >> t;
    for(int y=1; y<=n; y++){
        for(int x=1; x<=n; x++){
            cin >> map[y][x];
        }
    }
    for(int i=0; i<m; i++){
        int r,c;
        cin >> r >> c;
        q.push({r,c});
        chk[r][c] =1;
    }

    // 구슬이동
    int cnt =0;
    for(int T=1; T<=t; T++){
        memset(nxt_chk, 0, sizeof(nxt_chk));
        while(!q.empty()){
            Point now = q.front();
            q.pop();
            int ry = now.y, rx=now.x;
            int max_val =-1;
            for(int d=0; d<4; d++){
                int ny = now.y + dy[d];
                int nx = now.x + dx[d];

                if(ny<=0 || nx<=0 || ny> n || nx> n)
                    continue;
                
                if(max_val < map[ny][nx]){
                    max_val = map[ny][nx];
                    ry = ny, rx = nx;
                }
            }
            nxt_chk[ry][rx]++;
        }

        // 겹치는 않은 구슬 넣어주기
        cnt =0;
        for(int y=1; y<=n; y++){
            for(int x=1; x<=n; x++){
                if(nxt_chk[y][x]==1){
                    q.push({y,x});
                    cnt++;
                } 
                else if(nxt_chk[y][x]>1){
                    nxt_chk[y][x]=0;
                }
                chk[y][x] = nxt_chk[y][x];
            }
        }
    }
    cout << cnt ;
}
