from src.core.base_parser import BaseLogParser
from src.core.normalizer import normalize_event
import json

class SysmonLogParser(BaseLogParser):
    """
    Parser for Sysmon logs in JSON format (basic example).
    """
    def parse_line(self, line):
        try:
            data = json.loads(line)
            # Example: extract some common Sysmon fields
            timestamp = data.get('UtcTime')
            event_type = data.get('EventType', 'sysmon_event')
            details = {k: v for k, v in data.items() if k not in ['UtcTime', 'EventType']}
            return normalize_event(
                timestamp=timestamp,
                source='sysmon',
                event_type=event_type,
                details=details
            )
        except Exception:
            return None
