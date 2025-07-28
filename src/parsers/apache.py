from src.core.base_parser import BaseLogParser
import re

class ApacheAccessLogParser(BaseLogParser):
    """
    Parser for Apache access logs (common format).
    """
    # Example regex for the common Apache log format
    log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) (?P<size>\S+)')

    def parse_line(self, line):
        match = self.log_pattern.match(line)
        if match:
            return {
                'source': 'apache',
                'ip': match.group('ip'),
                'datetime': match.group('datetime'),
                'method': match.group('method'),
                'url': match.group('url'),
                'status': int(match.group('status')),
                'size': int(match.group('size')) if match.group('size').isdigit() else 0
            }
        return None
