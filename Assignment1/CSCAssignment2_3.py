import math

set1 = [0.012, 0.003, 0.01, 0.1, 0.02, 0.001]
set2 = [0.001, 0.012, 0.003, 0.01, 0.1, 0.02]
set3 = [0.1, 0.02, 0.001, 0.012, 0.003, 0.01]

def mean(arr):
    return sum(arr)/len(arr)

def cross_correlation(x, y):
    x_mean = mean(x)
    y_mean = mean(y)

    numerator = sum(( a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_freq = sum(( a - x_mean) ** 2 for a in x)
    y_freq = sum((b - y_mean) ** 2 for b in y)

    return numerator / math.sqrt(x_freq * y_freq)

correlation_1 = cross_correlation(set1, set2)
correlation_2 = cross_correlation(set1, set3)

print("Cross-correlation of Set 1 and Set 2: ",correlation_1 )
print("Cross-correlation of Set 1 and Set 3: ",correlation_2 )



    