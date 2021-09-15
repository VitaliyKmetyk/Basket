try:  
    print("Дано масив х, розмірність якого = 2n.")
    n = 2 *int(input("Введіть n(ціле число) = "))
except ValueError:
    print("Помилка! Введене n не є цілим числом " )
else:
    print("Ведіть", n, " елементів масиву")
    x = [float(input()) for i in range(n)]
    print("Ваш масив х = ", x)
    array = []
    for i in range(int(n/2)):
        array.append(min(x[i], x[n-1-i]))
    print("max(min(x[0], x[n-1]),...min(x[n-1], x[n])) = ",max(array))