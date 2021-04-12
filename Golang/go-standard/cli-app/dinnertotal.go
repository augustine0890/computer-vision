package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	args := os.Args[1:]
	if len(args) == 1 && args[0] == "/help" {
		fmt.Println("Usage: dinnertotal <Total Meal Amount> <Tip Percentage>")
		fmt.Println("Example: dinnertotal 30 10")
	} else {
		if len(args) != 2 {
			fmt.Println("You must enter arguments! Type /help for help")
		} else {
			mealTotal, _ := strconv.ParseFloat(args[0], 32)
			tipAmount, _ := strconv.ParseFloat(args[1], 32)
			fmt.Printf("Your meal total will be %.2f$\n", calculateTotal(float32(mealTotal), float32(tipAmount)))
		}
	}

}

func calculateTotal(mealTotal float32, tipAmount float32) float32 {
	totalPrice := mealTotal + (mealTotal * (tipAmount/100))
	return totalPrice
}
