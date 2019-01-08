# 应收场景


def get_scenario(sce):
    return {
        #####################################################################
        # 1. 应收系统收款单-收款单新增审核收款
        # Q: 小智，请制作一张应收收款单。
        # A: 好的，接下来会根据您的要求制作一张应收收款单，业务情况是：...
        # ...2018年1月18日，收到客户瑞达股份公司的一笔通过电汇的方式进入汇丰银行的人民币账户的20000元的销售回款。
        # A: 应收收款单完成了，接下来对收款单进行提交审核处理以及收款处理。
        'scenario_1': {
            0: {'制作', '生成'},
            1: {'应收', '营收', '应受'},
            2: {'收款单'}
        },
        #####################################################################
        # 2. 机器人执行收款单生成凭证
        # Q: 小智，请对应收系统制作的收款单进行生成凭证处理。
        # A: 好的，接下来会根据您来生成应收收款单的全部财务凭证。
        'scenario_2': {
            0: {'应收系统', '营收系统', '应受系统'},
            1: {'收款单', '首款单'},
            2: {'生成'},
            3: {'凭证', '平整'},
            4: {'处理'}
        },
        # A: 你好，应收收款单已经生成了凭证，需要为您打开查看下成功的记录吗？
        # Q1: 好的，请打开成功的记录
        # Q1.1 小智，请打开生成的凭证让我看下。
        # Q2: 小智，不用了。
        'scenario_2_sub': {
        },
        #####################################################################
        # 3. 机器人执行收款单生成凭证设置
        # Q: 小智，我要看看应收收款单凭证生成机器人是如何设置的。
        # A: 好的，接下来我们看看金蝶软件（中国）有限公司的应收收款单凭证生成机器人是如何设置的。
        # A: 本页面的设置，可以保证金蝶软件（中国）有限公司每天对制作好的应收收款单进行凭证生成处理。
        'scenario_3': {
            0: {'应收'},
            1: {'收款单'},
            2: {'如何'},
            3: {'设置'}
        }
    }[sce]


def get_answer(sce):
    return {
        'scenario_1': '好的，接下来会根据您的要求制作一张应收收款单，业务情况是：'
                      '2018年1月18日，收到客户瑞达股份公司的一笔通过电汇的方式进入汇丰银行的人民币账户的20000元的销售回款。',
        'scenario_2': '好的，接下来会根据您来生成应收收款单的全部财务凭证， 随后进入子场景',
        'scenario_2_sub': '好的，请打开成功的记录',
        'scenario_3': '好的，接下来我们看看金蝶软件（中国）有限公司的应收收款单凭证生成机器人是如何设置的。',
    }[sce]


