from Prosjektoppgave.utils.functions import log_decorator


def test_log_decorator_prints_messages(capsys):
    @log_decorator
    def hello():
        print("Hello")
        return 123

    result = hello()
    captured = capsys.readouterr()

    assert result == 123
    assert "Funksjonen hello blir kalt." in captured.out
    assert "Hello" in captured.out
    assert "Funksjonen hello er ferdig." in captured.out
