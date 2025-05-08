#!/usr/bin/env python3


#function to put the fibonacci
def print_fibonacci(length):  
    #defining the list
    my_list = [0, 1]
    
    if(length == 0):
        my_list.clear()
        print(my_list)
    elif(length < 3):
        print(my_list[0:length] )
        
    else:
        for i in range(length - 2):
            my_list.append(my_list[-1] + my_list[-2])
        print(my_list)
    
    
print_fibonacci(1)


