#include <iostream>
#include <string>
#include <vector>

std::vector<int> myVector {10, 20, 30, 40};

void PrintVector() {
    for (int i = 0; i < myVector.size(); ++i) {
        std::cout << myVector[i];
    }

    std::cout << "\n\n";
}

int main() {
    PrintVector();

    myVector.pop_back();
    PrintVector();

    myVector.push_back(6);
    PrintVector();

    myVector.erase(myVector.begin() + 1);
    PrintVector();

    myVector.insert(myVector.begin() + 3, 8);
    PrintVector();
}