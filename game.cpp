#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    // 设置随机数种子，保证每次运行生成的数字都不一样
    srand(time(0)); 
    int target = rand() % 100 + 1; // 生成 1-100 的随机数
    int guess;
    int tries = 0;

    cout << "==================================" << endl;
    cout << "  欢迎来到猜数字游戏！" << endl;
    cout << "  我已经想好了一个 1-100 之间的数字。" << endl;
    cout << "==================================" << endl;

    do {
        cout << "\n请输入你猜的数字: ";
        cin >> guess;
        tries++;

        if (guess > target) {
            cout << "📉 太大了！再往下猜猜。" << endl;
        } else if (guess < target) {
            cout << "📈 太小了！再往上猜猜。" << endl;
        } else {
            cout << "\n🎉 恭喜你，猜对了！" << endl;
            cout << "你一共猜了 " << tries << " 次。" << endl;
        }
    } while (guess != target);

    return 0;
}