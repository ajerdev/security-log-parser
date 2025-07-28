from src.core.base_parser import BaseLogParser
from src.core.normalizer import normalize_event
import re

class NginxAccessLogParser(BaseLogParser):
    """
    Parser for Nginx access logs (common format, similar to Apache).
    """
    log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) (?P<size>\S+)')

    def parse_line(self, line):
        match = self.log_pattern.match(line)
        if match:
            return normalize_event(
                timestamp=match.group('datetime'),
                source='nginx',
                event_type='http_request',
                details={
                    'ip': match.group('ip'),
                    'method': match.group('method'),
                    'url': match.group('url'),
                    'status': int(match.group('status')),
                    'size': int(match.group('size')) if match.group('size').isdigit() else 0
                }
            )
        return None
