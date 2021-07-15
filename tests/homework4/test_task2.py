from unittest.mock import patch

import pytest

from homework4.task2 import count_dots_on_i


def test_count_dots_on_i_mocked_data_poisitive():
    with patch("requests.get") as mock_request:
        url = "https://example.com/"
        mock_request.return_value.content = "i" * 59
        assert count_dots_on_i(url) == 59
        mock_request.assert_called_once_with(url)


def test_count_dots_on_i_incorrect_URL():
    with pytest.raises(ValueError, match="Unreachable https://inNncCorrect.com/"):
        count_dots_on_i("https://inNncCorrect.com/")
