from AudioProcess import Script_process


def identify_execute(string):

    arousing_status = Script_process.arouse_recognize(string)
    if arousing_status is not None:
        return arousing_status
    else:
        script_status = Script_process.script_recognize(string)
        if script_status is not None:
            return script_status

    return None
