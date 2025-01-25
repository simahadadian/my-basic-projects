import random
q=1
z=99
guess=random.randint(q,z)
print(guess)
answer=input('give your idea.if it is larger than yours, type k. if it is smaller than yours, type b. if it is correct, type d: '  )
while answer!='d':
    if answer=='k':
      z=guess-1
      guess=random.randint(q,z)
      print(guess)
      answer=input('give your idea.if it is larger than yours, type k. if it is smaller than yours, type b. if it is correct, type d: '  )
    elif answer=='b': 
      q=guess+1 
      guess= random.randint(q,z)
      print(guess)
      answer=input('give your idea.if it is larger than yours, type k. if it is smaller than yours, type b. if it is correct, type d: '  ) 
print ('done') 


       
