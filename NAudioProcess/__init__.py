import os
from NAudioProcess.data import File_Setting


# 判断是否存在路径，没有则创建
if os.path.exists(File_Setting.outPath_Combin) is False:
    os.makedirs(File_Setting.outPath_Combin)