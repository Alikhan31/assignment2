class DataProcessorCreator:
    def __init__(self, processor=None):
        self.processor = processor

    def setProcessor(self, processor):
        self.processor = processor

    def processData(self, data):
        if self.processor is None:
            raise ValueError("Processor not set")
        return self.processor.createDataProcessor(data)
