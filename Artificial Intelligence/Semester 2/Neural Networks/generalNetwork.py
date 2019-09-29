import sys, random, math

class neuralNet:
    def __init__(self, inputnodes, hiddenlayers, outputnodes):
        self.weights = []
        for i in range(len(hiddenlayers)):
            temp = [random.random() for j in range(hiddenlayers[i])]
            weights.append(temp)