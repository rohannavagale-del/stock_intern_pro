import numpy as np
# a = np.array([[1,2,3,4,5,6,7], [8, 9, 10,11, 12,13,14]])
# # print(a)
# # get a spcific element
# # print(a[1,4])

# # get a specific row 
# # print(a[0 , :])

# #  get a specific column
# print(a[: , 1])

# # [starting index : ending index : step size]
# print(a[0,1 : 7 : 2])

# # a[1,3] = 16
# # print(a)

# 3D DIMENION array:

# a = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# # print(a)
# a[:,1,:] = [[9,9]]
# print(a)

# DIFFERENRT TYPE OF ARRAY :



# a = np.array([[1,2,3],[4,5,6],[7,1,0]])

# print(a.sum(axis=0))---- for axising

# print(a.flat)
# for item in a.flat: --- for printing no in line wise
#     print(item)

# print(a.ndim) --- No of dimension

# print(a.size) -- show the size of array

# print(a.nbytes) -- no bytes (so we have 9 number in array and 1 byte = 8 bites.. so 9*8 =72)

# one = np.array([1,3,45,8]) 
# print(one.argmax()) --- show at which idx we have our max element
# print(one.argmin()) --- show at which idx we have our min element
# print(one.argsort()) ---  sort the idx in accesinding



# # print(a[:,1])
# print(a.dtype)
# print(a.shape)
# print(a.size)
# a = np.identity(45)

# print(a)
# print(a.shape)

# a = np.array([0,1,2,3,4,5,6,7,8,9])
# print(np.arange(0,10,2))

# print(np.zeros((2,10)))

# print(np.full((10 , 3),6))

# list = [1,2,3,4] --- list to numpy:
# a = np.array(list)
# print(a)
# print(type(a))

# np1 = np.array([1,2,3,4,5,6,7,8,9]) --- SLICING
# print(np1[1:5])
# print(np1[3:])
# print(np1[-3:-1])
# print(np1[1:10:2])

# np1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(np1[0,1:3])
# # print(np1[1,1:3])
# print(np1[0:2 , 1:3])


# trig cos ,sin , log
# np1 = np.array([-1,-2,-3,0,1,2,3,4,5,6,7,8,9])
# print(np.sin(np1))


# COPY VS VIEW
# view
# np1 = np.array([0,1,2,3,4])
# np2 = np1.view()

# print(f"original NP1 {np1}")
# print(f"original NP2 {np2}")

# np1[0] = 41
# print(f'changed NP1 {np1}')
# print(f'changed NP2 {np2}')

# copy
# np1 = np.array([0,1,2,3,4])
# np2 = np1.copy()

# print(f"original NP1 {np1}")
# print(f"original NP2 {np2}")

# np1[0] = 41
# print(f'changed NP1 {np1}')
# print(f'changed NP2 {np2}')

# SHAPE & RESHAPE:

# np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np1)

# np2 = np1.reshape(4,3) -- 2D
# print(np2)
# print(np2.shape)

# np3 = np1.reshape(2,3,2) -- 3D
# print(np3)
# print(np3.shape)

# np4 = np3.reshape(-1) --- back to 1D
# print(np4)
# print(np4.shape)

# ITERATING :

# np1 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# for x in np1:
#     # print(np1)
#     for y in x:
#         # print(y)
#         for z in y:
#             print(z)

# for x in np.nditer(np1): -- iteration method
#     print(x)
    
# np1 = np.array([1,2,3,4,5,6,3,2])
# x = np.where(np1==3)
# print(x[0])

# x = np.where(np1 % 2 ==0) -- returns even value
# print(x[0])
# print(np1[x[0]])

# x = np.where(np1 % 2 !=0)-- return the odd value
# print(x[0])
# print(np1[x[0]])

# FILTERING

np1 = np.array([1,2,3,4,5,6,7,8,9])
# filtered= []
# for things in np1:
#     if things % 2 == 0:
#         filtered.append(True)

#     else:
#         filtered.append(False)

# print(np1)
# print(filtered)
# print(np1[filtered])

# shortcut 
filtered = np1 % 2 == 0
print(np1)
print(filtered)
print(np1[filtered])