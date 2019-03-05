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