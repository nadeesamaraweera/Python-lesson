my_list1 = [10,8,5,6]
my_list2 = [4,3,6,1]

def find_sum(a,b):
    return a + b

sumOfNumbrs = map(find_sum, my_list1, my_list2)
sumOfNumbrs = list(sumOfNumbrs)
print(sumOfNumbrs) #[14, 11, 11, 7]