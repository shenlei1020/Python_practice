#include <iostream>
#include <array>
using namespace std;

template <size_t SIZE>
int* sum(array<int, SIZE> arr) {
	int length = arr.size();
	static int returnArr[SIZE];
	for (int i = 0; i < length; i++) {
		returnArr[i] = arr[i];
	}
	return returnArr;
}

int main() {
	int N = 5;
	array<int, N> arr={ 1,3,5,7,9 } ;    // C++ 11 standard
	int* summary = sum(arr);
	for (unsigned int i = 0; i < arr.size(); i++) {
		cout << summary[i] << " ";
	}
	return 0;
}