def quicksort(a,s,e):
    tmp=a[0]
    i=s;j=e
    while(i<j):
        if(i<j&a[j]>tmp):
            j-=1                
        if(i<j&a[i<tmp):
            i+=1
        t=a[i];a[i]=a[j];a[j]=t
    a[0]=a[j];a[j]=tmp;
    quicksort(a,s,t-1)
    quicksort(a,t+1,e)    