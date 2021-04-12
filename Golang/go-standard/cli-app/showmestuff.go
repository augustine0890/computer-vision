package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
)

func main() {
	// this is where stuff happens
	// fmt.Println("The current version of Go is " + runtime.Version())
	readr := bufio.NewReader(os.Stdin)
	fmt.Println("What's your name?")
	text, _ := readr.ReadString('\n')
	fmt.Printf("Hello, %v", text)
	fmt.Printf("We are using Go %v running in %v\n", runtime.Version(), runtime.GOOS)
}
