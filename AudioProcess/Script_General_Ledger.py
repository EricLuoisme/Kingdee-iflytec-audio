from AudioProcess.data import Sin_General_Ledger
from AudioProcess import Recognition_process


def do_script(result, num):
    sce = "scenario_" + str(num)
    scenario = Sin_General_Ledger.get_scenario(sce)
    check = True
    for key in scenario:
        # print(scenario.get(key))
        if scenario.get(key) not in result:
            check = False
            break
    if check:
        print(Sin_General_Ledger.get_answer(sce))
        Recognition_process.doing_voice_comb(Sin_General_Ledger.get_answer(sce))

        return False
        ###################################


def do_sub_script(num):
    # 只有在用户回答查看原因的时候才会执行子场景
    sce = "scenario_" + str(num) + "_sub"
    print(Sin_General_Ledger.get_answer(sce))
    return False
