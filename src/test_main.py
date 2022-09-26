import main
import pytest

# Tests main input method
class TestInput:
    # Check if returning values normally
    def test_normal(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: "test")
        assert main.get_input('prompt') == 'test'

    # Check if raising error when player enters 'quit'
    def test_error(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: "quit")
        with pytest.raises(main.QuitError):
            main.get_input('prompt')

# Tests hero instantiation
class TestHeroInst:
    # Testing name returns correctly
    def test_name(self):
        hero = main.Character('test')
        assert hero.name == 'Test'

    # Testing level is correctly assigned
    def test_level(self):
        hero = main.Character('test')
        assert hero.level == 5
