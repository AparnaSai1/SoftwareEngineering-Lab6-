from main import encoder, decode_str

def test_encoder():
    assert encoder("123456") == "456789"
    assert encoder("098765") == "321098"
    assert encoder("555555") == "888888"
    assert encoder("") == ""
    
def test_decode_str():
    assert decode_str("45678888") == "12345555"
    assert decode_str("321098") == "098765"
    assert decode_str("888888") == "555555"
    assert decode_str("") == ""

