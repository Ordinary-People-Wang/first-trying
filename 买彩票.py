import random
fonds=200
print('您的初始资金为200美刀！每次买中最低可得5倍奖金！十轮后若资金大于200美刀即可获胜！')
for i in range(10):
    a=random.randint(1, 9)
    number=int(input("请选择您要购买的号码（1-9）："))
    while number<=0 or number>9:
        print('违规！请重新购买！')
        number=int(input("请选择您要购买的号码（1-9）："))
    multiple=int(input("加几注？："))
    while multiple<=0:
        print('违规！请重新加注！')
        multiple=int(input("加几注？："))
    fonds-=10*multiple
    print('您的资金剩余：',fonds)
    for j in range(3):
        print('噔噔咚！')
    print('中奖号码是',a,'!')
    if a==number:
        print('恭喜您中奖了！奖金：',50*multiple)
        fonds+=50*multiple
    else:
        print('很遗憾您没有中奖，请再接再厉吧！')
    print('您的资金剩余：',fonds)
    if fonds<=0:
        break
if fonds>200:
    print('You win!!!')
else:
    print('Sorry,please try again!')