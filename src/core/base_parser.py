from abc import ABC, abstractmethod

class BaseLogParser(ABC):
    """
    Abstract base class for all log parsers.
    """
    @abstractmethod
    def parse_line(self, line):
        """
        Receives a log line and returns a normalized dictionary.
        """
        pass

    def parse_file(self, file_path):
        """
        Parses a file line by line and returns a list of normalized events.
        """
        events = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                event = self.parse_line(line)
                if event:
                    events.append(event)
        return events
