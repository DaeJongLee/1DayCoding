#get the valulable numbers
def get_number(prompt):
    while True:
        try: 
            return float(input(prompt))
        except ValueError:
            print("유효한 숫자를 입력해주세요.")
#taking number 
input_ls = []
for i in range(1,3):
    input_number =get_number(f"{i}번째 숫자를 입력하세요.:" )
    print (f"{i}번째 숫자는 {input_number},입니다.")
    input_ls.append(input_number)

# calulating
def perform_calculation(input_ls):
    calculateing = input("연산자를 입력하세요 : + - * / ")
    if calculateing == "+":
        print(input_ls[0]+input_ls[1])
    elif calculateing == "-":         
        print((input_ls[0])-(input_ls[1]))
    elif calculateing == "*":         
        print((input_ls[0])*(input_ls[1]))
    elif calculateing == "/":         
        if input_ls[1] == 0:
            print("0으로는 나눌수 없습니다.")
        else:
            print((input_ls[0])/(input_ls[1]))

#playing 
            
perform_calculation(input_ls)