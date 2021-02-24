
name = "sumanth"
print(name)          # prints sumanth

print(name + ' is clever') # o/p - sumanth is clever

print(name[0])      # prints according to  s  u  m  a  n  t  h  -- s
print(name[1])      #                      0  1  2  3  4  5  6  -- u
print(name[-1])     #                     -7 -6 -5 -4 -3 -2 -1  -- h
print(name[0:2])    # prints 0 to 1
print(name[1:])     # from  1 to end
print(name[:5])     # 0 to 4
print(name[0:7:2])  # 0 to 7 with step of 2
'''name[0]='H'
print(name[0])      # error..strings can't be changed'''

print('H'+name[1:])
print(len(name))    # length of the string

