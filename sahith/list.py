l1=list(map(int,input("Enter list1 numbers:").strip().split()))
l2=list(map(int,input("Enter list2 numbers:").strip().split()))

print("missing values are:",set(l1).difference(l2))
print("missing values are:",set(l2).difference(l1))
      
