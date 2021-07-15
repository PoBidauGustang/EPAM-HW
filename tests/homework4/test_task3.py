from homework4.task3 import my_precious_logger


def test_my_precious_logger_positive_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_my_precious_logger_positive_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"


def test_my_precious_logger_positive_stdout_another_case(capsys):
    my_precious_logger("NOT an error - captured in stdout")
    captured = capsys.readouterr()
    assert captured.out == "NOT an error - captured in stdout"
