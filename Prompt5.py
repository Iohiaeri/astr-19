import numpy as np
from tabulate import tabulate

def sin(x):
    y=np.sin(x)
    return y
def main():
    x=0
    values = ({'x':[],'sin(x)':[]})
    for i in range(1001):
        values["x"].append(x)
        values["sin(x)"].append(sin(x))
        x += ((2*np.pi)/1000)
    print(tabulate(values, headers = "keys"))
if __name__ == "__main__":
    main()
    

