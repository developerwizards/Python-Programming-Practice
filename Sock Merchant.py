'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar = [1,2,1,2,1,3,2] . There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Constraints
1<= n <=100
1<= ar[i] <= 100 where 0<= i < n

Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
'''


#My Submission
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    single_list = []
    for i in range(len(ar)):
        if not ar[i] in single_list:
            single_list.append(ar[i])
        else:
            single_list.remove(ar[i])
    #print(single_list)
    return int((len(ar)-len(single_list))/2)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    
    result = sockMerchant(n, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()


''' Alternative Solutions '''
'''Using Conter'''
''' 
from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0

for x in c:
    ans += c[x] // 2
    
print(ans)
'''

'''using hashmap/dictionary'''
'''
n = int(input())
temp = input().split(' ')
graph = {}
for item in temp:
    graph[item] = 0
for item in temp:
    graph[item] += 1
count = 0
for item in graph:
    count += int(graph[item]/2)
print(count)
'''



