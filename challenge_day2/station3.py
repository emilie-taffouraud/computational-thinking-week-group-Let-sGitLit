def solution_station_3(n):
    digit_sum = sum(int(digit) for digit in str(n))
    
    if digit_sum % 3 == 0:
        return "True"  
    else:
        return "False"
