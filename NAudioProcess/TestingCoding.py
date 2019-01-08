
from NAudioProcess import NMain_process

result = str("小智同学")
state_now = NMain_process.identify_execute(result)

i = 0

if state_now.type is 'Arousing':
    print("唤醒成功")
    result = str("请制作一张提现凭证")
    state_now = NMain_process.identify_execute(result)
