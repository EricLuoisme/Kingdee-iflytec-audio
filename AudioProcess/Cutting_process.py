
import wave
import struct
import numpy as np

from AudioProcess.data import Cutting_Setting

######################################################

THRESHOLD_FOR_CUTTING_PLA = Cutting_Setting.THRESHOLD_FOR_CUTTING_PLA   # 认为振幅在20%以上为有效输入
ACCEPTABLE_INTERVAL_TIME = Cutting_Setting.ACCEPTABLE_INTERVAL_TIME     # 1.5秒内，认为是同一条指令
UP_FRONT_INFO_TIME = Cutting_Setting.UP_FRONT_INFO_TIME     # 切割音频时添加有效输入的前0.25s
DOWN_BACK_INFO_TIME = Cutting_Setting.DOWN_BACK_INFO_TIME   # 切割音频时添加有效输入的后0.5s

#####################################################


# for cutting the audio
def cut(waveData, framerate):
    start = -1
    end = -1
    count = 0
    for i in range(len(waveData)):
        if waveData[i] > THRESHOLD_FOR_CUTTING_PLA:  # meet needed info
            if start < 0:
                temp = i - int(UP_FRONT_INFO_TIME * framerate)
                if temp > 0:
                    start = temp
                else:
                    start = 0
            count = 0
        else:
            if start < 0:  # before meeting the needed info
                continue
            elif count / framerate < ACCEPTABLE_INTERVAL_TIME:
                count = count + 1
            else:
                end = i - count + int(DOWN_BACK_INFO_TIME * framerate)
                #                 print(count)
                break
    return start, end


def doing_cutting(outfile):
    f = wave.open(outfile + '.wav', "r")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = f.readframes(nframes)
    waveData_org = np.frombuffer(strData, dtype=np.int16)
    waveData = waveData_org * 1.0 / (max(abs(waveData_org)))

    channels = f.getnchannels()
    sampwidth = f.getsampwidth()
    framerate = f.getframerate()
    start, end = cut(waveData, framerate)  # use cut function

    # could use overwirte
    outwave = wave.open(outfile + '_cut.wav', 'wb')
    outwave.setnchannels(channels)
    outwave.setframerate(framerate)
    outwave.setsampwidth(sampwidth)

    for v in waveData[start:end]:
        outwave.writeframes(struct.pack('h', int(v * 64000 / 2)))  # outData:16位，-32767~32767，注意不要溢出
