#Игра угадай число
#Компьютер сам загадывает и сам угадывает ч

import numpy as np



def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = [np.random.randint(1, 101) for i in range(100)]
    predict.sort()
    left = 0
    right = len(predict)-1
    center = (left + right) // 2
    
    while predict[center] != number:
        count +=1
        if number > predict[center]:
            left = center +1 
        else: right = center - 1
        center = (left + right) // 2
        if left > right:
            break

    
                                
    return count


#функция для оценки

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)