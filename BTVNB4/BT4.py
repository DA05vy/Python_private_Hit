import random
def y(n):
    y = [random.uniform(0,10) for _ in range(n)]
    yy = [random.uniform(0,10) for _ in range(n)]
    return y, yy

def is_number(n):
    try:
        n = int(n)
        return n > 0
    except:
        return False


def mae(y,yy,n):
    sum = 0
    for i in range(1,n,1):
        sum += abs(y[i] - yy[i])
    return sum/n

def mse(y,yy,n):
    sum = 0
    for i in range(1,n,1):
        sum += abs(y[i] - yy[i])**2
    return sum/n

def rmse(y,yy,n):
    return mse(y,yy,n)**0.5

def huber(y,yy,n):
    sum = 0
    p = 0.5
    for i in range(1,n,i):
        dif = abs(y[i] - yy[i])
        if dif <= p:
            sum += 0.5*(y[i] - yy[i])**2
        else:
            sum += p*(dif - 0.5*p)
    return sum/n

n = input("Input number: ")
if ( is_number(n) ):
    n = int(n)
    str = input("Input loss name(MAE, MSE, RMSE, Huber_Loss): ")
    if str in ( "MAE", "MSE", " RMSE", "Huber_Loss"):
        y, yy = y(n)
        res = 0
        if ( str == "MAE"):
            res = mae(y,yy,n)
        elif ( str == "MSE"):
            res = mse(y,yy,n)
        elif ( str == "RMSE"):
            res = rmse(y,yy,n)
        elif ( str == "Huber_Loss"):
            res = huber(y,yy,n)
    
        print(y)
        print(yy)
        print(f"{str} : {res}")
    else:
        print(f"{str} is not supported")
else:
    print( f"{n} is not a positive integer number")

            