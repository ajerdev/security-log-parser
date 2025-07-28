# Security Log Parser

A Python parser capable of interpreting system logs (Windows, Sysmon, Apache, nginx…) and normalizing them into a structured format.

---

## Phases

### 🔥 Phase 1 – Core Logs (High Priority)
These are the most common logs in enterprise environments and SOCs.

| Source                  | Format                | Content Highlights                             |
|-------------------------|-----------------------|------------------------------------------------|
| **Windows Event Logs**  | `.evtx` / XML / JSON  | Logon events, process creation, etc.           |
| **Sysmon**              | XML / JSON            | Processes, network activity, file changes.     |
| **Apache access/error** | Plaintext (customizable) | HTTP requests, errors, IPs.               |
| **nginx access/error**  | Plaintext             | Similar to Apache.                             |

### 🛡️ Phase 2 – Security and Critical System Logs

| Source                    | Format       | Content Highlights                            |
|---------------------------|--------------|-----------------------------------------------|
| **auth.log / secure.log (Linux)** | Plaintext | Authentication attempts, sudo, SSH.         |
| **auditd (Linux Audit Framework)** | Key-Value  | Kernel events, syscalls.                    |
| **iptables / ufw**        | Plaintext     | Allowed/blocked network traffic.              |
| **DNS logs (BIND, Unbound)** | Plaintext  | DNS queries, blocks, suspicious activity.     |

### 📡 Phase 3 – Network and Proxy Logs

| Source             | Format     | Content Highlights                       |
|--------------------|------------|------------------------------------------|
| **Squid Proxy**    | Plaintext  | URL access, IPs, timestamps.             |
| **Zeek (Bro)**     | TSV        | Connections, DNS, HTTP, SSL, etc.        |
| **Suricata / Snort** | JSON / Eve | IDS alerts, traffic metadata, signatures. |

### 🧪 Phase 4 – Specialized / Advanced Logs

| Source                          | Format       | Content Highlights                           |
|---------------------------------|--------------|-----------------------------------------------|
| **AWS CloudTrail / GuardDuty**  | JSON         | Cloud activity (IAM, S3 access, etc.).        |
| **Okta / Azure AD**             | JSON         | Logins, MFA, resource access.                 |
| **VPN logs (OpenVPN, IPSec)**   | Plaintext    | Connection data, IPs, authentication.         |
| **EDR (CrowdStrike, SentinelOne)** | JSON / API | Detections, behavior, process activity.       |

---

## Project structure

- `src/core/`: Core, base classes, normalization
- `src/parsers/`: Specific parsers
- `src/exporters/`: Exporters (JSON, SIEM)
- `src/utils/`: Utilities
- `tests/`: Unit tests
- `samples/`: Sample logs
- `docs/`: Documentation
