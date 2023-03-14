import random

# 1.增加勝負判斷
# 2.提示區間


x = random.randint(1, 50)

for i in range(5):
    y = eval(input('請猜一個數字(1~50之間):'))
    if x == y:
        break

    if x > y:
        print('猜大一點')
    else:
        print('猜小一點')

print(f'遊戲結束!答案為:{x}')
