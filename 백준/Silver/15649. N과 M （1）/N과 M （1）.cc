#include <iostream>
using namespace std;

int n,m;
int path[9] = {0};
int visited[9] ={0};

void func(int lev){
	if(lev== m){
		for(int i=0; i<lev; i++)
		{
			cout << path[i] << " ";
		}
		cout << "\n";
		return;
	}
	for(int i=1; i<= n; i++){
		if(visited[i])
		continue;	
		
		visited[i] =1;
		path[lev] = i;
		func(lev+1);
		path[lev] =0;
		visited[i] =0;
	}
}

int main(){
	cin >> n >> m;
	func(0);
	return 0;
}