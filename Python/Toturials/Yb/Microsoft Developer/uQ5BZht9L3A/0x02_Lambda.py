# Sort alphabetically
def sorter(item):
    return item['name']

presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort(key=sorter)
print(presenters)

# Using lambda
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort(key=lambda item: item['name'])
print(presenters)

# Sort by length (shortest to longest)
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort(key=lambda item: len(item['name']))
print(presenters)
