while True:
    num1 = int(input())
    num2 = int(input())
    if num1 == num2 or (num1%2==0 and num2%2!=0) or (num2%2==0 and num1%2!=0) or (num1>1000 and num2>1000):
        print("YA")
        break
    else:
        print("TODAVIA NO")