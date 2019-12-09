#def word_counter(x):
    #String1='I need noise I need buzz of sub a crack of whip and some blood on the cuts'#hangi lyrics i koyicaksaniz buraya yapistirin
    #word=String1.split()
    #count=word.count(x)
    #if count==1:
        #print (str(x) + ' is written ' + str(count) + ' time')
    #else:
        #print (str(x) + ' is written '+ str(count) + ' times')
#word_counter('I');


#def fib(n,d):
    #if n in d:
        #return d[n]
    #else:
        #ans=fib(n-1,d)+fib(n-2,d)
        #ans=d[n]
        #return ans
#print fib(6,5)

#def factorial():
    #fact=1
    #input1 = int(raw_input('Please type an integer:'))
    #while input1==1 or input1==0:
        #return 1
    #else:
        #for i in range(1,input1+1):
            #fact=fact*i
        #return fact

#print factorial()

#def diction():
    #n=int(input('Please type an integer:'))
    #d=dict()
    #for i in range(1,n+1):
        #d[i]=i*i
    #return d
#print diction()

# from timeit import default_timer
#
# beginning  = default_timer()
#
# number = 10 ** 11 #This is function fs component we want to find out.
# a1 = int(number ** 0.5)
# J_in_J = [J for J in range(1 + a1)]
# DVD = [0] * (1 + a1)
#
# for x in range(2, 1 + a1):
#     if x == J_in_J[x]:
#         for y in range(x, 1 + a1, x):
#             J_in_J[y] = J_in_J[y] - J_in_J[y] // x
#     J_in_J[x] = J_in_J[x] + J_in_J[x - 1]
#
# for d in range(a1, 0, -1):
#     temp_num = number // d
#     R = temp_num * (1 + temp_num) // 2
#     a2 = int(temp_num ** 0.5)
#     a3 = temp_num // (1 + a2)
#     for z in range(1, 1 + a3):
#         R -= (temp_num // z) * (J_in_J[z] - J_in_J[z - 1])
#     for j in range(2, 1 + a2):
#         R -= (DVD[j * d]
#         if j * d<= a1 else J_in_J[temp_num // j])
#     j = 1 + a2
#     R += a2 * J_in_J[temp_num // j]
#     DVD[d] = R
#
# R=0
# c=2
# while c <= number:
#   R += DVD[c] if c <= a1 else J_in_J[number // c]
#   R = R - 1
#
# modu = 7 + 10 ** 9
# print(R)
# print(R % modu)
# print(default_timer() - beginning)

num = 0

for num in range(2000):
    if num % 3 == 0 or num % 5 == 0:
        lis.append(num)
        sumofmult  += num



