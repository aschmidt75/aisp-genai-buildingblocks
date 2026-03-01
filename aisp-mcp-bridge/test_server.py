"""Test script to verify the Weather MCP Server tools work correctly"""

import json
from datetime import datetime

from src.weather_server import (
    get_weather,
    get_weather_summary,
    get_weather_metrics,
    get_weather_alerts,
    get_temperature,
    get_weather_stats,
)


def test_get_weather():
    """Test get_weather tool"""
    print("\n" + "=" * 80)
    print("Testing get_weather")
    print("=" * 80)
    result = get_weather("London")
    print(f"Result type: {type(result)}")
    print(f"Result: {result}")
    if hasattr(result, "model_dump"):
        print(json.dumps(result.model_dump(), indent=2, default=str))


def test_get_weather_summary():
    """Test get_weather_summary tool"""
    print("\n" + "=" * 80)
    print("Testing get_weather_summary")
    print("=" * 80)
    result = get_weather_summary("Paris")
    print(f"Result type: {type(result)}")
    print(json.dumps(result, indent=2, default=str))


def test_get_weather_metrics():
    """Test get_weather_metrics tool"""
    print("\n" + "=" * 80)
    print("Testing get_weather_metrics")
    print("=" * 80)
    result = get_weather_metrics(["Tokyo", "Sydney", "Mumbai"])
    print(f"Result type: {type(result)}")
    print(json.dumps(result, indent=2, default=str))


def test_get_weather_alerts():
    """Test get_weather_alerts tool"""
    print("\n" + "=" * 80)
    print("Testing get_weather_alerts")
    print("=" * 80)
    result = get_weather_alerts("California")
    print(f"Result type: {type(result)}")
    print(f"Number of alerts: {len(result)}")
    for alert in result:
        print(f"\nAlert: {alert.title}")
        print(f"  Severity: {alert.severity}")
        print(f"  Description: {alert.description}")
        print(f"  Affected areas: {', '.join(alert.affected_areas)}")
        print(f"  Valid until: {alert.valid_until}")


def test_get_temperature():
    """Test get_temperature tool"""
    print("\n" + "=" * 80)
    print("Testing get_temperature")
    print("=" * 80)
    result_c = get_temperature("Berlin", "celsius")
    result_f = get_temperature("Berlin", "fahrenheit")
    print(f"Temperature in Celsius: {result_c}°C")
    print(f"Temperature in Fahrenheit: {result_f}°F")


def test_get_weather_stats():
    """Test get_weather_stats tool"""
    print("\n" + "=" * 80)
    print("Testing get_weather_stats")
    print("=" * 80)
    result = get_weather_stats("Seattle", 30)
    print(f"Result type: {type(result)}")
    print(f"Result: {result}")
    if hasattr(result, "model_dump"):
        print(json.dumps(result.model_dump(), indent=2, default=str))


if __name__ == "__main__":
    print("\nTesting Weather Service Tools (Direct Function Calls)\n")
    
    test_get_weather()
    test_get_weather_summary()
    test_get_weather_metrics()
    test_get_weather_alerts()
    test_get_temperature()
    test_get_weather_stats()
    
    print("\n" + "=" * 80)
    print("All tests completed successfully!")
    print("=" * 80)
