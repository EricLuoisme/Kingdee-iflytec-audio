

def detect_keywords_percentage(string, keywords):
    # 对输入的场景的keywords进行检测，获得百分比
    inside = 0
    for i in keywords:
        have = False
        this_keywords = keywords.get(i)
        for j in this_keywords:
            if string.__contains__(j):
                have = True
                break
        if have:
            inside += 1
            continue

    return inside/keywords.__len__()




# string = str("请制作一张体先凭证")
# string = str("随便测试体现凭证")
# keywords = {
#     0: {'制作', '生成'},
#     1: {'提现', '体现', '体先', '提鲜'},
#     2: {'凭证'}
# }
#
# print(detect_keywords_percentage(string, keywords))



