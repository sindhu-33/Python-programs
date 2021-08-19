#function to set the elements smaller than pivot in front and greater than pivot at back.
def divide(a,l,h):
    i=(l-1) # index of smaller element
    pi=a[h]  # pivot element initialization
    # running a loop from low to high index
    for j in range(l,h):
        # if current element is smaller than or equal to pivot increment index of smaller element
        if(a[j]<=pi):
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return (i+1)
#function to partition the list
def quicksort(a,l,h):
    #base case
    if(len(a)==1):
        return a
    if(l<h):
       #at pi index we have to divide the elements it is partitioning index.
        pi=divide(a,l,h)
        # pi is plaed at correct index partition elements before and after it.
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)
#take input list
a=[int(x) for x in input().split()]
#sorting the elements
quicksort(a,0,len(a)-1)
#printing the sorted elements
for i in range(len(a)):
    print(a[i],end=" ")