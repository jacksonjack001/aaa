# xiaozhao-bishi-test

#### Description
校招笔试题，leetcode刷题


#### Instructions

1. 冒泡排序<br>
前进后退不交叉<br>
后小互换改标签<br>
一轮未变已排完<br>
```python
def bubble(self, arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(n - i):
            if self.compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

2. 快速排序<br>
首小末时有递归<br>
第一键值为标准<br>
两标相等才能停<br>
找时分清前后标<br>
先到后小换前值<br>
再到前大换后值<br>
```python
def quicksort(a,s,e):
    tmp=a[s]
    i=s;j=e
    if i>=j:
        return
    while i!=j:
        while (i<j)&(a[j]>=tmp):
            j-=1
        while (i<j)&(a[i]<=tmp):
            i+=1
        t=a[i];a[i]=a[j];a[j]=t
    a[s]=a[j];a[j]=tmp;
    quicksort(a,s,j-1)
    quicksort(a,j+1,e)


a=[6,8,7,9,0,1,3,2,4,5]
quicksort(a,0,len(a)-1)
print a
```
3. 直接插入排序<br>
默认首键有序区<br>
每次倒着插回去<br>
大值移后标向前<br>
到小后放当前值<br>
4. 折半插排序<br>
无首有末开始比<br>
不撞南墙不回头<br>
遇大后移遇小插<br>
```python
a='2,3,10,15,20,25,28,29,30,35,40'
A=map(int, a.split(','))
N=len(A)
def findBi(a, v):
    # a
    low=0
    high=len(a)-1

    while(low<=high):
        mid = (low + high) / 2
        if a[mid]==v:
            return mid+1
        elif a[mid]>v:
            flag=1
            high=mid-1
        else:
            flag=2
            low=mid+1
    # if mid==len(a)-1:
    #     mid=len(a)
    if flag==1:
        mid=mid
    else:
        mid=mid+1
    return mid
index=findBi(A,25)
print index
A.insert(index,1000)
```

5. 折半查找<br>
高低确认选中间<br>
成功返回中后标<br>
大，高->中前<br>
小，低->返中后<br>
```python
a='2,3,10,15,20,25,28,29,30,35,40'
a='2,2,2,2,2,2,3,3,3'
A=map(int, a.split(','))
N=len(A)
def findBi(a, v):
    # a
    low=0
    end=len(a)-1
    high=end
    #如果错在中间，那么比的两个值一定连续比如6,7，mid=6
    #如果mid值大于key，7->5,这样变成6,5跳出循环
    #如果mid值小于key，6->7，这样变成7,7，还需要一下轮循环
    #如果恰好相等，或者还是小于，那么输出后面一个8
    #否则大于，那么输出当前值7  mid+=1
            return mid+1
        elif a[mid]>v:
            flag=1
            high=mid-1
        else:
            flag=2
            low=mid+1
    if flag==1:
        mid=mid
    else:
        mid=mid+1
    return mid
index=findBi(A,3)
print index
A.insert(index,1000)
print A
```


5. Dijkstra<br>
```c++
#include <iostream>
#include <cstring>
using namespace std;
const int maxInf = 1000;
//Dijkstra算法：
//1. 不会因为负边的出现而更新已经计算过的顶点的路径长度！
//   如果路径长度有负数，算法无法进行：考虑有三个顶点，三条边：(1,2,1),(1,3,2),(2,3,-3)，
//   最终计算出的路径长度是(1,2,1),(1,3,-2)，但明显存在(1,2,-1)这条更短的路径。
int main() {
  int N = 7;
  int a[12][3] = {{0, 1, 4}, {0, 2, 6}, {0, 3, 6}, {1, 2, 1}, {1, 4, 7}, {2, 4, 6},
                  {2, 5, 4}, {3, 2, 2}, {3, 5, 5}, {4, 6, 6}, {5, 4, 1}, {5, 6, 8}
  };
  int A[N][N];
  int S[N], D[N], P[N];
  memset(A, -1, sizeof(A));
  memset(S, 0, sizeof(S));  S[0] = 1;
  //注意memset在初始化int类型时只能初始化为0和-1！！
  for(int i=0;i<N;i++)D[i]=maxInf;  D[0] = 0;
  memset(P, -1, sizeof(P));  P[0] = 0;
  for (int i = 0; i < 12; i++) {
    A[a[i][0]][a[i][1]] = a[i][2];
  }
  int v, u, ut, temp = maxInf;
  v = 0;//首轮更新单独做一次！！
  for (int i = v + 1; i < N; i++) {
    if (A[v][i] > 0) {
      P[i] = v;
      D[i] = A[v][i];
      if (A[v][i] < temp) {
        temp = A[v][i];
        u = i;
      }
    }
  }
  S[u] = 1;//确定入伙人身份
  int n = N - 2;
  while (n > 0) {
    for (int i = 0; i < N; i++) {
        //刚入伙人的作用就是招揽新人
        //首先人要‘干净’，再者介绍费比boss直聘要少
        if (A[u][i] > 0 && S[i] == 0 && D[u] + A[u][i] < D[i]) {
          D[i] = D[u] + A[u][i];
          P[i] = u;
        }
    }
    temp = maxInf;
    for(int i=0;i<N;i++){
      if (S[i]==0 && D[i] < temp) {
        temp = D[i];
        ut = i;
      }
    }
    u = ut;
    S[u] = 1;
    n = n - 1;
  }
  //输出结果
  int t;
  for(int i=1;i<N;i++){
    cout<<i<<": "<<D[i]<<":->"<<i<<",";
    t=P[i];
    while(t!=v){
      cout<<t<<",";
      t=P[t];
    }
    cout<<v<<endl;
  }
  return 0;
};
```

# HashTbale作用，映射机制非常重要
```python
string1='5 2 3 1 5 6'
string2='12 2 2 4 1 5 5 6 3 1 1 5 6'
A1=map(int, string1.split(' '))
A2=map(int, string2.split(' '))

