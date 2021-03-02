#include <iostream>
#include <string>

#define GROUP_1_THRESHOLD 18
#define GROUP_2_THRESHOLD 55
#define GROUP_1_NAME "Group A"
#define GROUP_2_NAME "Group B"
#define GROUP_3_NAME "Group C"

std::string GetGroup(int age);

int main() {
    std::string name = "";
    int age = 0;

    std::cout << "Please enter your name: ";
    getline(std::cin, name);
    std::cout << "And please enter your age: ";
    std::cin >> age;

    std::cout << "Welcome " << name << ". You are in group " << GetGroup(age) << ".\n";
}

std::string GetGroup(int age) {
    if (age < 18) {
        return GROUP_1_NAME;
    } else if (age < 55) {
        return GROUP_2_NAME;
    } else {
        return GROUP_3_NAME;
    }
}
