

input_ls = []
input_a =input("첫번째 숫자를 입력하세요.:" )
input_ls.append(input_a)
input_b =input("두번째 숫자를 입력하세요.:" )
input_ls.append(input_b)

print(f"첫번째 숫자는 {input_ls[0]}, 두번째 숫자는{input_ls[1]}입니다.")
def calculater():
    calculateing = input("연산자를 입력하세요 : + - * / ")
    if calculateing == "+":
        print(int(input_ls[0])+int(input_ls[1]))
    elif calculateing == "-":         
        print(int(input_ls[0])-int(input_ls[1]))
    elif calculateing == "*":         
        print(int(input_ls[0])*int(input_ls[1]))
    elif calculateing == "/":         
        print(int(input_ls[0])/int(input_ls[1]))
    
calculater()