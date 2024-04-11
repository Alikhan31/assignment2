class TextDataProcessor(DataProcessor):
    def createDataProcessor(self, data):
        # Process text data
        print(f"Processing Text Data: {data.content}")

class AudioDataProcessor(DataProcessor):
    def createDataProcessor(self, data):
        # Process audio data
        print(f"Processing Audio Data: {data.content}")

class VideoDataProcessor(DataProcessor):
    def createDataProcessor(self, data):
        # Process video data
        print(f"Processing Video Data: {data.content}")
