import numpy as np
from tabulate import tabulate

def main():
    x=0
    values = ({'x':[],'sin(x)':[]})
    for i in range(1000):
        y=np.sin(x)
        values["x"].append(x)
        values["sin(x)"].append(y)
        x += ((2*np.pi)/1000)
    print(tabulate(values, headers = "keys"))
if __name__ == "__main__":
    main()
    

