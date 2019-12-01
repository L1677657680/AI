#
# #1
# print ("hello word")
# for i in range(3):
#     print(i);         #注释
#
#
# #2
# if True:
#     print("yes       ,\
#           I do")  # \为换行
# else:
#     print("not")  # 空格行自动缩进
#
#
# #3
# str = 'abcde'
# print(str)
# print(str[2:-2])  # 正数从前面截取，负数从后面截取
# print(str * 2)
# print(str + "2")
#
#
# #4
# i = 6 + 5
# print(i)
#
#
# #5
# i = 10 // 3  # 向下取整
# print(i)
#
#
# #6
# i = 17 % 3  # 取余数
# print(i)
#
#
# #7
# str = "你好!"
# print(str + "我叫小艾\n很高心见到你")
# print(str + r"我叫小艾\n很高心见到你")
#
#
#
# #8
# list = ["abcde", 12345, 456789, "qwerty"]
# onelist = [789456]
# print(list)
# print(list[0])
# print(list[-1])
# print(list[1: -1])
# print(list[2 - 1])
# print(list + onelist)
#
#
#
# #9
# a=[1,2,3]
# a[0]=9    #列表元素替换
# print(a)
#
#
# #10
# a,b,c=1,2,3
# print(a,end=' ')
# print(b,end=' ')
# print(c,end=' ')    #不换行输出
# print()
#
#
# #11
# a=1.1
# b=int (a)   #数据类型转换
# print(b)
#
#
# #12
# k=2 ** 4  #次幂
# print(k)
#
#
# #13
# input("\n\n按下Enter键后退出")
#
#
# #14
# tuple=('dsf', 143, 'efsf', 517, 191)  #元组,元组元素不能修改
# print(tuple)
#
#
#
# #15
# stu={'z','x','c','z','x','q'}   #集合
# print(stu)
# if 'r' in stu:
#     print('T')
# else:
#     print('F')
# a=2
# if a>2:
#     print("ture")
# elif a<2:
#     print("!!")
# else:
#     print("false")
#
#
# #16
# a= set('zxczxc')
# b= set('zxazxa')
# print(a - b)    #差
# print(a | b)    #并
# print(a & b)    #交
# print(a ^ b)    #不同时存在的元素
#
#
#
# #17
# #字典
# dict = {}
# dict[1]='标题'
# dict[2]='作者'
# tinydict={'名字：' :'滴答',
#           '年限：' :100,
#           '作者：' :'粑粑'}
# print(dict)
# print(dict[1])
# print(dict[2])
# print(tinydict.keys())   #字典的键
# print(tinydict.values())   #字典的值
#
#
# #18
# a=int(input("请输入数字："))
# while a<=6:
#     a += 2
#     b=a
#     print(b)
#     if a>6:
#         a-=3
#         c=a
#         print(c)
#         #break
#     else:
#         a=a*3
#         d=a
#         print(d)
#
#
# #19
# a = [1, 2, 8, 9, 6, 5, 7]
# for i in a:
#     print(i)
#     if i == 6:
#         print("本是渣渣")
#         break
#     else:
#         pass   #空语句
#
#
#
# #20
# i=10/3
# b=10//3
# c=10%3
# print(i)
# print(b)
# print(c)
#
#
# #21
# a = "this is my string"
# k=0
# for i in a:
#     if i != 'g':
#         k+=1
#         print(k)
#
#
# #22
# a = "this is my string"
# k=0
# for i in a:
#     k+=1
# print(k)
#
#
# #23
# print(a.__len__())
# print(len(a))
#
# a= int(sum(range(1,101)))    #求和
# print(a)
#
#
#
# #24
# i = 1
# while i<=5:
#     j = 1
#     while j<=i:
#         print("❤",end='')  #不换行输出
#         j +=1
#     print()
#     i+=1
# a = 4
# while a>=0:
#     b = 1
#     while b<=a:
#         print("❤",end='')
#         b +=1
#     print()
#     a-=1
#
#
# #25
# #函数调用
# #计数面积函数
# def a(b,c):
#     return b*c
# b = 4
# c = 6
# print("面积=",a(b,c))
#
#
#
# #26
# def p(str):
#     print(str)
#     return
# p("阿大撒撒在擦拭")
#
#
# #27
# def q(age,name):
#     print("年龄：",age)
#     print("姓名：",name)
#     return
# q(age=18,name="粑粑")
#
#
#
# #28
# def sum(n,m):
#     l=n+m
#     print("函数内：",l)
#     return n*m
# l=sum(1,2)
# n=3
# m=4
# print("函数外：",sum(n,m),l)
#
#
#
# #29
# class A:
#     def f(self,a,b):
#         return a*b
# a = 3
# b = 5
# x=A()
# print("面积为："+str(x.f(a,b)))
#
# #30
# from numpy import *
# print(eye(4))
#
#
##31
# import numpy as np
# o=np.array([[1,2,3],[3,2,1],[1,2,6],[8,9,7]])    #二维数组，记得有个大的中括号
# print(o)
# print(o.shape)    #计算数组的维度
# x=np.empty([3,3],dtype = int)   #np.empty（【x,y】，类型）创建一个指定矩阵
# print(x)
# z=np.ones(5)
# print(z)
# q=np.ones([3,2],dtype=int)
# print(q)
# w=np.sum([3,1],dtype=int)
# print(w)
# f=(1,2,3)
# a=np.asarray(f)
# print(a)
# g=np.arange(10,200,20)        #从数值范围创建数组
# h=g[2:100:20]
# print(h)
# print(o[1:4])      #从某个索引开始切割
# j=np.array([[1,2,3],
#            [2,3,4]])
# k=np.array([1,2,3.1])
# print((j+k),dict=int)


#32
import numpy as np
a = np.arange(9).reshape(3,3)      #改变数组的形状排列
b = np.arange(9).reshape(3,3)
print(b)
print(a.flatten(order='F'))      #F->按列展开，C->按行展开，A->原顺序,K->按元素大小顺序
print(np.transpose(a))      #翻转矩阵
print('按axis连接：')
print(np.concatenate((a,b),axis=0))       #连接两个相同队列矩阵，axis=？->按？拼接
c=np.array([0,30,45,60,90])
print(np.tan(c*np.pi/180))      #三角函数
d=np.array([1.021,5.956,122.499])
print('四舍五入：')
print(np.around(d))
print(np.around(d,decimals=3))       #取小数位的个数值
print(np.around(d,decimals=-2))      #-1:取整十，-2：取整百
print('数组相加=',np.divide(a,b))       #两个数组相除
print('数组相减=',np.multiply(a,b))      #两个数组相乘
print('数组相除=',np.subtract(a,b))      #两个数组相减
print('数组相乘=',np.multiply(a,b))      #两个数组相加
print(a)
print('中位数查询：',np.median(a))
print('沿axis=？输出数组中位数：',np.nanmedian(a,axis=1))