from unittest.mock import patch

from src.weather import get_weather


@patch('requests.get')
def test_get_weather_with_mocks(mocked_get):
    # Given
    expected_weather = {"main": {"temp": 25}, "weather": [{"main": "Clear"}]}
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = expected_weather

    # When
    weather_data = get_weather("London")

    # Then
    assert weather_data == expected_weather


@patch('requests.get')
def test_get_weather_with_mocks_error(mocked_get):
    # Given
    mocked_get.return_value.status_code = 404

    # When
    weather_data = get_weather("London")

    # Then
    assert weather_data is None
