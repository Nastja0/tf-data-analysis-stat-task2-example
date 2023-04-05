import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 522929689 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.08
    alpha = 1 - p
    
    mean_X = x.mean()  

    u_alpha = norm.ppf(alpha / 2, loc=mean_X, scale=x.std() / len(x))
    u_1_alpha = norm.ppf(1-alpha / 2, loc=mean_X, scale=x.std() / len(x))
    
    
    return x.max(), x.max() + (x.min() - a) / len(x)