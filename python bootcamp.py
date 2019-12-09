##STRINGS
message = 'Hello World'
print message
print len(message)#same below
print len('Hello World')#same above
#index starts from 0
print message[0]#first chrachter in the string
print message[10]#second chracter in the string
##string slicing
print message[0:5]#it includes the first letter, but not the fifth one so the output is 'hello'
print message[:5]#same above and also it can be reverse
print message.lower()#its all lower case now
print message.upper()#its all upper case now
print message.count('m')#count method how many times the argument is used on the string there is no m in hello world so the output is 0
print message.count('Hello')#it works on words too
print message.find('H')#it gives the index of the number
print message.find('m')#the output is -1 because there is no m in hello world and it can't find the index
print message.find('Hello')#it works on words too
print message.replace('World','Universe')# it litteraly replaces the argument with other one second one is the replacement
greeting='Hello'
name='Ayca'
print greeting + name#there is no space between them => HelloAyca
print greeting + ' ' + name#Now there is space between => Hello Ayca
print '{} {} welcome'.format(greeting,name)#it gives Hello Ayca welcome, the spaces is importan is must be in this format
#some mini functions doing some cool stuff
fruit='banana'
for char in fruit:
    print char
#---------------------
index=0#at first we set the index to 0
while index<len(fruit):#we want this code to work while index is lower than the length of the fruit so it won't go on 4ver
    letter=fruit[index]#we assign the fruits letters to letter
    print letter
    index=index+1# it will go on until the final index of the fruit
#------------------------
letters='JKQWDR'
subset='ack'
for word in letters:#we use the for loop so that it will be in an alpahabetical order
    print word + subset
#---------------------
#the in operator on string
word='ayca'
print 'a' in word #the outpus it true if the word has the letter 'a' in it
print 'b' in word#output is false if the word does not have the letter 'b' in it

#a little function that does cool stuff again
def check(word1,word2):#this function gives the common letters in two words
    for letter in word1:#if the letter is in word1
        if letter in word2:#also in word2
            print letter
check('elma','armut')#the output is 'm' and 'a'

##LISTS









