# C++ from Scratch
## Introduction
### Code Explanation
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}
```
- The `#include` command is a specific proprocessor command the effectively copies and pastes the entire text of the file specified between the angle brackets into the source code.
- The "iostream" file is a short for "input-output streams". It contains code for displaying and getting the text from the user.
- A namespace is essentially a prefix that is applied to all the names in a certain set. Command tells the compiler to allow all the names in the “std” namespace to be usable without their prefix.
- Use the `cout`, `cin` and `endl` tools from the `std` toolbox.
- The starting poit of all C++ programs is the `main` function. Performing the actions specified by the statements in your program.
- `cout` is short for character output
- `cin` is an abbreviation for character input
- Statements in C++ must be terminated with a semicolon.
- The `return` keyword tells the program to return a value to the function `int main`.
- The type of the value returned by a function must match the type specified in the declaration of the function.

### Compiling C++ Code
- The compiler translates the textual representation of the program into a form that a computer can execute more efficiently.
- The compiler is a translator that acts as an intermediary between the programmer and the CPU on the computer.
- There are several compilers:
    - The `GNU Compiler Collection` __(GCC)__ has versions available for most systems and does a good job of implementing the ISO C++ standard.
    - The `clang` compiler has complete support for C++11 and FreeBSD fully support clang and C++11.
- For MacOS X: `Xcode` which uses _gcc_ for compiling C++
- The ports of the GNU Compiler Collection distributed within: `Cygwin` and `MinGW` Or `Geany`
- Each compiler is invoked in a specific way. For example, __GCC__:
    - `g++ main.cpp -o main`
- To invokethe compiled the program:
    - `./main`