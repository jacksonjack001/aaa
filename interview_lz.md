# lz 校招笔试面试准备
## 1 网易互娱-数据挖掘岗位

## 2 公交云算法岗位
1. 3Sum
2. 给出一组数字，拼接一个最大的值:
直接的想法是按照字典排序，但面试官立刻给出反例：
98,9   vs  45,4   一看就知道不靠谱
```python
a=[98,9]
a=[12,43,6,9,78,11]
a=map(str,a)
def cmp1(x,y):
    #print x,y
    if x+y>y+x:
        return 1
    elif x+y<y+x:
        return -1
    else:
        return 0
b=sorted(a,lambda x,y: cmp1(x,y),reverse=True)
#bstr=map(str,b)
print ''.join(b)
```
## 3 经典练习


## 面试集锦
1. VIVO推荐算法工程师2019.3.12<br>
https://blog.csdn.net/a1066196847/article/details/86549572
1) MCMC模型是什么？<br>
2）集成学习数学理论？<br>
强可学习：多项式复杂度进行模式识别，错误率按照一定概率可以任意小；
弱可学习：预测结果仅仅比随机猜想效果好；
强弱等价性猜想：只要寻找比随机猜想略好的弱可学习方法，就一定能提升为强可学习。
https://wenku.baidu.com/view/38f340b450e2524de4187e5e.html
3）将n表示成完全平方数的和？<br>
https://blog.csdn.net/qq_35481167/article/details/82817699 欧拉的数学贡献
