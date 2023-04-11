'''
https://www.codingninjas.com/codestudio/problem-details/total-unique-paths_1081470

'''

def my_func(m,n):
	if m == 0 and n == 0:
		return 1
	left = 0
	right = 0 
	if m>0:
		left =  my_func(m-1,n)
	if n>0:
		right = my_func(m,n-1)
	return left + right


def uniquePaths(m, n):
	# Write your code here.
	return my_func(m-1,n-1)