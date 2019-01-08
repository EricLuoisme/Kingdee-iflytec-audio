from NAudioProcess import NMain_process


FILE_NUMBER = 0


def simple_checking(result):

    global FILE_NUMBER

    string = str("小智同学")
    state_now = NMain_process.identify_execute(string, FILE_NUMBER)

    arouse = False
    if state_now.type is 'Arousing':
        arouse = True
        print("唤醒成功")
        state_now = NMain_process.identify_execute(result, FILE_NUMBER, arouse)
        FILE_NUMBER = FILE_NUMBER + 1
        if state_now is not None:
            arouse = False


result = str("请制作一张提现凭证")
simple_checking(result)
result = str("对本期完成的凭证进行提交处理")
simple_checking(result)
result = str("我要看看总账凭证提交的机器人是如何设置的")
simple_checking(result)
result = str("请对本期提交的凭证进行审核处理")
simple_checking(result)
result = str("我要看看总账凭证审核的机器人是如何设置的")###################
simple_checking(result)
result = str("请制作一张应收收款单")
simple_checking(result)
result = str("请对应收系统制作的收款单进行生成凭证处理")###################
simple_checking(result)
result = str("我要看看应收收款单凭证生成机器人是如何设置的")###############
simple_checking(result)