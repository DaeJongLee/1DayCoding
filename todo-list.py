#todo list 
# CRUD 
todo_list= ["list1", "list2", "list3", ]

def print_divider(style):
    if style == 1:
        print("--------------------------")
    elif style == 2: 
        print("==========================")
#Read the todo list 
def read_todo_list(todo_list):
    print_divider(2)
    print(f"Todo list \n")
    for i in range(len(todo_list)):
        print(f"list {i+1} :: {todo_list[i]}.\n")
    print_divider(2)
#Create the todo list
def create_todo_list(todo_list):
    read_todo_list(todo_list)
    todo_list.append(input("What is new to-do list? : "))
    print_divider(1)
    read_todo_list(todo_list)

#update the todo list
def Update_todo_list(todo_list):
    read_todo_list(todo_list)
    mod_input_number =int(input(f"This is Update menu please give the number of list:" ))-1
    def choose_mod_list(todo_list):
        if 0<= mod_input_number < len(todo_list):
            print(f"the number is {mod_input_number+1}, and the to-do is  {todo_list[mod_input_number]}")
            print_divider(1)
        else:    
            print("please return again the number")
            choose_mod_list(todo_list)
    choose_mod_list(todo_list)
    modified_by= input ("what do you want to change the list  : ")  
    todo_list[mod_input_number]=f"{modified_by}"
    print(f"{mod_input_number+1}th todo is modiffy of {todo_list[mod_input_number]}.")
    print_divider(1)
    read_todo_list(todo_list)
#delete the todo list
def del_todo_list(todo_list):
    read_todo_list(todo_list)
    
    def choose_del_list(todo_list):
        while True:
    
            del_input_number = int(input("please choose the number "))-1
    
            if 0<= del_input_number < len(todo_list):
                return del_input_number
    
            else :
                print(f"Invalid number. Please choose a nother between 1 and {len(todo_list)}")
    
    def delete_perform(todo_list, del_input_number):
    
        print(todo_list[del_input_number])
        del_confirm = input("Do you want to delete this to-do list? (y/n) : ")
    
        if del_confirm == "y":
            del todo_list[del_input_number]
            read_todo_list(todo_list)
 
        elif del_confirm == "n":
            print("delete canceled")
            read_todo_list(todo_list)
 
        else :
            print("Please Answer y or n ")
            delete_perform(todo_list,del_input_number)
    
    del_input_number = choose_del_list(todo_list)
    delete_perform(todo_list,del_input_number)

def main(todo_list):
    choose_mode = input(f"""
                Choose your work
                COMMAND:
                        {print_divider(1)}
                C. create the list
                R. read the list 
                U. Update the list 
                D. delete the list 
                Q. quit
                """)
    print_divider(2)    
    
    if choose_mode == "c":
        create_todo_list(todo_list)
        main(todo_list)
    elif choose_mode == "r":                 
        read_todo_list(todo_list)
        main(todo_list)
    elif choose_mode == "u":                 
        Update_todo_list(todo_list)
        main(todo_list)
    elif choose_mode == "d":                 
        del_todo_list(todo_list)
        main(todo_list)
    elif choose_mode == "q":
        pass
    else :
        print("please input the correct command")
        main(todo_list)

main(todo_list)        
