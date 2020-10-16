#If you have to print a loop in a  straight line use "print(i,end="")" as such after the "for" loop 
if __name__ == '__main__':
    n = int(input())
    if n>=1:
        if n<=150:
            for i in range(1, n+1):
                print(i, end="")