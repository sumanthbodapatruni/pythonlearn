heights=[23,56,76,67]
print(heights[0])      # same as strings
names= ['satya','sai','sumanth']
print(names[0])

mix=['satya',22,]       # possible with str and int together
heights[0]= 24          # can change value
print(heights[0])

add=[names,heights]
print(add)

heights.append(45)      # adds 45 at end
print(heights)

heights.insert(0,20)    # inserts at position
print(heights)

heights.remove(20)      # removes the given number..if not in the lists - error
print(heights)

heights.pop()           # removes the  last element
print(heights)

heights.pop(0)          # removes accc to index number
print(heights)

del heights[0:2]        # deletes from 0 to 1
print(heights)

heights.extend([45,67,98,34])
print(heights)

print(min(heights))

print(max(heights))

print(sum(heights))

heights.sort()
print(heights)
