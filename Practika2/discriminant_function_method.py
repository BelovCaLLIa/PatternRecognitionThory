import matplotlib.pyplot as plt
import numpy as np
from random import randint


class Discriminant_function_method:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.general = np.vstack((x,y)).transpose()

    # Возвращает отдельно X и Y координаты
    def getCoordinateX(self):
        return self.x

    def getCoordinateY(self):
        return self.y

    # Нахождение средних значений по x и y
    def mean(self):
        sum = 0.0
        for i in range(len(self.x)):
            sum += self.x[i]
        x_mean = sum/len(self.x)

        sum = 0.0
        for i in range(len(self.y)):
            sum += self.y[i]
        y_mean = sum/len(self.y)

        return x_mean, y_mean

    # Матрица отклонений
    def deviation(self, x_mean, y_mean):
        x = np.array(self.general[:, 0] - x_mean)
        y = np.array(self.general[:, 1] - y_mean)
        return np.array(np.vstack((x,y)).transpose())

    # Обобщённая матрица ковариации
    def covariance(self, X1, X2):
        S1 = X1.transpose() @ X1
        S2 = X2.transpose() @ X2
        len(X1) + len(X2) - 2
        S0 = (S1 + S2) / (len(X1) + len(X2) - 2)
        return S0, S1, S2

    # Обратная матрица к S0
    def inverseCovariance(self, S0):
        # Функция linalg.inv() вычисляет обратную матрицу
        S0_inverse = np.linalg.inv(S0)
        return S0_inverse

    # Находим матрицу коэффициентов дискриминантной функции
    def coefficientMatrix(self, S0_inverse, x_mean, y_mean):
        X_mean = np.array([[x_mean, y_mean]])
        A = S0_inverse @ X_mean.transpose()
        return A

    # Уравнение прямой, вычисляем функцию
    def equationLine(self, A, meanList):
        if len(A) == len(meanList):
            f = 0.0
            for i in range(len(A)):
                f += A[i] * meanList[i]
            return f
        else:
            # Если это случилось, проверить кол-во средних значений
            print("Недастаёт операндов в записи!")
            return None

    def prints(self):
        print(f"Координаты по оси x: {self.x}")
        print(f"Координаты по оси y: {self.y}")
        print(f"Матрица координат:\n{self.general}\n")

    def draw(self):

        plt.figure("Метод Дискриминантной Функции")
        # Устанавливаем координаты для отображения
        plt.xlim(0,6)
        plt.ylim(0,6)

        plt.scatter(self.x, self.y, s = 50, color=color)

# Генерация цвета вида #DDDDDD
def color():
    r = lambda: randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    return color

def draw(oneClassPoint, twoClassPoint, onePointLine, twoPointLine):

    one_x = oneClassPoint.getCoordinateX()
    one_y = oneClassPoint.getCoordinateY()

    two_x = twoClassPoint.getCoordinateX()
    two_y = twoClassPoint.getCoordinateY()
    
    fig = plt.figure("Метод Дискриминантной Функции")

    # Вычисляем коэффициенты
    coefficients = np.polyfit(onePointLine, twoPointLine, 1)

    # Создим полиномиальный объект с коэффициентами
    polynomial = np.poly1d(coefficients)

    # Чтобы линия выходила за две точки, 
    # создаём линейное пространство, используя min и max x_lim,
    # И задаём пределы этого пространства
    x_axis = np.linspace(-10, 10)

    # Вычисляем Y для каждого X, используя полином
    y_axis = polynomial(x_axis)

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # Устанавливаем координаты для отображения
    axes.set_xlim(-6, 6)
    axes.set_ylim(-6, 6)

    axes.scatter(one_x, one_y, s = 50, color=color())
    axes.scatter(two_x, two_y, s = 50, color=color())
    col = color()
    axes.plot(x_axis, y_axis, color=col, label="Прямая разделяющая два класса объектов")
    axes.plot(onePointLine, twoPointLine, marker='o', color=col)
    # Вывод легенды
    axes.legend()
    # Показ сетки
    axes.grid(which="major")
    plt.show()

if __name__ == '__main__':
    # Данные с практики
    one_class = Discriminant_function_method([1, 3, 4], [2, 3, 5])
    two_class = Discriminant_function_method([4, 5, 5], [3, 4, 2])

    # Свои данные
    # one_class = Discriminant_function_method([-2, 1, 3], [3, 2, 5])
    # two_class = Discriminant_function_method([4, 4, 6], [3, 1, 2])

    # Есть артефакты (но система молодец=))
    # one_class = Discriminant_function_method([-2, -3, 1], [3, -1, 1])
    # two_class = Discriminant_function_method([2, 1, -2], [1, -1, -2])

    one_class.prints()
    two_class.prints()

    X1x_mean, X1y_mean = one_class.mean()
    X2x_mean, X2y_mean = two_class.mean()
    print(f"1 группа среднее значение\nX1x: {X1x_mean}\nX1y: {X1y_mean}\n2 группа среднее значение\nX2x: {X2x_mean}\nX2y: {X2y_mean}")

    X1_matrix = one_class.deviation(X1x_mean, X1y_mean)
    X2_matrix =two_class.deviation(X2x_mean, X2y_mean)
    print(f"Матрица отклонений переменных от средних значений для 1 группы:\n{X1_matrix}\nМатрица отклонений переменных от средних значений для 2 группы:\n{X2_matrix}\n")

    # Находим обобщённую матрицу ковариации
    # covariance() оперирует с обоими объектами
    S0, S1, S2 = one_class.covariance(X1_matrix, X2_matrix)
    print(f"Матрица ковариации для 1 группы:\n{S1}\nМатрица ковариации для 2 группы:\n{S2}\nОбобщённая матрица ковариации:\n{S0}\n")

    # Обратная матрица к S0
    S0_inverse = one_class.inverseCovariance(S0)
    print(f"Обратная матрица ковариации:\n{S0_inverse}\n")

    # Находим вектор коэффициентов дискриминантной функции
    # coefficientMatrix() оперирует с обоими объектами
    A = one_class.coefficientMatrix(S0_inverse, X1x_mean - X2x_mean, X1y_mean - X2y_mean)
    print(f"Вектор коэффициентов дискриминантной функции:\n{A}\n=>\na1: {A[0]}\na2: {A[1]}\n")

    # Подставляем полученный вектор в уравнение прямой (для каждой, получаем 2 функции)
    oneMeanList = [X1x_mean, X1y_mean]
    twoMeanList = [X2x_mean, X2y_mean]
    f1 = one_class.equationLine(A, oneMeanList)
    f2 = two_class.equationLine(A, twoMeanList)
    print(f"Значение функции f1= {f1[0]}\nЗначение функции f2= {f2[0]}\n")

    # Находим константу с
    c = (f1[0] + f2[0]) / 2
    print(f"Константа с= {c}\n")

    # Находим координаты для разделяющей прямой
    x1 = c / A[0]
    x2 = c / A[1]
    print(f"Координаты для разделяющей прямой:\nx1(x)={x1[0]}\nx2(y)={x2[0]}\n")

    # Рисуем всё
    draw(one_class, two_class, [x1[0], 0.0], [0.0, x2[0]])