def subArraySum(arr, n, sum): 
    for i in range(n): 
        sum1 = arr[i]     
        j = i+1
        while (j<= n):       
            if (sum1 == sum): 
                print((arr[i:j]))               
                return 1               
            if (sum1 > sum or j == n): 
                break          
            sum1 = sum1 + arr[j] 
            j += 1
    print ("None") 
    return 0
arr=eval(input())
k=int(input())
n=len(arr) 
subArraySum(arr,n,k)
