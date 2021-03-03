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

### C++ pipeline
- Preprocessor: resolves any preprocessor statements, editing origin code.
- Complilation: creates object files that contain machine code from our source files.
- Linker: Links object files together to create the final executable.

### Preprocessor Directives
#### Include
- `#include` means `copy here`. It will copy and paste the contents of the included file in its place. Any functions, variables, classes, and so on defined in that header are now also accessible by the class containing the `include` directive.
```cpp
// Include example.
// Version 1 - Generally for system files.
#include <headerfile>

// Version 2 - Generally for programmer files.
#include "headerfile"
```
- Version 1: The preprocessor to look for the file using pre-defined search paths. This is typically used for system headers, and these paths might be set by your IDE.
- Version 2: The preprocessor to start its search locally where the file itself sits. This is generally used to include your own project headers.

#### Macros
- The `#define/#undef` directives allow us to define macros in our programs.
```cpp
#define name content
// Defining functionality
#include <iostream>
#define MULTIPLY(a, b) (a * b)

int main() {
    std::cout << MULTIPLY(3, 4);
}
```
#### Conditional Compilation
- The `#ifdef/#endif` directives to help us guard against this by letting us check whether a given values is currently defined.

### Basic I/O Statements
- I/O stands for __input/output__.
- The `iostream` header contains everything we need to interface with our applications via the keyboard.
- Use `std::cin` to read data from keyboard.

### Functions
- Functions encapsulate our code into logical units of functionality
- A function is declared as follows:
```cpp
return_type function_name(parameters);
```
- The declaration usually lives in a header file `(.h)` along with other functions declarations, and they are the defined in a `.cpp` file. (`#include` directive so often)
- We declaration our objects'functionality in header files, then actually define how they work in `.cpp` files.

## Control Flow
- Link [here](https://github.com/augustine0890/computer-vision/tree/master/Cpp/Cpp-Scratch/control-flow)

## Built-In Data Types
- A class is a collection of variables and functionality, encapsulated neatly within a single object.
    ```cpp
    class MyClass
    {
    public:
        // Any members declared from this point forth will be public.
    protected:
        // Any members declared from this point forth will be protected.
    private:
        // Any members declared from this point forth will be private.
    };
    ```
- `Structs` are very similar to classes. The difference between the two is that, by default, class members are private, and in a struct, they are public.
    ```cpp
    #include <iostream>
    #include <string>

    struct Coordinate {
        float x = 0;
        float y = 0;
    };

    int main() {
        Coordinate myCoordinate;
        myCoordinate.x = 1;
        myCoordinate.y = 2;
        std::cout << "Coordinate: " << myCoordinate.x << ", " << myCoordinate.y;
    }
    ```
- Static is a special keyword in C++. The static variables are only inititalized once during the application, and therefore maintain their value throughout.
- Both variables and functions can be made static
    ```cpp
    #include <iostream>
    #include <string>

    int MyInt()
    {
        static int myInt = 0;
        return ++myInt;
    }

    int main()
    {
        for (int i = 0; i < 5; ++i)
        {
            std::cout << MyInt();
        }
    }
    ```