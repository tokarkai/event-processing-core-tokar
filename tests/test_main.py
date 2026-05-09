from src.main import process_event

def test_process_event():
    result = process_event("login")
    assert result == "Processed: LOGIN"
