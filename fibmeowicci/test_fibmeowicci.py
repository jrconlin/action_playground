import sys
from io import StringIO

from fibmeowicci import meow


def test_meow():
    captured = StringIO()
    prev = sys.stdout
    sys.stdout = captured
    meow(limit=5)
    sys.stdout = prev
    assert "Meow.\n\nMeow.\n\nMeow meow.\n\nMeow meow meow.\n\n" == captured.getvalue()
