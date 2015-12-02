#include <iostream>
using namespace std;

int main() {
	cout << "Hello Raspberry" << endl;

	int sum = 0;
	int n = 9;
	sum = (n * (n + 1)) >> 1;

	cout << "Sum:" << sum << endl;

	return 0;
}
