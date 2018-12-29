from AudioProcess.data import File_Setting


class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self. path)


class MovieMP4(Video):
    type = 'MP4'


# if __name__ == "__main__":
#     movie = MovieMP4(File_Setting.videoPath)
#     movie.play()
