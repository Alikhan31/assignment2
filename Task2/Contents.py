# Assuming simplistic content definitions; real implementations would be more complex.
class TextContent:
    def __init__(self, text):
        self.text = text

class AudioContent:
    def __init__(self, audio_file):
        self.audio_file = audio_file

class VideoContent:
    def __init__(self, video_file):
        self.video_file = video_file
