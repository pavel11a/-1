# калькулятор
operation = input( "Действие (+, -, /, *): " )
a = float ( input ("Первое число: ") )
b = float ( input ("Второе число: ") )
if operation == "+":
	c = a + b
	print ( "Результат: " + str(c) )
elif operation == "-":
	c = a - b
	print ("Результат: " + str(c) )
elif operation == "/":
	c = a / b
	print ("Результат: " + str(c) )
elif operation == "*":
	c = a * b
	print ( "Результат: " + str(c) )
