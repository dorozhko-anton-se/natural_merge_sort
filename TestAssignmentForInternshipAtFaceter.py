def Merger():
    result = open('result.txt', 'w')
    file1 = open('text1.txt', 'r')
    file2 = open('text2.txt', 'r')
    tmp = file1.readline()

    for num1 in file1:
        if int(num1) < int(tmp):
            result.write(str(num1))
        else:
            result.write(str(tmp))
            tmp = num1
            for num2 in file2:
                if int(num2) < int(tmp):
                    result.write(str(num2))
                else:
                    result.write(str(tmp))
                    tmp = num2
                    break

    result.write(str(tmp))
    result.close()
    file1.close()
    file2.close()


def Distribution():
    result = open('result.txt', 'r')
    file1 = open('text1.txt', 'w')
    file2 = open('text2.txt', 'w')
    tmp = result.readline()
    file1.write(str(tmp))
    switch = True

    for num in result:
        if switch:
            if int(num) >= int(tmp):
                file1.write(str(num))
                tmp = num
            else:
                file1.write(str(num))
                switch = not switch
        else:
            if int(num) >= int(tmp):
                file2.write(str(num))
                tmp = num
            else:
                file2.write(str(num))
                switch = not switch

    result.close()
    file1.close()
    file2.close()


for i in range(1000):
    Merger()
    Distribution()

# TODO: 
# 1)функция Distribution() теряет записи, найти утечку
# 2)число между возрастающими последовательностями не сортируется (0134 3 2567)
# 3)вместо цикла использовать бесконечный цикл, который прерывается, когда файл result.txt перестает изменяться.
# Идея использовать switch-sorted, который становится True, когда за все итерации цикла не было записей в result.txt