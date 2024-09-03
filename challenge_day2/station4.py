def solution_station_4(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # If n is divisible by i, it is not prime
            return False
    return True

