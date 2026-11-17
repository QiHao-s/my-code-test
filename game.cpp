#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void playGame() {
    srand(time(0)); 
    int target = rand() % 1000 + 1; 
    int guess;
    int tries = 0;
    int max_tries = 10; // 给10次机会

    system("cls"); // 清空屏幕，保持界面干净
    cout << "==================================" << endl;
    cout << "      Welcome to Guessing Game 2.0!" << endl;
    cout << "  I have picked a number between 1 and 1000." << endl;
    cout << "  You have " << max_tries << " tries." << endl;
    cout << "==================================" << endl;

    while (tries < max_tries) {
        cout << "\n[Try " << tries + 1 << "/" << max_tries << "] Enter your guess: ";
        cin >> guess;
        tries++;

        if (guess == target) {
            cout << "\n*** Congratulations! You got it in " << tries << " tries. ***" << endl;
            return; // 猜对了，直接结束这个函数
        } else if (guess > target) {
            cout << "Too high! Try a smaller number." << endl;
        } else {
            cout << "Too low! Try a larger number." << endl;
        }
    }

    // 如果 while 循环结束还没 return，说明次数用光了
    cout << "\n--- Out of tries! The correct number was: " << target << " ---" << endl;
}

int main() {
    char playAgain;
    
    // 这是一个无限循环，直到玩家选择 'n'
    do {
        playGame(); // 呼叫上面的游戏函数

        cout << "\nDo you want to play again? (y/n): ";
        cin >> playAgain;
        
    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "\nThanks for playing. Goodbye!" << endl;
    return 0;
}