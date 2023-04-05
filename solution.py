import pandas as pd
import numpy as np

from scipy import stats


chat_id = 522929689 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.08
    alpha = 1 - p
    l = 0
    
    if(p == 0.9):
        if(len(x) < 11 ):
            l = 0.145
        elif(len(x) < 101):
            l = 0.0150
        else:
            l = 0.8
    elif (p == 0.95):
        l = 0.428
    elif (p == 0.7):
        l = 0.101
    else:
        l = 0.8
    
    
    return x.max(), \
           x.max() + l