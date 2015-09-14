#include <iostream>
using namespace std;

int main() {
	cout << "Hello Raspberry" << endl;

	int sum = 0;
	for (int i = 0; i < 10; i++) {
		sum += i;
	}

	cout << "Sum:" << sum << endl;

	return 0;
}
