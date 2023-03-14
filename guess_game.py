import random

# 1.增加勝負判斷(提示猜了幾次)
# 2.提示區間


x = random.randint(1, 50)
print(x)
win = False
for i in range(5):
    y = eval(input('請猜一個數字(1~50之間):'))
    if x == y:
        win = True
        break

    if x > y:
        print('猜大一點')
    else:
        print('猜小一點')

if win:
    print('恭喜過關!')

print(f'遊戲結束!答案為:{x}')
