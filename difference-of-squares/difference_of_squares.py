def square_of_sum(num):
    """retorna el cuadrado de una sumatoria"""
    return sum(range(1, num+1))**2


def sum_of_squares(num):
    """retorna la sumatoria de los cuadrados"""
    return sum(i*i for i in range(1, num+1))


def difference_of_squares(num):
    """retorna la diferencia entre el cuadrado de una sumatoria
    y la sumatoria de los cuadrados"""
    return square_of_sum(num) - sum_of_squares(num)
