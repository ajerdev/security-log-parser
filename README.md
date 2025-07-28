# Security Log Parser

A Python parser capable of interpreting system logs (Windows, Sysmon, Apache, nginx…) and normalizing them into a structured format.

## Phases

### Phase 1 – Core logs (high priority)
- Windows Event Logs (.evtx / XML / JSON)
- Sysmon (XML / JSON)
- Apache access/error (Plaintext)
- nginx access/error (Plaintext)

### Bonus
- Export to JSON format compatible with SIEM

## Suggested structure

- `src/core/`: Core, base classes, normalization
- `src/parsers/`: Specific parsers
- `src/exporters/`: Exporters (JSON, SIEM)
- `src/utils/`: Utilities
- `tests/`: Unit tests
- `samples/`: Sample logs
- `docs/`: Documentation
