'''
Create a CLI application to store a shopping list.  Use cases: 

    User adds item to list (Item may not be blank and may not already be in list)
    User prints sorted item list like 1.) Apple
    User removes item by typing its number
    User saves list to file
    User loads list from file
    Use can exit the program runtime
'''

menuOption = None

mylist = []

menuText = '''
1.) add item
2.) print list
3.) remove item by number
4.) save list to file
5.) load list form file
6.) exit
'''

while menuOption != '6':
    print(menuText)
    menuOption = input('Enter selection\n')
    print(menuOption)
    if menuOption == '1':
        print('add item')
        item = input("name of item: ")
        mylist.append(item)
    elif menuOption == '2':
        print('print list')
        print(mylist)
    elif menuOption == '3':
        print('remove item by number')
        item = input("number of item: ")
        del mylist[(int(item)+1)]

    elif menuOption == '4':
        print('save list to file')
    elif menuOption == '5':
        print('load list form file')
    elif menuOption == '6':
        print('exit')
    else:
        print("not recogonized")
