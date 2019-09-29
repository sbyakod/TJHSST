#Name: Sharath Byakod
#Date: 5/29/18
#Period: 4

import sys, random, math

def matMul(A, B):
    returnMat = []
    dim1, dim2 = len(A), len(B[0])
    for i in range(dim1):
        temp = []
        for j in range(dim2): temp.append(0)
        returnMat.append(temp)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)): returnMat[i][j] += A[i][k] * B[k][j]
    return returnMat
def applySigmoid(matrix, bool):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): matrix[i][j] = sigmoid(matrix[i][j], derive = bool)
    return matrix
def sigmoid(x, derive=False):
    if derive: return x * (1 - x)
    return 1 / (1 + math.exp(-x))
def getError(A, B):
    returnMat = []
    for i in range(len(A)): returnMat.append([.5 * ((A[i][0]- B[i][0])*(A[i][0]- B[i][0]))])
    return returnMat
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def hProduct(A, B):
    returnMat = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])): temp.append(A[i][j] * B[i][j])
        returnMat.append(temp)
    return returnMat
def scalarTimesMat(scale, mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):  mat[i][j] = scale * mat[i][j]
    return mat
def matMinusMat(A, B):
    returnMat = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])): temp.append(A[i][j] - B[i][j])
        returnMat.append(temp)
    return returnMat

X = [[1, 1, 1],[1, 0, 1],[0, 1, 1],[0, 0, 1]]
y = [[0],[1],[1],[0]]
eta = 3
iterations = 20000   #7.841291803970367e-05
#iterations = 100000  #7.470760722154875e-06
w01 = []
for i in range(3):
    temp = [random.random(), random.random(), random.random()]
    w01.append(temp)
w12 = [[1], [1], [1]]

for iteration in range(iterations):
    z_h = matMul(X, w01) # result after applying the weight matrix to the input
    a_h = applySigmoid(z_h, False) #sigmoid the multiplied weight matrix
    z_o =  matMul(a_h, w12) # final matrix multiplication to the output layer
    a_o = applySigmoid(z_o, False) # sigmoid the final result matrix after the last layer of weights
    a_o_error = getError(a_o, y) # create a 4x1 matrix with the error formula applied
    delta_a_o_error = [] # 4x1 matrix with final matrix output minus the actual output
    for i in range(len(a_o)): delta_a_o_error.append([a_o[i][0] - y[i][0]])
    delta_z_o = applySigmoid(a_o, True) # take the sigmoid deriative of the output layer
    delta_w12 = a_h #sigmoid times initial weight matrix
    delta_output_layer = matMul(transpose(delta_w12),hProduct(delta_a_o_error , delta_z_o)) #backprop to get a matrix that updates the weights on the final layer
    delta_a_h = matMul(hProduct(delta_a_o_error , delta_z_o), transpose(w12))#derivative of error function wrt hiddlen layer
    delta_z_h = applySigmoid(a_h,True) #calculate sigmoid derivative of hidden layer
    delta_w01 = X #derivative of input hidden layer wrt hidden layer weights
    delta_hidden_layer = matMul(transpose(delta_w01), hProduct(delta_a_h , delta_z_h)) # update matrix for hidden layer
    w01 = matMinusMat(w01 , scalarTimesMat(eta , delta_hidden_layer))
    w12 = matMinusMat(w12 , scalarTimesMat(eta , delta_output_layer))
    #actually updaing the matrices
result = applySigmoid(matMul(applySigmoid(matMul(X, w01), False),w12), False)
#print(result)
#print()
print("# of Iterations: " + str(iterations))
print()
print("Weight matrix for hidden layer:")
print(w01)
print()
print("Weight matrix for output layer: ")
print(w12)
print()
error = .5*(result[0][0] * result[0][0]) + .5*(result[3][0] * result[3][0]) + .5*((1-result[1][0]) * (1-result[1][0])) + .5*((1-result[2][0]) * (1-result[2][0]))
print("Error: " + str(error))