from app.app import hello

def test_app():
    assert hello() == '<h1>Hello, World!</h1>'
    