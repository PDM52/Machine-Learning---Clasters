import math
import random

if __name__ == '__main__':

    file = open('iris_training.txt', 'r')
    data = []
    for line in file.readlines():
        line = line.replace('\n', '')
        data.append(line.replace(' ', '').replace(',', '.').split('\t'))
    file.close()

    k = int(input("Podaj k: "))
    dataLenght = (len(data[0])-1)
    centroids = random.sample(data, k)
    clasters = []

    for i in range(10):
        clastersBuffor = [[] for _ in range(k)]
        totalSum = [0]*k
        for point in data:
            minValue = [-1, 0]
            for ceIdx in range(0, len(centroids)):
                toCompare = [ceIdx, 0]
                for d in range(dataLenght):
                    toCompare[1] += (float(point[d]) - float(centroids[ceIdx][d])) ** 2
                if toCompare[1] < minValue[1] or minValue[0] == -1:
                    minValue = toCompare
            totalSum[minValue[0]] += minValue[1]
            clastersBuffor[minValue[0]].append(point)
        sum = 0
        for w in range(k):
            sum += totalSum[w]
            print("Suma kwadratów odległości dla klastra " + str(w+1)+": " + "{:.2f}".format(totalSum[w]))
        print("Całkowita suma kwadratów odległości " + "{:.2f}".format(sum))
        print("==================================")

        for clIdx in range(len(clastersBuffor)):
            sum = [0]*dataLenght
            for point in clastersBuffor[clIdx]:
                sum = [a + float(b) for a, b in zip(sum, point)]
            centroids[clIdx] = [s / len(clastersBuffor[clIdx]) for s in sum]
        clasters = clastersBuffor

    for i in range(len(clasters)):

        print("Claster " + str(i+1))
        counter = {}

        for point in clasters[i]:
            if not(point[-1] in counter):
                counter[point[-1]] = 1
            else:
                counter[point[-1]] += 1

        entropy = 0.0
        for value in counter:
            print(value + ": " + str(counter[value]))
            p = float(counter[value])/len(clasters[i])
            entropy -= p * math.log2(p)
        print("Entropia: " + "{:.2f}".format(entropy))
        print("==================================")

