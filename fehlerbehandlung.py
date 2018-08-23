import math

def loesungsformel(p, q):
    if not (math.pow((p/2),2) - q >= 0):
        raise ValueError("No result")    

    x = -p/2 + math.sqrt((p/2)**2 - q)
    y = -p/2 - math.sqrt((p/2)**2 - q)

    assert x**2 + p * x + q == 0 and y**2 + p * y + q == 0

    return x, y

print(loesungsformel(5, 7))
