# Build OpenCV.js

## Emscripten
- Emsccripten is an LLVM-to-JavaScript (compiler toolchain to WebAssembly).
    - Compile C and C++ code, or any other language that uses LLVM, into WebAssembly, and run it on the Web, Node.js, or other wasm runtimes.
    - Compile the C/C++ runtimes of other languages into WebAssembly, and then run code in those other languages in an indirect way.
    - [Download and install](https://emscripten.org/docs/getting_started/downloads.html) or using [unofficial](https://formulae.brew.sh/formula/emscripten) package (not recommended).
    - OpenCV [docs](https://docs.opencv.org/master/d4/da1/tutorial_js_setup.html)

## Obtaining OpenCV Source Code
- Launch Git client and clone OpenCV repository
    - `git clone https://github.com/opencv/opencv.git`
- Install `cmake`
    - `brew install cmake`

## Building OpenCV.js from Source
- Please refer [here](https://github.com/opencv/opencv/tree/master/platforms/js)
- OpenCV.js location: `$PATH/build_js/bin/opencv.js`

## Docker Image for `opencv4nodejs`
- Usage: `./build.sh <OpenCV version> <with contrib?> <node major version>`
    - `sudo chmod 755 'build.sh'`
- Example: Build OpenCV 3.4.14 with contrib and node version 12.x
    - `./build.sh 3.4.14 y 12`