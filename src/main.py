import pygame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import pandas as pd
import hashlib


def Sha512Hash(Password):
    return hashlib.sha512(Password.encode('utf-8')).hexdigest()
    


if __name__ in "__main__":
    print('Toodles')
