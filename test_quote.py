from quote import get_inspirational_quote

def test_quote_fetch():
    quote = get_inspirational_quote()
    assert isinstance(quote, str)
    assert len(quote) > 0
