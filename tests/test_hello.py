from best import hello

def test__hello__sam__says_hello():
    result = hello('sam')
    assert result == 'Hello, sam'x