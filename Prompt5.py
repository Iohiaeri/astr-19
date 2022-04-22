import numpy as np
def main():
    x=0
    for i in range(1001):
        y=np.sin(x)
        y = round(y,3)
        z = round(x,3)
        print(z,'|' ,y)
        x += ((2*np.pi)/1000)
if __name__ == "__main__":
    main()
    

