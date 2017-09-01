# ----------------------------------------------------------------------------
# 递归求斐波那契数列
# def digui(n):
	# if n==1:
		# return 1
	# elif n==2:
		# return 1
	# else:
		# return digui(n-2)+digui(n-1)
# print(digui(int(input('n='))))


# --------------------------------------------------------------------------
# 迭代求斐波那契数列
#使用while循环的迭代方法
# def diedai(n):
	# n1=1
	# n2=1
	# n3=1
	# # if n==1:
		# # return 1
	# # elif n==2:
		# # return 1
	# while n>2:
		# n3=n1+n2
		# n1=n2
		# n2=n3
		# n-=1
	# return n3
# print(diedai(int(input('n='))))

#--------------------------------------------------------------------------
# 迭代求斐波那契数列
# 使用for循环的迭代方法
# def diedai(n):
	# n1=1
	# n2=1
	# n3=1
	# # if n==1:
		# # return 1
	# # elif n==2:
		# # return 1
	# if n<1:
		# return -1
	# for i in range(3,n+1):
		# n3=n1+n2
		# n1=n2
		# n2=n3
	# return n3
# result=diedai(int(input('n=')))
# if result>0:
	# print(result)
# else:
	# print('输入数字应该大于0')
	
#------------------------------------------------------------------------
#汉诺塔游戏：使用递归方法将x上的n个盘子全部移动到z
#本程序功能是打印输出
def hanoi(n,x,y,z):
	if n==1:
		print(x,'-->',z)
	else:
		hanoi(n-1,x,z,y)	#将前n-1个盘子从X移动到y上
		print(x,'-->',z)	#将最底下的最后一个盘子从x移动到z上
		hanoi(n-1,y,x,z)	#将y上n-1个盘子从y移动到z上
hanoi(int(input('请输入汉诺塔的层数：')),'x','y','z')

#汉诺塔游戏：使用递归方法将x上的n个盘子全部移动到z
#本程序功能是打印输出
#本程序较上一个程序做有详细标记的
# def hanoi(n,x,y,z):
	# # print(type(x))
	# if n==1:
		# print('n==1时',x,'-->',z,'\n')
	# else:
		# hanoi(n-1,x,z,y)	#将前n-1个盘子从X移动到y上
		# print('执行语句hanoi(%d,%s,%s,%s)'%(n-1,x,z,y))
		
		# print(x,'-->',z)	#将最底下的最后一个盘子从x移动到z上
	
		# hanoi(n-1,y,x,z)	#将y上n-1个盘子从y移动到z上
		# print('执行语句hanoi(%d,%s,%s,%s)'%(n-1,y,x,z))
		
# hanoi(int(input('请输入汉诺塔的层数：')),'x','y','z')