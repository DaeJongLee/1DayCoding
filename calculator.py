input_a =input("첫번째 숫자를 입력하세요.:" )
input_b =input("두번째 숫자를 입력하세요.:" )
 
def calculater(input_a,input_b):
    #checking input
    print(f"첫번째 숫자는 {input_a}, 두번째 숫자는{input_b}입니다.")
    input_how_to_calculate = input("연산자를 입력하세요 : + - * / ")
    if input_how_to_calculate == "+":
        print(num(input_a)+num(input_b))


calculater(input_b,input_b)