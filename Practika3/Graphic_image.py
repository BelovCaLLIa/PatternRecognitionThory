import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from random import randint
import numpy as np

# Генерация цвета вида #DDDDDD
def color():
    r = lambda: randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    return color

def formula(fi):
    # np.around - округляет значения до decimals
    # Применяется так как sin(180) != 0
    # Модуль важен!
    return np.around(abs(1 * np.sin(1 * np.radians(fi)) + 2 * np.sin(2 * np.radians(fi))), decimals=10)


if __name__ == '__main__':
    # шаг с которым будет увеличиваться угол 
    step = int(input("Введити целое число с которым хотите увеличивать угл:\n"))

    fi = np.array([])
    roFromFi = np.array([])

    # Формируем таблицу 
    count = 0
    # 181 для того, чтобы 180 входило
    for degrees in range(0,361, step):
        count += 1
        fi = np.append(fi, np.radians(degrees))
        roFromFi = np.append(roFromFi, formula(degrees))
    
        print(f"{count} шаг:\t{degrees}\t{roFromFi[count-1]}")

    # r = np.arange(1, 10, 1)

    # theta = [i*np.pi/2 for i in range(9)]
    """ theta = []
    for i in range(len(r)):
        theta.append(i*np.pi/2) """

    plt.figure("Полярная развёртка")

    # Первый параметр отвечает за позицианирование
    # projection = 'polar' Укажите как полярные координаты
    ax = plt.subplot(111,projection='polar')


    #theta - угол, r - полярный диаметр.
    # linewidth - толщина линии
    # Виды markers: https://matplotlib.org/stable/api/markers_api.html
    if len(fi) == len(roFromFi):
        ax.plot(fi, roFromFi, marker='o', linewidth=2, color=color())
        # Подпись к точкам
        """ for x, y in zip(fi, roFromFi):
            ax.text(x, y, f"{(round(x, 2), round(y, 2))}") """
    else:
        print("Количество вершин не соответствует количеству вычесленных точек!")
        raise SystemExit

    #Есть сетка
    ax.grid(True) 
    plt.show()