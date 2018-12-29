import time
import os
from AudioProcess import Main_process
from AudioProcess.data import Timing_Setting, File_Setting


# 判断是否存在路径，没有则创建
if os.path.exists(File_Setting.outPath_Arouse) is False:
    os.makedirs(File_Setting.outPath_Arouse)
    os.makedirs(File_Setting.outPath_Script)
    os.makedirs(File_Setting.outPath_Combin)

tt = Main_process.TapTester()
time.sleep(2)
print('程序开始运行')
while Timing_Setting.main_record_time:
    tt.listen()
