#coding:UTF8
'''
Created on 2016年9月14日

@author: YR
'''
#  {(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)}

# node{
#    node left:        左子树
#    node right:        右子树
#    string split:        基于哪个维度切分
#      data:            矢量
#    node   parent:    父节点
# }
import matplotlib.pyplot as plt

class Node:
    def __init__(self,data = None, split = None, left = None, right = None):
        self.data = data
        self.split = split
        self.left = left
        self.right = right

class KDTree:
    '''
    pointList = ((2,3),(5,4),(9,6),(4,7),(8,1),(7,2))
    '''
    def __init__(self,pointList = None):    
        self.pointList = pointList
    
    def createKDTree(self,pointList,boundary):
        pointNum = len(pointList)
        if pointNum == 0:  
            return
        #维度
        dimension = len(pointList[0])
        maxVari = -1
        split = -1
        for i in range(dimension):
            component = []
            for point in pointList:
                component.append(point[i])
            variance  = self.computeVariance(component)
            if variance > maxVari:
                maxVari = variance
                split = i
        pointList.sort(key = lambda p : p[split])#lambda函数
        root = Node(pointList[pointNum / 2],split)
        
        self.drawLine(pointList[pointNum / 2],split,boundary)
        rcBound = boundary[:]
        lcBound = boundary[:]
        if split:
            lcBound[3] = pointList[pointNum / 2][split]
            rcBound[2] = pointList[pointNum / 2][split]
        else:
            lcBound[1] = pointList[pointNum / 2][split]
            rcBound[0] = pointList[pointNum / 2][split]
        root.left = self.createKDTree(pointList[0:(pointNum / 2)],lcBound)
        root.right = self.createKDTree(pointList[(pointNum / 2) + 1:pointNum],rcBound)    

        return root
    def computeVariance(self,numList):
        #E([X-E(X)]^2)
        pass
        floatList = [float(x) for x in numList]
        length = len(floatList)
        sumT = 0
        #求期望值
        for f in floatList:
            sumT += f
        EX = sumT / length
        #平方和
        squareSum = 0
        for f in floatList:
            squareSum += (f-EX) * (f-EX)
        variance = squareSum / length
        
        return variance
    def drawLine(self,point,split,boundary):
        '''
                划线方法，参数boundary是当前矩形的四条边界
                boundary[0]=>xLeft,boundary[1]=>xRight,
                boundary[2]=>yLeft,boundary[3]=>yRight,
        '''
        if split:
            plt.plot([boundary[0],boundary[1]],[point[split],point[split]])
        else:
            plt.plot([point[split],point[split]],[boundary[2],boundary[3]])
        
    def drawPoint(self,pointList):
        gx = lambda p:p[0]
        gy = lambda p:p[1]
        x = [gx(p) for p in pointList]
        y = [gy(p) for p in pointList] 
        plt.plot(x,y,"o")
        
if __name__ == "__main__":

    testList = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
    tree = KDTree()
    tree.drawPoint(testList)
    root = tree.createKDTree(testList,[0,10,0,10])
    plt.show()
        
        
        
        
        
        
        