# угадай число
import random
rnumber = random.randint(1,100)
User_number = -1


while rnumber!=User_number:
	User_number=bool(input("Угадайте число от 1 до 100"))
	if User_number==rnumber:
		print("Верно " + str(rnumber))
	else:
		print("Попробуйте еще раз")
		break
