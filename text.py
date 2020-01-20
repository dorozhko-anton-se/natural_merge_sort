import random
from multiprocessing import Pool


def Write(x):
    file = open('text{}.txt'.format(x), 'w')

    for i in range(20000000):
        file.write(
            str(random.randint(-9223372036854775808, 9223372036854775807)) + '\n')

    file.close()


if __name__ == '__main__':
    with Pool(2) as p:
        p.map(Write, [1, 2])
