def viny_puh(str):
    str = str.split()
    list = []
    for word in str:
        k = 0
        for i in word:
            k += 1
        list.append(k)
    if len(set(list)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

viny_puh(input())