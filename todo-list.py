#todo list 
# CRUD 
todo_list= ["list1", "list2", "list3", ]

def lines(type):
    if type == 1:
        print("--------------------------")
    elif type == 2: 
        print("==========================")
#Read the todo list 
def read_todo_list(todo_list):
    lines(2)
    print(f"Todo list \n")
    for i in range(len(todo_list)):
        print(f"list {i+1} :: {todo_list[i]}.\n")
    lines(2)
#Create the todo list
def create_todo_list(todo_list):
    read_todo_list(todo_list)
    todo_list.append(input("What is new to-do list? : "))
    lines(1)
    read_todo_list(todo_list)

#update the todo list
def Update_todo_list(todo_list):
    read_todo_list(todo_list)
    mod_input_number =int(input(f"This is Update menu please give the number of list:" ))-1
    if 0<= mod_input_number < len(todo_list):
        print(f"the number is {mod_input_number+1}, and the to-do is  {todo_list[mod_input_number]}")
        lines(1)
    else:    
        print("please return again the number")
    modified_by= input ("what do you want to change the list  : ")  
    todo_list[mod_input_number]=f"{modified_by}"
    print(f"{mod_input_number+1}th todo is modiffy of {todo_list[mod_input_number]}.")
    lines(1)
    read_todo_list(todo_list)
#delete the todo list
def delete_todo_list(todo_list):
    read_todo_list(todo_list)
    del_input_number =int(input(
        """
    This is delete menu. 
    Please give the to-do number.:""" 
    ))-1

    lines(1)
    print(todo_list[del_input_number])
    del_confirm= input("do you want to delete this to-do? : y/n   ")
    
    if del_confirm == "y":
        del todo_list[del_input_number]
        print(f"#{del_input_number} is terminated .. now the list")
        read_todo_list(todo_list)
     
    elif del_confirm == "n":
        print(f"delete is canceled.")
    else :
        print("ERROR please insert Y or N ")

def main(todo_list):
    choose_mode = input(f"""
                Choose your work
                COMMAND:
                        {lines(1)}
                C. create the list
                R. read the list 
                U. Update the list 
                D. delete the list 
                Q. quit
                """)
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
        delete_todo_list(todo_list)
        main(todo_list)
    elif choose_mode == "q":
        pass
    else :
        print("please input the correct command")
        main(todo_list)

main(todo_list)        
