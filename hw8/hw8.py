'''
1. Import numpy as np and print the version number. (5 Points)
2. Create a 1D array of numbers from 0 to 9. Desired output:
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])(10 Points)
3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)
4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)
5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
Input:
np.random.seed(100)
a = np.random.uniform(1,50, 20)
(20 Points)
'''
#1
import numpy as np
print(np.__version__)
#2
two = np.arange(10)
print(two)
#3
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
dtypes = [float, float,  float, float, 'U15']
data = np.genfromtxt(url, delimiter=',', dtype=dtypes)
#4
petalwidth = np.genfromtxt(url, delimiter=',', dtype=float, usecols=3)
position = np.where(petalwidth > 1.0)[0][0]
print(f"row {position} has the first occurrence of a value greater than 1.0 in petalwidth")
#5
np.random.seed(100)
a = np.random.uniform(1,50, 20)
a[a > 30] = 30
a[a < 10] = 10
print(a)





