from numpy import *
import operator
from os import listdir
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取训练集到numpy数组
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())      #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1  
    return returnMat,classLabelVector

# 归一化特征值

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

# def img2vector(filename):
#     returnVect = zeros((1,1024))
#     fr = open(filename)
#     for i in range(32):
#         lineStr = fr.readline()
#         for j in range(32):
#             returnVect[0,32*i+j] = int(lineStr[j])
#     return returnVect

fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels=file2matrix("D:\\workspace\\AI\machine_learn\\data\\datingTestSet2.txt")
normMat,ranges,minVals=autoNorm(datingDataMat)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15*array(datingLabels), 15*array(datingLabels))
# ax.axis([-2,25,-0.2,2.0])
plt.xlabel('玩视频游戏所占的百分比')
plt.ylabel('每周消费的冰激凌公升数')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels=file2matrix("D:\\workspace\\AI\machine_learn\\data\\datingTestSet2.txt")

ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15*array(datingLabels), 15*array(datingLabels))
# ax.axis([-2,25,-0.2,2.0])
plt.xlabel('每年获得的飞行常客里程数')
plt.ylabel('玩视频游戏所占的百分比')
plt.show()

