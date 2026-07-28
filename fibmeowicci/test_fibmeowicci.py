from fibmeowicci import meow

from io import StringIO
import sys

def test_meow():
    captured = StringIO()
    prev = sys.stdout
    sys.stdout = captured
    meow(limit=5)
    sys.stdout = prev
    assert '\nmeow\nmeow\nmeow meow\nmeow meow meow\n' == captured.getvalue()
