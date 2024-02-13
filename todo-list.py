#todo list 
# CRUD 

#Read the todo list 
todo_list= ["list1", "list2", "list3", ]
def read_todo_list():
    for i in todo_list:
        print(i)
        pass    

#Create the todo list
def create_todo_list(todo_list):
    todo_list.append(input("Todo 를 입력하세요: "))
    print(input(todo_list))

#update the todo list
def Update_todo_list(todo_list):
    for i in range(len(todo_list)):
        print(f"Todo list 목록 {i+1}. {todo_list[i]}")
    input_number =int(input(f"수정하기 메뉴 입니다.to do 목록 번호를 입력하세요.:" ))-1
    if 0<= input_number < len(todo_list):
        print(f"번호는{input_number+1}이고 todo는 {todo_list[input_number]}")
    else:    
        print("다시 입력해 주세요")

Update_todo_list(todo_list)
create_todo_list(todo_list)

#dd
