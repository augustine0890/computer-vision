#include <iostream>
#include <string>
#define HELLO_WORLD "Hello World!"
#define LEVEL 3

void Modify(int& a) {
    a = a - 1;
}

int main() {
    // Data type keywords
    int myInt = 1;
    double myDouble = 1.5;
    char myChar = 'c';
    bool myBool = true;

    // Program flow keywords
    if (myBool) {
        std::cout << "true";
    } else {
        std::cout << "false";
    }

    // struct myStruct {
        // int myInt = 1;
    // };

    #ifdef HELLO_WORLD
        std::cout << HELLO_WORLD;
    #endif
    #undef HELLO_WORLD
    #ifdef HELLO_WORLD
        std::cout << HELLO_WORLD;
    #endif
    // std::cout << HELLO_WORLD;

    #if LEVEL == 0
        #define SCORE 0
    #else
    #if LEVEL == 1
        #define SCORE 15
    #endif
    #endif

    #if LEVEL == 2
        #define SCORE 30
    #elif LEVEL == 3
        #define SCORE 45
    #endif

    #ifdef SCORE
        std::cout << SCORE << std::endl;
    #endif

    // I/O statements
    std::string name;
    int age;

    std::cout << "Please enter your name: ";
    // std::cin >> name;
    getline(std::cin, name);
    std::cout << "Please enter your age: ";
    std::cin >> age;
    // getline(std::cin, age);

    std::cout << name << std::endl;
    std::cout << age << std::endl;

    int a = 10;
    Modify(a);
    std::cout << a << std::endl;
}
