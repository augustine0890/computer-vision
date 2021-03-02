// Number-Guessing Game
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

int main() {
    std::cout << "***Number guessing game***\n";
    int guessCount, minNumber, maxNumber, randomNumber = 0;
    bool bIsRunning = true;
    std::string input = "";

    while (bIsRunning) {
        std::cout << "\nEnter the number of guesses: ";
        getline(std::cin, input);
        guessCount = std::stoi(input);
        std::cout << "\nEnter the minumum number: ";
        getline(std::cin, input);
        minNumber = std::stoi(input);
        std::cout << "\nEnter the maximum number: ";
        getline(std::cin, input);
        maxNumber = std::stoi(input);


        // Generate random number within range.
        srand((unsigned) time(0));
        randomNumber = rand() % (maxNumber - minNumber + 1) + minNumber;
        
        for (int i = 0; i < guessCount; ++i) {
            int guessNumber = 0;
            std::cout << "\nEnter your guess: ";
            getline(std::cin, input);
            guessNumber = std::stoi(input);

            if (randomNumber == guessNumber) {
                std::cout << "\nWell done, you guessed the number!";
                break;
            }
            int guessesRemaining = guessCount - (i + 1);
            std::cout << "Your guess was too " << (guessNumber < randomNumber ? "low. " : "high. ");
            std::cout << "You have " << guessesRemaining << (guessesRemaining > 1 ? " guesse" : " guess") << " remaining";
            }

        std::cout << "\nEnter 0 to exit, or any number to play again: ";
        getline(std::cin, input);
        if (std::stoi(input) == 0) {
            bIsRunning = false;
        }
    }
}