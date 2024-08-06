import random
from fibonacci import fibonacci, is_fibonacci, fibonacci_quiz, find_nearest_fibonacci

def fibonacci_game():
    print("フィボナッチ数列ゲームへようこそ！")
    while True:
        print("\n何をしますか？")
        print("1: フィボナッチクイズに挑戦")
        print("2: 数がフィボナッチ数列に含まれるかチェック")
        print("3: 最も近いフィボナッチ数を見つける")
        print("4: 終了")
        
        choice = input("選択してください (1-4): ")
        
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
            print("お疲れ様でした！またプレイしてください。")
            break
        else:
            print("無効な選択です。1から4の数字を入力してください。")

if __name__ == "__main__":
    fibonacci_game()
