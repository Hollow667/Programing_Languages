## Lists are collections of items
names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # Collections are Zero-indexed

## Arrays are also collections of items
# all items must have the same datatype
from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

## ommon operation on lists are arrays
names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0,'Bill')  # Insert before index
print(names)
names.sort()
print(names)

## Retriving ranges
names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
# Start and end index

print(names)
print(presenters)

## Dictinaries
# key : value
person = { 'first' : 'Christopher' }
person['last'] = 'Harrison'
print(person)
print(person['first'])
