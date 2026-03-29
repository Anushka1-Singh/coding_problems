# write a program to find all duplicate elements in an array
arr=[10,20,30,20,40,10,50]
duplicates=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            if arr[i] not in duplicates:
                duplicates.append(arr[i])
print('duplicate elements: ',duplicates)
# dry run
# i=0, j=i+1 => j=1, arr[i]==arr[j]=> arr[0]==arr[1]=> 10==20 => false , skip
# i=0, j=i+2 => j=2, arr[i]==arr[j]=> arr[0]==arr[2]=> 10==30 => false , skip 
# i=0, j=i+3 => j=3, arr[i]==arr[j]=> arr[0]==arr[3]=> 10==20 => false , skip
# i=0, j=i+4 => j=4, arr[i]==arr[j]=> arr[0]==arr[4]=> 10==40 => false , skip
# i=0, j=i+5 => j=5, arr[i]==arr[j]=> arr[0]==arr[5]=> 10==10 => true ,  append => 10
# i=1, j=i+1 => j=2, arr[i]==arr[j]=> arr[1]==arr[2]=> 20==30 => false , skip
# i=1, j=i+2 => j=3, arr[i]==arr[j]=> arr[1]==arr[3]=> 20==20 => true ,  append => 20
# i=2, j=i+1 => j=3, arr[i]==arr[j]=> arr[2]==arr[3]=> 30==20 => false , skip
# i=2, j=i+2 => j=4, arr[i]==arr[j]=> arr[2]==arr[4]=> 30==40 => false , skip
# i=2, j=i+3 => j=5, arr[i]==arr[j]=> arr[2]==arr[5]=> 30==10 => false , skip
# i=2, j=i+4 => j=6, arr[i]==arr[j]=> arr[2]==arr[6]=> 30==50 => false , skip
# i=3, j=i+1 => j=4, arr[i]==arr[j]=> arr[3]==arr[4]=> 20==40 => false , skip
# i=3, j=i+2 => j=5, arr[i]==arr[j]=> arr[3]==arr[5]=> 20==10 => false , skip
# i=3, j=i+3 => j=6, arr[i]==arr[j]=> arr[3]==arr[6]=> 20==50 => false , skip
# i=4, j=i+1 => j=5, arr[i]==arr[j]=> arr[4]==arr[5]=> 40==10 => false , skip
# i=4, j=i+2 => j=6, arr[i]==arr[j]=> arr[4]==arr[6]=> 40==50 => false , skip
# i=5, j=i+1 => j=6, arr[i]==arr[j]=> arr[5]==arr[6]=> 10==50 => false , skip
# i=6 => no j loop (because j starts from i+1 and no elements left)
