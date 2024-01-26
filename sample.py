def get_evaluation_input():
    while True:
        print('1から5で評価を入力してください')
        point = input()

        if point.isdecimal():
            point = int(point)

            if 1 <= point <= 5:
                return point
            else:
                print('1から5で入力してください')
        else:
            print('評価ポイントは数字で入力してください')

def record_evaluation():
    point = get_evaluation_input()
    print('コメントを入力してください')
    comment = input()
    record = f'評価: {point} コメント: {comment}'
    
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{record}\n')

def show_evaluations():
    print('これまでの評価結果')
    
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main_menu():
    print('実施したい処理を選択してください')
    print('1:評価ポイントとコメントを入力する')
    print('2:今までの結果を確認する')
    print('3:終了する')

def main():
    while True:
        main_menu()
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                record_evaluation()
            elif num == 2:
                show_evaluations()
            elif num == 3:
                print('終了します')
                break
            else:
                print('1から3で入力してください')
        else:
            print('1から3で入力してください')

if __name__ == "__main__":
    main()