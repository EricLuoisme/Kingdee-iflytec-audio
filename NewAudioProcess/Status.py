

class Status:

    def __init__(self, the_type, the_state=None, the_num=None):
        # type, state, num 分别对应 主类型，是否为子场景，场景编号
        self.type = the_type
        self.state = the_state
        self.num = the_num

        # type: 'General_Ledger', 'Receivable_Module', 'Arousing', 'Mis_operation '
