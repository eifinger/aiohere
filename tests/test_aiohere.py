"""Tests for `aioweenect.aioweenect`."""
from aiohere.enum import WeatherProductType
from aiohere.aiohere import API_HOST, API_PATH
import json
import os

import aiohttp
import pytest

from aiohere import AioHere


# @pytest.mark.asyncio
# async def test_get_user_with_invalid_token(aresponses):
#     """Test getting user information with a timed out token."""
#     aresponses.add(
#         API_HOST,
#         f"{API_VERSION}/user/login",
#         "POST",
#         response=load_json_fixture("login_response.json"),
#     )
#     aresponses.add(
#         API_HOST,
#         f"{API_VERSION}/user/100000",
#         "GET",
#         aresponses.Response(
#             body="{"
#             '"description": "Signature has expired",'
#             '"error": "Invalid token",'
#             '"status_code": 401'
#             "}",
#             status=401,
#         ),
#     )
#     aresponses.add(
#         API_HOST,
#         f"{API_VERSION}/user/login",
#         "POST",
#         response=load_json_fixture("login_response.json"),
#     )
#     aresponses.add(
#         API_HOST,
#         f"{API_VERSION}/user/100000",
#         "GET",
#         response=load_json_fixture("get_user_response.json"),
#     )
#     async with aiohttp.ClientSession() as session:
#         aioweenect = AioWeenect(username="user", password="password", session=session)
#         response = await aioweenect.get_user("100000")

#         assert response["postal_code"] == "55128"


@pytest.mark.asyncio
async def test_get_weather(aresponses):
    """Test getting weather information."""
    aresponses.add(
        API_HOST,
        API_PATH,
        "GET",
        response=load_json_fixture("daily_simple_forecasts.json"),
    )
    async with aiohttp.ClientSession() as session:
        aiohere = AioHere(api_key="password", session=session)
        response = await aiohere.weather_for_coordinates(
            latitude=0.0,
            longitude=0.0,
            product=WeatherProductType.forecast_7days_simple,
        )

        assert (
            response["dailyForecasts"]["forecastLocation"]["forecast"][0][
                "highTemperature"
            ]
            == "4.00"
        )


def load_json_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        content = fptr.read()
        json_content = json.loads(content)
        return json_content
