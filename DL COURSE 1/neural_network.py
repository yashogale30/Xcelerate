import numpy as np
import copy
params = {}
def initialize_parameters(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for i in range(1,L):
        parameters['W'+str(i)] = np.random.randn(layers_dims[i], layers_dims[i-1]) * 0.01
        parameters['b'+str(i)] = np.zeros((layers_dims[i],1))
    return parameters

def linear_forward(A_prev,W,b):
    Z = np.dot(W,A_prev)+b
    cache = (A_prev,W,b)
    return Z, cache

def linear_activation_forward(A_prev,W,b, activation):
    Z, linear_cache = linear_forward(A_prev,W,b)
    if(activation == "sigmoid"):
        A = 1/(1+np.exp(-Z))
        activation_cache = Z
    elif(activation == "relu"):
        A = np.maximum(0,Z)
        activation_cache = Z
    elif(activation == "tanh"):
        A = np.tanh(Z)
        activation_cache = Z
    elif(activation == "leaky_relu"):
        A = np.maximum(0.01*Z,Z)
        activation_cache = Z
    cache = (linear_cache,activation_cache)
    return A, cache

def forward_prop(X, parameters):
    caches = []
    A = X
    L = len(parameters)//2
    
    for i in range(1,L):
        A_prev = A
        W = parameters['W'+str(i)]
        b = parameters['b'+str(i)]
        A, cache = linear_activation_forward(A_prev, W, b, "relu")
        caches.append(cache)
    
    W = parameters['W'+str(L)]
    b = parameters['b'+str(L)]
    AL, cache = linear_activation_forward(A,W,b,"sigmoid")
    caches.append(cache)
    
    return AL, caches

def compute_cost(A,Y):
    m = Y.shape[1]
    cost = -np.sum(np.multiply(Y,np.log(A))+np.multiply(1-Y,np.log(1-A)))/m
    cost = np.squeeze(cost)
    return cost


def linear_backwards(dZ, cache):
    A_prev,W,b = cache
    m = A_prev.shape[1]
    
    dW =  np.dot(dZ,A_prev.T)/m
    db = np.sum(dZ, axis = 1, keepdims=True)/m
    dA_prev = np.dot(W.T, dZ)
    
    return dA_prev,dW,db

def linear_activation_backwards(dA, cache, activation):
    m = len(cache)
    linear_cache, activation_cache = cache
    if(activation == "sigmoid"):
        Z = activation_cache
        s = 1 / (1 + np.exp(-Z))
        dZ = dA * s * (1 - s)
        dA_prev, dW, db = linear_backwards(dZ, linear_cache)
    if(activation == "relu"):
        dZ = np.array(dA, copy=True)
        dZ[activation_cache <= 0] = 0
        dA_prev, dW, db = linear_backwards(dZ, linear_cache)
    if(activation == "leaky_relu"):
        dZ = np.array(dA, copy=True)
        dZ[activation_cache < 0] *= 0.01
        dA_prev, dW, db = linear_backwards(dZ, linear_cache)
    if(activation == "tanh"):
        dZ = dA * (1 - np.power(np.tanh(activation_cache), 2))
        dA_prev, dW, db = linear_backwards(dZ, linear_cache)
    return dA_prev, dW, db

def backwards_prop(AL,Y,caches):
    grads = {}
    L = len(caches)
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)
    dAL = -(np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = caches[-1]
    dA_prev, dW, db = linear_activation_backwards(dAL,current_cache,"sigmoid")
    grads["dA" + str(L-1)] = dA_prev
    grads["dW" + str(L)] = dW
    grads["db" + str(L)] = db
    
    for i in range(L-2,-1,-1):
        current_cache = caches[i]
        dA_prev, dW, db = linear_activation_backwards(dA_prev, current_cache,"relu")
        grads["dA" + str(i)] = dA_prev
        grads["dW" + str(i+1)] = dW
        grads["db" + str(i+1)] = db
    
    return grads

def update_parameters(parameters,grads, learning_rate):
    params = copy.deepcopy(parameters)
    L = len(params) // 2
    
    for l in range(1,L+1):
        params['W'+str(l)] = params['W'+str(l)] - (learning_rate*grads['dW'+str(l)])
        params['b'+str(l)] = params['b'+str(l)] - (learning_rate*grads['db'+str(l)])
    
    return params

def nn_train(X,Y,layers_dimensions,num_iterations = 1000, learning_rate = 0.01, print_cost = False):
    global params
    params = initialize_parameters(layers_dimensions)
    for i in range(num_iterations):
        AL, caches = forward_prop(X,params)
        cost = compute_cost(AL,Y)
        if((i+1)%100 == 0):
            if(print_cost):
                print(f"cost after {i+1}th iteration is : {cost}")
        grads = backwards_prop(AL,Y,caches)
        params = update_parameters(params,grads,learning_rate)
        return params,grads
        
def nn_predict(X_test):
    Y_predicted,caches = forward_prop(X_test,params)
    return Y_predicted
    
        
    

