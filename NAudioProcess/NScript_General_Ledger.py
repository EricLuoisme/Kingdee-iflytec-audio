from AudioProcess.data import NSin_General_Ledger
from AudioProcess import Recognition_process
from NAudioProcess import NCheck_Keywords


def do_script(result, num):

    sce = "scenario_" + str(num)
    scenario = NSin_General_Ledger.get_scenario(sce)

    percentage = NCheck_Keywords.detect_keywords_percentage(result, scenario)
    if percentage > 0.6:
        # 在某个场景下，包含其关键词超过60%既认定为该场景
        print(NSin_General_Ledger.get_answer(sce))
        # 语音融合
        # Recognition_process.doing_voice_comb(NSin_General_Ledger.get_answer(sce))
        return False


# def do_sub_script(num):
#     # 只有在用户回答查看原因的时候才会执行子场景
#     sce = "scenario_" + str(num) + "_sub"
#     print(Sin_General_Ledger.get_answer(sce))
#     return False
