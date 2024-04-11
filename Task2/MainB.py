# Example usage
from Task2.Contents import TextContent, AudioContent, VideoContent
from Task2.Data import Data
from Task2.DataProcessorCreator import DataProcessorCreator
from Task2.Processors import TextDataProcessor, AudioDataProcessor, VideoDataProcessor

if __name__ == "__main__":
    # Create data instances
    text_data = Data("text", TextContent("Example text"))
    audio_data = Data("audio", AudioContent("audiofile.mp3"))
    video_data = Data("video", VideoContent("videofile.mp4"))

    # Create processor creator
    processor_creator = DataProcessorCreator()

    # Set and process text data
    processor_creator.setProcessor(TextDataProcessor())
    processor_creator.processData(text_data)

    # Set and process audio data
    processor_creator.setProcessor(AudioDataProcessor())
    processor_creator.processData(audio_data)

    # Set and process video data
    processor_creator.setProcessor(VideoDataProcessor())
    processor_creator.processData(video_data)
