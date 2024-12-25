from typing import List, TypedDict


class DataPoint(TypedDict):
    price: float
    timestamp: float


def is_convex(data: List[DataPoint]) -> bool:
    """
    Check if price curve forms a convex shape (rate of increase is increasing).

    Args:
        data: List of data points containing 'price' and 'timestamp' values

    Returns:
        bool: True if price curve is convex, False otherwise
    """
    if len(data) < 3:
        return True

    # Sort data points by timestamp
    sorted_points = sorted(data, key=lambda x: x["timestamp"])

    # Calculate slopes between consecutive points
    slopes = []
    for i in range(1, len(sorted_points)):
        time_diff = sorted_points[i]["timestamp"] - sorted_points[i - 1]["timestamp"]
        price_diff = sorted_points[i]["price"] - sorted_points[i - 1]["price"]

        # Avoid division by zero
        if time_diff == 0:
            raise ValueError("Duplicate timestamp found")

        slopes.append(price_diff / time_diff)

    # Check if slopes are increasing (convex property)
    for i in range(1, len(slopes)):
        if slopes[i] <= slopes[i - 1]:
            return False

    return True


def is_concave(data: List[DataPoint]) -> bool:
    """
    Check if price curve forms a concave shape (rate of increase is decreasing).

    Args:
        data: List of data points containing 'price' and 'timestamp' values

    Returns:
        bool: True if price curve is concave, False otherwise
    """
    if len(data) < 3:
        return True

    # Sort data points by timestamp
    sorted_points = sorted(data, key=lambda x: x["timestamp"])

    # Calculate slopes between consecutive points
    slopes = []
    for i in range(1, len(sorted_points)):
        time_diff = sorted_points[i]["timestamp"] - sorted_points[i - 1]["timestamp"]
        price_diff = sorted_points[i]["price"] - sorted_points[i - 1]["price"]

        # Avoid division by zero
        if time_diff == 0:
            raise ValueError("Duplicate timestamp found")

        slopes.append(price_diff / time_diff)

    # Check if slopes are decreasing (concave property)
    for i in range(1, len(slopes)):
        if slopes[i] >= slopes[i - 1]:
            return False

    return True


def is_increasing(data: List[DataPoint]) -> bool:
    """
    Check if prices are strictly increasing over time.

    Args:
        data: List of data points containing 'price' and 'timestamp' values

    Returns:
        bool: True if prices are strictly increasing, False otherwise
    """
    if len(data) < 2:
        return True

    # Sort data points by timestamp to ensure chronological order
    sorted_points = sorted(data, key=lambda x: x["timestamp"])

    # Check if each price is greater than the previous one
    for i in range(1, len(sorted_points)):
        if sorted_points[i]["price"] <= sorted_points[i - 1]["price"]:
            return False

    return True


def is_decreasing(data: List[DataPoint]) -> bool:
    """
    Check if prices are strictly decreasing over time.

    Args:
        data: List of data points containing 'price' and 'timestamp' values

    Returns:
        bool: True if prices are strictly decreasing, False otherwise
    """
    if len(data) < 2:
        return True

    # Sort data points by timestamp to ensure chronological order
    sorted_points = sorted(data, key=lambda x: x["timestamp"])

    # Check if each price is less than the previous one
    for i in range(1, len(sorted_points)):
        if sorted_points[i]["price"] >= sorted_points[i - 1]["price"]:
            return False

    return True
