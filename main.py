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
4.) save list to "shoppinglist.txt"
5.) load list from "shoppinglist.txt"
6.) exit
'''
while 1:
    num = 1

    while menuOption != '6':
        item = ''
        print(menuText)
        menuOption = input('Enter selection\n')
        #print(menuOption)
    #1 add item
        if menuOption == '1':
            print('\nadd item')
            item = input("name of item: ")
            if item.strip() == '':
                print('item cannot be empty')
            elif item in mylist:
                print('item already in list')
            else:
                mylist.append(str(num) + '.) ' + item)
                num += 1
    #2 print list
        elif menuOption == '2':
            print('\nprint list')
            print(mylist)
    #3 remove item
        elif menuOption == '3':
            print('\nremove item by number')
            item = input("number of item: ")
            if item.strip() == '':
                print('item cannot be empty')
            else:
                del mylist[(int(item)-1)]
    #4 save to file
        elif menuOption == '4':
            print('\nlist saved')
            with open("shoppinglist.txt","a") as out:
                out.write(str(mylist))
            #5 load file  
        elif menuOption == '5':
            print('\nlist loaded')
            #print("operation not implemented yet")
            with open('shoppinglist.txt', 'r') as file:
                mylist = file.read()
    #6 exit
        elif menuOption == '6':
            print('exit')
    #else
        else:
            print("not recogonized")
    break