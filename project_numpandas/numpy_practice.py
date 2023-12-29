import numpy as np
import matplotlib.pyplot as plt

def vector_1d_np():
    np_list_int=np.array([0,1,2,3])
    np_list_float=np.array([0.,1,2,3,5])
    print(f"NumPy version: {np.__version__}'\n'")

    print(f"Numpy list first index np_list_int[0]: {np_list_int[1]}")
    print(f"Numpy list type(variable): {type(np_list_int)}")
    print(f"Numpy list data type variable.dtype: {np_list_int.dtype}")
    print(f"Numpy list elements in array with variable.size attribute: {np_list_int.size}")
    print(f"Numpy list number of variable.ndim attribute: {np_list_int.ndim}")
    print(f"Numpy list float data type variable.dtype attribute: {np_list_float.dtype}")

    np_list_float[0]=100
    print(f"Change Numpy list float first element with variable[0]=100 {np_list_float}")

    np_list_float[2:4]=300,400
    print(f"Change Numpy list float indices 2,3 to 300, 400 variable[2:4]=300,400 {np_list_float}\n")

    ##Vector Addition/Subtraction
    u=np.array([1,0])
    v=np.array([0,1])
    z=np.add(u,v)
    x=np.subtract(u,v)
    w=np.multiply(u,v)
    y=np.divide(u,v)
    print(f"Vector addition z=u+v: {z}")
    print(f"Vector subtraction x=u-v: {x}")
    print(f"Vector multiplication w=np.multiply(u,v): {w}")

    ##Vector Multiplication with Scalar
    v_mul=np.array([1,2])
    z_mul=v_mul*2
    print(f"Vector multiplication is answer=vector*scalar in this case 2: {z_mul}")

    ##Product of two vectors with Hadamard Product, Used to enhance, supress, mask image regions
    u_had=np.array([1,2])
    v_had=np.array([3,2])
    z_had=u_had*v_had
    print(f"Product using Hadamard Product with two vectors, answer=vector*vector: {z_had}\n")

    ##Dot Product of two vectors, Represents how similar vectors are
    u_vect=np.array([1,2])
    v_vect=np.array([3,2])
    z_prod=np.dot(u_vect,v_vect)
    print(f"Dot Product of two vectors is answer=np.dot(vect1,vect2): {z_prod}\n")

    ##Adding Constants to Numpy Array aka Broadcasting
    u_const=np.array([1,2,3,-1])
    z_const=u_const+1
    print(f"Adding constant 1 to vector 1,2,3,-1: {z_const}\n")

    ##Min,Max, Mean, Standard Deviation, Pi, Sin (Calculate unknown angle or side of triangle)
    test_array=np.array([1,3,5,7])
    print(f"The variable.max() method will display max: {test_array.max()}")
    print(f"The variable.min() method will display min: {test_array.min()}")
    print(f"The variable.mean() method will display the mean: {test_array.mean()}")
    print(f"Standard deviation is variable.std(): {test_array.std()}")
    print(f"pi is np.pi: {np.pi}")
    print(f"np.sin\n")

    ##Linespace returns evenly spaced numbers over specified intervals
    test_array_a=np.linspace(-2,2,num=4) #Begin, End, Number of Samples
    print(f"The variable=np.linespace(-2,2,num=4) will begin with -2, end with 2, and provide 4 numbers: {test_array_a}")

    ##Plot Math functions
    x_new=np.linspace(0,2*np.pi,100)
    y_new=np.sin(x_new)
    plt.plot(x_new,y_new)


##Iterating 1D Array
def array_iterate():
    array_iterate=np.array([1,2,3])
    print(f"Iterate over array by printing array: {array_iterate}")
    print("To print as list use for loop: for i in array: print i: ")
    for i in array_iterate:
        print(i)

def array_2d():
    alist=[[11,12,13],
           [21,22,23],
           [31,32,33]]
    blist=[[41,42,43],
           [51,52,53],
           [61,62,63]]
    aarray=np.array(alist)
    barray=np.array(blist)
    bscalar=2*barray
    print(f"variable=np.array(list): \n{aarray}")
    print(f"Number of dimensions, ranks, number of nested lists: variable.ndim: {aarray.ndim}")
    print(f"Shape is rows, columns: variable.shape: {aarray.shape}")
    print(f"Size is elements: variable.size: {aarray.size}")
    print(f"Accessing row/index 0, column/index 0 is variable[0][0]: {aarray[0][0]}")
    print(f"Accessing row/index 2, column/index 2 is variable[1][1]: {aarray[1][1]}")
    print(f"Splicing row index, columns up to index 2 variable[0:0:2]: {aarray[0,0:2]}")
    print(f"Splicing row index, columns up to index 1 variable[1:0:1]: {aarray[1,0:1]}")
    print(f"Splicing row index up to 2, column index 2: variable[0:2,2]: {aarray[0:2,2]}")
    print(f"Scalar multiplication using 2*array=answer: \n{bscalar}")
    
def matrix_2d():
    amatrix=[[1,0],
             [0,1]]
    bmatrix=[[2,1],
             [1,2]]
    cmatrix=np.matmul(amatrix,bmatrix)

    print(f"Multiplying first matrix * second matrix using answer=np.matmul(first,second): {cmatrix}")
    print(f"")

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

a=np.array([-1,1])
b=np.array([1,1])

#vector_1d_np()
#Plotvec2(a,b)
#array_iterate()
array_2d()
#matrix_2d()