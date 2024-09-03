import numpy as np

def solution_station_6(x):
    a = 0.9998
    b = 1.0001
    c = -0.0002
    d = 0.0002
    
    # Calculate the y value based on the fitted trig function
    y = a * np.sin(b * x + c) + d
    return round(y, 4)
