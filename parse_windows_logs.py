
import win32evtlog

def read_event_log(server="localhost", logtype="Security"):
    """
    Reads Windows event logs and extracts critical events.

    Args:
        server (str): Server to read logs from.
        logtype (str): Type of event log (Security, Application, etc.).
    """
    hand = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    print(f"Reading {total} events from {logtype} logs.")
    
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        for event in events:
            print(f"Event ID: {event.EventID}, Source: {event.SourceName}, Time: {event.TimeGenerated}")

if __name__ == "__main__":
    read_event_log()
