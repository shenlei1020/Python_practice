#include <iostream>
#include <ctime>
#include <cstdlib>
#include <string.h>

using namespace std;

int copymatrix()
{
	const int M = 6;
	const int N = 5;
	int board[M][N];
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			board[i][j] = i * N + j;
		}
	}
	int myboard[M][N];
	memcpy(myboard, board, sizeof(myboard));

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cout << "board = " << board[i][j] << "\t";
			cout << "myboard = " << myboard[i][j] << endl;
		}
	}

	return 0;
}