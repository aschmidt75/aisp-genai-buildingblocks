"""MCPServer Weather Example with Structured Output

Demonstrates how to use structured output with tools to return
well-typed, validated data that clients can easily process.

From https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/mcpserver/weather_structured.py
MIT License
Copyright (c) 2024 Anthropic, PBC
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict

from pydantic import BaseModel, Field

from mcp.server import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create server
mcp = FastMCP("Weather Service")
logger.info("Weather Service MCP server initialized")


# Example 1: Using a Pydantic model for structured output
class WeatherData(BaseModel):
    """Structured weather data response"""

    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Humidity percentage (0-100)")
    condition: str = Field(description="Weather condition (sunny, cloudy, rainy, etc.)")
    wind_speed: float = Field(description="Wind speed in km/h")
    location: str = Field(description="Location name")
    timestamp: datetime = Field(default_factory=datetime.now, description="Observation time")


@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get current weather for a city with full structured data"""
    logger.debug(f"get_weather called with city={city}")
    # In a real implementation, this would fetch from a weather API
    result = WeatherData(temperature=21.5, humidity=55.0, condition="partly cloudy", wind_speed=12.3, location=city)
    logger.info(f"Returning weather data for {city}: temp={result.temperature}°C, condition={result.condition}")
    return result


# Example 2: Using TypedDict for a simpler structure
class WeatherSummary(TypedDict):
    """Simple weather summary"""

    city: str
    temp_c: float
    description: str


@mcp.tool()
def get_weather_summary(city: str) -> WeatherSummary:
    """Get a brief weather summary for a city"""
    logger.debug(f"get_weather_summary called with city={city}")
    result = WeatherSummary(city=city, temp_c=22.5, description="Partly cloudy with light breeze")
    logger.info(f"Returning weather summary for {city}")
    return result


# Example 3: Using dict[str, Any] for flexible schemas
@mcp.tool()
def get_weather_metrics(cities: list[str]) -> dict[str, dict[str, float]]:
    """Get weather metrics for multiple cities

    Returns a dictionary mapping city names to their metrics
    """
    logger.debug(f"get_weather_metrics called with cities={cities}")
    # Returns nested dictionaries with weather metrics
    result = {
        city: {"temperature": 20.0 + i * 2, "humidity": 60.0 + i * 5, "pressure": 1013.0 + i * 0.5}
        for i, city in enumerate(cities)
    }
    logger.info(f"Returning weather metrics for {len(cities)} cities: {', '.join(cities)}")
    return result


# Example 4: Using dataclass for weather alerts
@dataclass
class WeatherAlert:
    """Weather alert information"""

    severity: str  # "low", "medium", "high"
    title: str
    description: str
    affected_areas: list[str]
    valid_until: datetime


@mcp.tool()
def get_weather_alerts(region: str) -> list[WeatherAlert]:
    """Get active weather alerts for a region"""
    logger.debug(f"get_weather_alerts called with region={region}")
    # In production, this would fetch real alerts
    if region.lower() == "california":
        alerts = [
            WeatherAlert(
                severity="high",
                title="Heat Wave Warning",
                description="Temperatures expected to exceed 40 degrees",
                affected_areas=["Los Angeles", "San Diego", "Riverside"],
                valid_until=datetime(2024, 7, 15, 18, 0),
            ),
            WeatherAlert(
                severity="medium",
                title="Air Quality Advisory",
                description="Poor air quality due to wildfire smoke",
                affected_areas=["San Francisco Bay Area"],
                valid_until=datetime(2024, 7, 14, 12, 0),
            ),
        ]
        logger.info(f"Returning {len(alerts)} weather alerts for {region}")
        return alerts
    logger.info(f"No weather alerts for {region}")
    return []


# Example 5: Returning primitives with structured output
@mcp.tool()
def get_temperature(city: str, unit: str = "celsius") -> float:
    """Get just the temperature for a city

    When returning primitives as structured output,
    the result is wrapped in {"result": value}
    """
    logger.debug(f"get_temperature called with city={city}, unit={unit}")
    base_temp = 22.5
    if unit.lower() == "fahrenheit":
        result = base_temp * 9 / 5 + 32
        logger.info(f"Returning temperature for {city}: {result}°F")
        return result
    logger.info(f"Returning temperature for {city}: {base_temp}°C")
    return base_temp


# Example 6: Weather statistics with nested models
class DailyStats(BaseModel):
    """Statistics for a single day"""

    high: float
    low: float
    mean: float


class WeatherStats(BaseModel):
    """Weather statistics over a period"""

    location: str
    period_days: int
    temperature: DailyStats
    humidity: DailyStats
    precipitation_mm: float = Field(description="Total precipitation in millimeters")


@mcp.tool()
def get_weather_stats(city: str, days: int = 7) -> WeatherStats:
    """Get weather statistics for the past N days"""
    logger.debug(f"get_weather_stats called with city={city}, days={days}")
    result = WeatherStats(
        location=city,
        period_days=days,
        temperature=DailyStats(high=28.5, low=15.2, mean=21.8),
        humidity=DailyStats(high=85.0, low=45.0, mean=65.0),
        precipitation_mm=12.4,
    )
    logger.info(f"Returning weather stats for {city} over {days} days")
    return result
