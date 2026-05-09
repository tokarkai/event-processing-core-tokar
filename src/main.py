from validator import validate_event

def process_event(event_name):
    print("Processing started")
    event_name = event_name.strip()

    if not validate_event(event_name):
        return "Invalid event"

    return f"Processed: {event_name.upper()}"
