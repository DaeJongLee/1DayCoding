#todo list 
# CRUD 

#Read the todo list 
todo_list= ["23", "24", "25", ]
def read_todo_list():
    for i in todo_list:
        print(i)
        pass    

#Create the todo list
def create_todo_list():
    todo_list.append(input("todo 를 입력하세요: "))
    print(input(todo_list))
    pass
#update the todo list
def Update_todo_list():
    for i in range(len(todo_list)):
        print(f"todo list 목록 {i+1}. {todo_list[i]}")

Update_todo_list()