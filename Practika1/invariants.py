import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import sqrt

class Triangle:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.general = np.vstack((x,y)).transpose()
        self.N = len(self.general)

    def prints(self):
        print(f"Координаты по оси x: {self.x}")
        print(f"Координаты по оси y: {self.y}")
        print(f"Матрица координат:\n{self.general}\n")

    def draw(self):
        # Создание случайного 16-битного цвета
        r = lambda: randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())

        plt.figure("Invariants")
        plt.scatter(self.x, self.y, s = 30, color=color)

        plt.gca().add_patch(plt.Polygon(self.general[:,:], color=color))

    # Среднее значение
    def mean_x(self):
        return np.mean(self.x)

    def mean_y(self):
        return np.mean(self.y)

    # Формула для mpq
    def _m(self, p, q):
        sum_x = 0.0
        sum_y = 0.0
        # Суммирования резулитатов по оси x
        for i in range(self.N):
            sum_x += (self.x[i] - self.mean_x()) ** p

        # Суммирования резулитатов по оси y
        for i in range(self.N):
            sum_y += (self.y[i] - self.mean_y()) ** q

        return 1/self.N * sum_x * sum_y
        

    # Инвариантные моменты
    def moment(self):
        M = list()
        for i in range(self.N):
            if i == 0:
                # print("m20+m02")
                M.append(self._m(2, 0) + self._m(0, 2))
            if i == 1:
                # print("(m20-m02)^2 + 4m11^2")
                M.append((self._m(2, 0) - self._m(0, 2)) ** 2 + 4 * (self._m(1, 1) ** 2))
            if i == 2:
                # print("(m30 - 3m12)^2 + (3m21+m03)^2")
                M.append((self._m(3, 0) - 3 * self._m(1, 2)) ** 2 + (3 * self._m(2, 1) + self._m(0, 3)) ** 2)

        return M

    # Инвариатность к масштабированию ?? неизвестно как обрабатывать результат
    def scalability(self, M2):
        r = sqrt(self._m(2, 0) + self._m(0, 2))
        M_hatch = M2 / r ** 4
        return M_hatch

if __name__ == '__main__':
    one = Triangle([1,1,3], [1,4,1])
    one.prints()
    one.draw()
    M = one.moment()
    print(f"Инвариантные моменты для первого треугольника:\nM1: {M[0]} \nM2: {M[1]} \nM3: {M[2]}\n")

    # two = Triangle([-1,-1,-3], [1,4,1])
    # two = Triangle([-1,-1,-3], [-1,-4,-1])
    two = Triangle([2,2,9], [-1,-4,-1])
    two.prints()
    two.draw()
    M_two = two.moment()
    print(f"Инвариантные моменты для второго треугольника:\nM1: {M_two[0]} \nM2: {M_two[1]} \nM3: {M_two[2]}\n")

    if M[0] == M_two[0] and M[1] == M_two[1] and M[2] == M_two[2]:
        print("Инвариантные моменты совпадают,\n => Значит это один и тот же треугольник")
    else:
        print("Инвариантные моменты несовпадают,\n => Значит это разные фигуры")

    plt.show()