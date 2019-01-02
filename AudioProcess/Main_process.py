# #!/usr/bin/python
#
# # open a microphone in pyAudio and listen for taps
#
# import pyaudio
# import math
# # import time
# import wave
# import struct
#
# # import Denoising_process
# from AudioProcess import Recognition_process, Cutting_process, Script_process
# from AudioProcess.data import File_Setting
# # from data import Timing_Setting
#
#
# INITIAL_TAP_THRESHOLD = 0.010
# FORMAT = pyaudio.paInt16
# SHORT_NORMALIZE = (1.0 / 32768.0)
# CHANNELS = 1
# # RATE = 44100
# RATE = 16000
# INPUT_BLOCK_TIME = 0.05
# INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)
# RECORD_SUSTAIN = 2 / INPUT_BLOCK_TIME  # change from 2.5 to 2
# # if we get this many noisy blocks in a row, increase the threshold
# OVERSENSITIVE = 15.0 / INPUT_BLOCK_TIME
# # if we get this many quiet blocks in a row, decrease the threshold
# UNDERSENSITIVE = 120.0 / INPUT_BLOCK_TIME
# # if the noise was longer than this many blocks, it's not a 'tap'
# MAX_TAP_BLOCKS = 0.15 / INPUT_BLOCK_TIME
#
# FILE_NUMBER = 0
#
# #####################################################
# # For audio recording
#
#
# def get_rms(block):
#     # RMS amplitude is defined as the square root of the
#     # mean over time of the square of the amplitude.
#     # so we need to convert this string of bytes into
#     # a string of 16-bit samples...
#
#     # we will get one short out for each
#     # two chars in the string.
#     count = len(block) / 2
#     format = "%dh" % (count)
#     shorts = struct.unpack(format, block)
#
#     # iterate over the block.
#     sum_squares = 0.0
#     for sample in shorts:
#         # sample is a signed short in +/- 32768.
#         # normalize it to 1.0
#         n = sample * SHORT_NORMALIZE
#         sum_squares += n * n
#
#     return math.sqrt(sum_squares / count)
#
#
# class TapTester(object):
#     def __init__(self):
#         self.pa = pyaudio.PyAudio()
#         self.stream = self.open_mic_stream()
#         self.tap_threshold = INITIAL_TAP_THRESHOLD
#         self.noisycount = MAX_TAP_BLOCKS + 1
#         self.quietcount = 0
#         self.errorcount = 0
#         self.record_status = 0
#         self.record_data = []
#
#     def stop(self):
#         self.stream.close()
#
#     def find_input_device(self):
#         device_index = None
#         for i in range(self.pa.get_device_count()):
#             devinfo = self.pa.get_device_info_by_index(i)
#             print("Device %d: %s" % (i, devinfo["name"]))
#
#             for keyword in ["mic", "input"]:
#                 if keyword in devinfo["name"].lower():
#                     print("Found an input: device %d - %s" % (i, devinfo["name"]))
#                     device_index = i
#                     return device_index
#
#         if device_index is None:
#             print("No preferred input found; using default input device.")
#
#         return device_index
#
#     def open_mic_stream(self):
#         device_index = self.find_input_device()
#
#         stream = self.pa.open(format=FORMAT,
#                               channels=CHANNELS,
#                               rate=RATE,
#                               input=True,
#                               input_device_index=device_index,
#                               frames_per_buffer=INPUT_FRAMES_PER_BLOCK)
#
#         return stream
#
#     def tapDetected(self):
#         print("Tap!")
#
#     #############################################
#     # the main function
#     def listen(self, mode=1, sub_scenario='no', sub_scenario_number=0):
#         try:
#             block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
#         except IOError:
#             # dammit.
#             self.errorcount += 1
#             print("(%d) Error recording: " % (self.errorcount))
#             self.noisycount = 1
#             return
#
#         amplitude = get_rms(block)
#
#         if self.record_status == 1:
#             self.record_data.append(block)
#
#         if amplitude > self.tap_threshold:
#             # noisy block
#
#             self.quietcount = 0
#             self.noisycount += 1
#             if self.noisycount > OVERSENSITIVE:
#                 # turn down the sensitivity
#                 self.tap_threshold *= 1.1
#             else:
#                 if self.record_status == 0:
#                     # 开始录音
#                     self.record_data = []
#                     self.record_data.append(block)
#                     self.record_status = 1
#                     print('正在录音')
#         else:
#             # quiet block.
#
#             if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
#                 self.tapDetected()
#             self.noisycount = 0
#             self.quietcount += 1.5    ########################### initial 1
#             if self.quietcount > RECORD_SUSTAIN:
#                 if self.record_status == 1:
#                     # 结束录音
#                     #                     time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#                     #                     print('正在保持至'+time_str+'.wav')
#                     #                     wf = wave.open(time_str+'.wav', 'wb')
#
# #################################################################################################
#
#                     global FILE_NUMBER
#                     # can change the name of saved file here
#
#                     if mode is 1:
#                         outfile = File_Setting.outPath_Arouse + File_Setting.outFileName + str(FILE_NUMBER)
#                         # for arouse-word checking
#                     else:
#                         outfile = File_Setting.outPath_Script + File_Setting.outFileName + str(FILE_NUMBER)
#                         # for script checking / arouse + sub-scenario
#
#                     wf = wave.open(outfile + '.wav', 'wb')
#                     wf.setnchannels(CHANNELS)
#                     wf.setsampwidth(self.pa.get_sample_size(FORMAT))
#                     wf.setframerate(RATE)
#                     wf.writeframes(b''.join(self.record_data))
#                     wf.close()
#                     self.record_status = 0
#                     print('结束录音')
#                     FILE_NUMBER = FILE_NUMBER + 1
#
# ################################################################################################
#
#                     # three main processes here
#                     Cutting_process.doing_cutting(outfile)
#                     # print('cut-process finished')
#
#                     # if mode:
#                     #     # 识别指令的时候进行降噪
#                     #     # Denoising_process.doing_denoise(outfile)
#                     #     # print('de-noise-process finished')
#                     #     result = Recognition_process.doing_recog(outfile, False)####### no denoise
#                     # else:
#                     #     # 识别唤醒词的时候不进行降噪
#                     #     # print('skip de-noise process')
#                     #     result = Recognition_process.doing_recog(outfile, False)
#
#                     result = Recognition_process.doing_recog(outfile, False)
#
#                     if mode is 1:
#                         done = Script_process.arouse_recognize(result)
#                         # 唤醒后完成操作done将返回True
#                         # for arouse-word checking
#                         if done:
#                             return True
#                         else:
#                             print('你好像不是在叫我' + '\n')
#                     elif mode is 2:
#                         done = Script_process.script_recognize(result)
#                         # 完成操作done将返回True
#                         # for script checking
#                         if done:
#                             return True
#                         else:
#                             print('对不起我没有听清楚' + '\n')
#                     else:
#                         # mode 3
#                         done = Script_process.sub_script_recognize(result, sub_scenario, sub_scenario_number)
#                         # 完成操作done将返回True
#                         # for script checking
#                         if done:
#                             return True
#                         # else:
#                             # print('重新返回到监听mode' + '\n')
#
#             if self.quietcount > UNDERSENSITIVE:
#                 # turn up the sensitivity
#                 self.tap_threshold *= 0.9