#N^2
A=[]
for i in range(1,len(A2)):
    temp=A2[i]
    for j in range(1,len(A1)):
        if temp==A1[j]:
            A+=[j]
print A

#HashTable N
A=[]
Hashtable=[-1 for i in range(max(A2))]
for j in range(1, len(A1)):
    Hashtable[A1[j]]=j
for i in range(1, len(A2)):
    if Hashtable[A2[i]]>-1:
        A+=[Hashtable[A2[i]]]
print A
```

6. 栈<br>
注意是将最有用的信息存到栈中，比如标号，因为值只有()两种，存入栈中肯定没有意义。<br>
出栈时的条件以及状态：<br>
	1. 能够出栈那么一定会有匹配；(()())，()(),等等.每一次出栈只要和停留的栈首元素比较下距离就可以得到长度
	2. 需要注意的是当栈为空的时候就没办法比较，所以需要单独判断！！
```python
def longestValidParentheses1(s):
    j = len(s)
    maxlen = 0
    stack = []
    for i in range(j):
	#适合弹出的条件非常重要
        if s[i] == ')' and len(stack) != 0 and s[stack[-1]] == '(':
            a = stack.pop()
            if len(stack) == 0:
		#一旦有卡死的地方，沉寂在栈中再也出不来了,所以很少执行，除非说从头到尾都没有死穴
                maxlen = i + 1
            else:
		#一般的情况下，按照匹配规则，适合弹出的时候中间的序列一定是匹配的！
                maxlen = max(maxlen, i - stack[-1])

        else:
            stack.append(i)
    return maxlen
def longestValidParentheses2(s):
    tl = len(s)
    stack = []
    st = 0
    maxlen = 0
    for i in range(tl):
        if s[i] == '(':
            stack.append(i)
        else:
            #遇到右括号，但是没有元素那么直接跳过
            if len(stack) == 0:
                st = i + 1
                continue
            #有元素那么一定至少有一个左括号
            else:
                a = stack.pop()
                if len(stack) == 0:
                    maxlen = max(i - st + 1, maxlen)
                else:
                    maxlen = max(i - stack[-1], maxlen)
    return maxlen

str1='())(()())'
print longestValidParentheses1(str1)
```


7. 并查集


8. 深度优先搜索


9. 01背包问题
```python
# -- coding: utf-8 --
# 01背包问题
# w=[2,2,6,5,4]
# c=[6,3,5,4,6]
# t=10
# 完全背包问题
w=[3,2,6,5,4]
c=[6,3,5,4,7]
t=10
#dfgs sdfg
n=len(w)
# S=[[0]*(t+1)]*(n+1)
S=[[0]*(t+1) for i in range(n+1)]
L=[0]*(n+1)
B=[0]*(n+1)
for i in range(1,n+1):
    wt=w[i-1]
    tj=0
    if i == 2:
        1
    for jt in range(1, t + 1):
        S[i][jt] = S[i - 1][jt]

    for j in range(1,t+1):
        #不足以放入那么不处理
        K=j/wt+1
        # K=1+1
        for k in range(1,K):
            if j<k*wt:
                1
            else:
            #一层只有可能一次跳跃
                # S[i][j]=max(S[i][j], S[i-1][j-wt]+c[i-1])
                if S[i][j]<S[i-1][j-k*wt]+k*c[i-1]:
                    S[i][j] =  S[i - 1][j - k*wt] + k*c[i - 1]
    #对最早或者最晚加入背包的位置进行尝试记录是无效的！！！
for i in range(len(S)):
    print S[i]

# ti=t
# for i in range(n,0,-1):
#     if S[i][ti]>S[i-1][ti]:
#         B[i]=1
#         ti=ti-w[i-1]
ti=t
for i in range(n,0,-1):
    K=ti/w[i-1]+1
    # K=1+1
    if S[i][ti]>S[i-1][ti]:
        for k in range(1,K):
            tk = ti - k * w[i - 1]
            if S[i][tk]==S[i-1][tk]:
                B[i]=k
                ti=tk
                break


print S[n][t]
print B
```

