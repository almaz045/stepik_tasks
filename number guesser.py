from random import randrange

random_number = randrange(1, 101)
while True:
    number = int(input("Введите число от 1 до 100\n"))
    if number == random_number:
        print("Вы угадали, поздравляем!")
        break
    elif number > random_number:
        print("Слишком много, попробуйте еще раз")
        continue
    else:
        print("Слишком мало, попробуйте еще раз")
        continue
