from src.core.base_parser import BaseLogParser
from src.core.normalizer import normalize_event
import xml.etree.ElementTree as ET

class WindowsEventLogParser(BaseLogParser):
    """
    Parser for Windows Event Logs in XML format (basic example).
    """
    def parse_line(self, line):
        try:
            root = ET.fromstring(line)
            timestamp = root.findtext('.//TimeCreated/@SystemTime')
            event_id = root.findtext('.//EventID')
            details = {elem.tag: elem.text for elem in root.iter() if elem.text}
            return normalize_event(
                timestamp=timestamp,
                source='windows',
                event_type=event_id or 'windows_event',
                details=details
            )
        except Exception:
            return None
