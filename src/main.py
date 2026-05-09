from validator import validate_event

def process_event(event_name):
    if not validate_event(event_name):
        return "Invalid event"

    return f"Processed: {event_name.upper()}"
