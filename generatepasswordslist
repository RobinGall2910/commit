import itertools
import sys
res = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=2) # this changes the length of password size
with open('passwords.txt', 'w') as passwords_to_txt:
 for i in res: 
  #print >>passwords_to_txt, ''.join(i)
  passwords_to_txt.write(''.join(i) + '\n')
  
