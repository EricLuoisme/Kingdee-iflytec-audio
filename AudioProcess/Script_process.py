import time

from AudioProcess.data import WakeWord_Setting, Timing_Setting
from AudioProcess import Main_process, Recognition_process, Script_General_Ledger, Script_Receivable_module


def arouse_recognize(result):
    if result is not "":
        if result.__contains__(WakeWord_Setting.wake_word):
            print("您好，小智来了")
            Recognition_process.doing_voice_Comb("您好，小智来了")
            tt = Main_process.TapTester()
            time.sleep(1)
            print('开始接收指令')
            for ii in range(Timing_Setting.script_record_time):
                check = tt.listen(2)
                if check:
                    # 正确执行指令后，check为True
                    return True
    else:
        return False


def script_recognize(result):
    # 返回True：已经执行
    # 返回False：需要重新录音
    if result is not "":

        # 错误唤醒 操作
        if result.__contains__("没事"):
            return True

        # 制作/生成 操作
        if result.__contains__("制作") or result.__contains__("生成"):
            # 总账场景 2 + 应收场景 1
            check = Script_General_Ledger.do_script(result, 2)  # 完成执行操作后，check应返回False
            if check is False:
                return True

            check = Script_Receivable_module.do_script(result, 1)  # 完成执行操作后，check应返回False
            if check is False:
                return True

        # 处理/审核 操作
        elif result.__contains__("处理"):
            # 总账场景 3,5 + 应收场景 2
            check = Script_General_Ledger.do_script(result, 3)  # 完成执行操作后，check应返回False
            if check is False:
                mode_3_trigger('g', 3)  # 这边存在子场景
                return True
            check = Script_General_Ledger.do_script(result, 5)  # 完成执行操作后，check应返回False
            if check is False:
                mode_3_trigger('g', 5)  # 这边存在子场景
                return True
            check = Script_Receivable_module.do_script(result, 2)  # 完成执行操作后，check应返回False
            if check is False:
                mode_3_trigger('r', 2)  # 这边存在子场景
                return True

        # 查看设置 操作
        elif result.__contains__("查看") or result.__contains__("设置"):
            # 总账场景 4,6 + 应收场景 3
            check = Script_General_Ledger.do_script(result, 4)  # 完成执行操作后，check应返回False
            if check is False:
                return True
            check = Script_General_Ledger.do_script(result, 6)  # 完成执行操作后，check应返回False
            if check is False:
                return True
            check = Script_Receivable_module.do_script(result, 3)  # 完成执行操作后，check应返回False
            if check is False:
                return True
    else:
        return False


def mode_3_trigger(scenario, scenario_number):
    tt = Main_process.TapTester()
    time.sleep(1)
    print('请问是否查看原因')
    for ii in range(Timing_Setting.script_record_time):
        check = tt.listen(3, scenario, scenario_number)
        #  mode:3   scenario:general ledger    scenario_number:2
        if check:
            # 正确执行指令后，check为True
            print("离开子程序")
            return True


def sub_script_recognize(result, sub_scenario, sub_scenario_number):
    if result.__contains__("好") or result.__contains__("是") or result.__contains__("可以"):
        # 执行查看原因操作
        if sub_scenario is 'g':
            Script_General_Ledger.do_sub_script(sub_scenario_number)
        else:
            # 'r'
            Script_Receivable_module.do_sub_script(sub_scenario_number)
        return True
    elif result.__contains__("不"):
        # 执行取消操作
        print("退出子场景")
        return True
    elif result.__contains__(WakeWord_Setting.wake_word):   # 小智同学
        # 执行新的指令
        arouse_recognize(result)
        return True
    else:
        # 不包含以上三种情况的，继续监听(在mode_3_trigger里循环)
        # print("等待指令种中")
        return False

