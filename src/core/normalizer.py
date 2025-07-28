"""
Defines the normalized event structure for all log types.
"""

def normalize_event(
    timestamp: str,
    source: str,
    event_type: str,
    details: dict
) -> dict:
    """
    Returns a normalized event dictionary.
    Args:
        timestamp (str): Event timestamp (ISO 8601 recommended)
        source (str): Log source (e.g., 'apache', 'sysmon', 'windows')
        event_type (str): Type of event (e.g., 'logon', 'process_creation', 'http_request')
        details (dict): Additional event details
    Returns:
        dict: Normalized event
    """
    return {
        'timestamp': timestamp,
        'source': source,
        'event_type': event_type,
        'details': details
    }
