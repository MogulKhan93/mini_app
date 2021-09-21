import sys
import random
            

def start_game_loop():
    # Ігровой цикл
    number = random.randint(0, 1000)
    try:
        while True:
            input_number = int(input("Введіть число від 0 до 1000: "))
            if input_number > number:
                print("Число менше ")
            elif input_number == number:
                print("Вітаю, ти переміг! \n")
                break
            elif input_number < 0:
                print('Число має бути додатнім, а також від 0 до 1000!')
            else:
                print("Число більше ")
            print("")
    except ValueError:
        print('Потрібно вводити лише числа, і щоб вони були від 0 до 1000!!!')


while True:
    # Основний цикл
    choice = input("Хочете зіграти? (Y/n) ")
    if choice.lower() == "y":
        start_game_loop()
    else:
        print("Бувай..ще побачимось!")
        sys.exit()
