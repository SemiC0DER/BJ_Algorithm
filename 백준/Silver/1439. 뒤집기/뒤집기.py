n = input();

arr1 = n.split('0')
arr2 = n.split('1')

a = len(arr1) -  arr1.count('')
b = len(arr2) - arr2.count('')

print(min(a , b))