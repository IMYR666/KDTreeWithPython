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
from time import sleep
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
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
        self.colors = ("#00967b","#6aa84f","#c27ba0","#c5b12b","#d11245")
    def createKDTree(self,pointList,boundary,No = 0):
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
        
        self.drawLine(pointList[pointNum / 2],split,boundary,No)
        rcBound = boundary[:]
        lcBound = boundary[:]
        if split:
            lcBound[3] = pointList[pointNum / 2][split]
            rcBound[2] = pointList[pointNum / 2][split]
        else:
            lcBound[1] = pointList[pointNum / 2][split]
            rcBound[0] = pointList[pointNum / 2][split]
        root.left = self.createKDTree(pointList[0:(pointNum / 2)],lcBound,No+1)
        root.right = self.createKDTree(pointList[(pointNum / 2) + 1:pointNum],rcBound,No+1)    

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
    def drawLine(self,point,split,boundary,No = 0):
        '''
                划线方法，参数boundary是当前矩形的四条边界
                boundary[0]=>xLeft,boundary[1]=>xRight,
                boundary[2]=>yLeft,boundary[3]=>yRight,
        '''
        if split:
            plt.plot([boundary[0],boundary[1]],[point[split],point[split]],color = self.colors[No%5])
#             plt.Data("1")
        else:
            plt.plot([point[split],point[split]],[boundary[2],boundary[3]],color = self.colors[No%5])
        #给线上加注释说明
        plt.annotate(No, color = "#00ffff",xy=(point[0], point[1]), xytext=(point[0]+0.2, point[1]+0.2),
            arrowprops=dict(facecolor='#e8d098', shrink=0.005,)
            )
#         ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10, repeat=False) 
    def drawPoint(self,pointList):
        self.initPlot()
        gx = lambda p:p[0]
        gy = lambda p:p[1]
        x = [gx(p) for p in pointList]
        y = [gy(p) for p in pointList] 
        plt.plot(x,y,"o",color = "#be2173")
        
    def initPlot(self):
        fig = plt.figure()
        plt.subplot(111,axisbg="#0c343d")
        plt.title("KDTree")
#         plt.xlabel(u"x轴")
if __name__ == "__main__":

    testList = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2],[8,9],[5,7],[7,7],[9,5]]
    tree = KDTree()
    tree.drawPoint(testList)
    root = tree.createKDTree(testList,[0,10,0,10],1)
    plt.show()
        
        
        
        
        
        
        