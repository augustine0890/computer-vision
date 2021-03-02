#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Loop Starting... \n";
    int count = 1;
    while (count <= 5) {
        cout << "\n" << count;
        if (count == 2)
        break;
        ++count; // increment
    }

    cout << "\n\nContinue..\n";
    count = 0;
    while (count < 5) {
        ++count;
        if (count == 3) {
            continue;
        }
        cout << "\n" << count;
    }
    cout << "\n\nLoop finished.";

    return 0;
}