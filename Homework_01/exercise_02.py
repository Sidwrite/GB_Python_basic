#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


time = int(input("Введите время в секундах:  "))
hours = time // 3600
time %=3600
min = time //60
sec = time % 60

print(f"{hours:02}:{min:02}:{sec:02}")