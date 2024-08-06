import random
from fibonacci import fibonacci, is_fibonacci, fibonacci_quiz, find_nearest_fibonacci

def plot_fibonacci_spiral():
    points = fibonacci_spiral(10)
    x, y = zip(*points)
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'r-')
    plt.title("フィボナッチ・スパイラル")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def explore_fibonacci_word():
    n = int(input("フィボナッチワードの長さを入力してください（10以下推奨）: "))
    word = fibonacci_word(n)
    print(f"フィボナッチワード: {word}")
    print(f"長さ: {len(word)}")
    print(f"0の数: {word.count('0')}")
    print(f"1の数: {word.count('1')}")

def fibonacci_game():
    print("フィボナッチ数列ゲームへようこそ！")
    while True:
        print("\n何をしますか？")
        print("1: フィボナッチクイズに挑戦")
        print("2: 数がフィボナッチ数列に含まれるかチェック")
        print("3: 最も近いフィボナッチ数を見つける")
        print("4: フィボナッチ・スパイラルを描画")
        print("5: フィボナッチワードを探索")
        print("6: 終了")
        
        choice = input("選択してください (1-6): ")
        
        if choice == '1':
            fibonacci_quiz()
        elif choice == '2':
            num = int(input("チェックしたい数を入力してください: "))
            if is_fibonacci(num):
                print(f"{num}はフィボナッチ数列に含まれます！")
            else:
                print(f"{num}はフィボナッチ数列に含まれません。")
        elif choice == '3':
            num = int(input("数を入力してください: "))
            nearest = find_nearest_fibonacci(num)
            print(f"{num}に最も近いフィボナッチ数は{nearest}です。")
        elif choice == '4':
            plot_fibonacci_spiral()
        elif choice == '5':
            explore_fibonacci_word()
        elif choice == '6':
            print("お疲れ様でした！またプレイしてください。")
            break
        else:
            print("無効な選択です。1から6の数字を入力してください。")

if __name__ == "__main__":
    fibonacci_game()
