

def readFile(path):
    with open(path,'r') as source:
        source = source.readlines()
        return source



'''
for i in readFile('72.txt'):
    if 'Poslt' in i:
        print(i)
'''

count = 0
def first():
    first = []
    for i in readFile('72.txt'):
        first.append(i)
    second = []
    for x in readFile('101.txt'):
        second.append(x)

    return first, second

first, second = first()

while first:
    for i in first:
        if i in

print(f'celkem je stejných {count} zaznamu')




