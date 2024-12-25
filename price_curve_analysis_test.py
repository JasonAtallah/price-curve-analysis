import pytest
from price_curve_analysis import is_convex, is_concave, is_increasing, is_decreasing

# Test data
convex_data = [
    {"price": 1.0, "timestamp": 0.0},
    {"price": 2.0, "timestamp": 1.0},
    {"price": 4.0, "timestamp": 2.0},  # Increasing slope
]

concave_data = [
    {"price": 1.0, "timestamp": 0.0},
    {"price": 3.0, "timestamp": 1.0},
    {"price": 4.0, "timestamp": 2.0},  # Decreasing slope
]

increasing_data = [
    {"price": 1.0, "timestamp": 0.0},
    {"price": 2.0, "timestamp": 1.0},
    {"price": 3.0, "timestamp": 2.0},
]

decreasing_data = [
    {"price": 3.0, "timestamp": 0.0},
    {"price": 2.0, "timestamp": 1.0},
    {"price": 1.0, "timestamp": 2.0},
]


def test_is_convex():
    assert is_convex(convex_data) == True
    assert is_convex(concave_data) == False
    assert is_convex([]) == True
    assert is_convex([{"price": 1.0, "timestamp": 0.0}]) == True

    # Test with duplicate timestamp
    duplicate_timestamp = [
        {"price": 1.0, "timestamp": 0.0},
        {"price": 2.0, "timestamp": 0.0},  # Same timestamp
        {"price": 4.0, "timestamp": 1.0},
    ]
    with pytest.raises(ValueError, match="Duplicate timestamp found"):
        is_convex(duplicate_timestamp)


def test_is_concave():
    assert is_concave(concave_data) == True
    assert is_concave(convex_data) == False
    assert is_concave([]) == True
    assert is_concave([{"price": 1.0, "timestamp": 0.0}]) == True

    # Test with duplicate timestamp
    duplicate_timestamp = [
        {"price": 1.0, "timestamp": 0.0},
        {"price": 2.0, "timestamp": 0.0},  # Same timestamp
        {"price": 4.0, "timestamp": 1.0},
    ]
    with pytest.raises(ValueError, match="Duplicate timestamp found"):
        is_concave(duplicate_timestamp)


def test_is_increasing():
    assert is_increasing(increasing_data) == True
    assert is_increasing(decreasing_data) == False
    assert is_increasing([]) == True
    assert is_increasing([{"price": 1.0, "timestamp": 0.0}]) == True

    # Test with equal prices
    equal_prices = [
        {"price": 1.0, "timestamp": 0.0},
        {"price": 1.0, "timestamp": 1.0},  # Same price
    ]
    assert is_increasing(equal_prices) == False


def test_is_decreasing():
    assert is_decreasing(decreasing_data) == True
    assert is_decreasing(increasing_data) == False
    assert is_decreasing([]) == True
    assert is_decreasing([{"price": 1.0, "timestamp": 0.0}]) == True

    # Test with equal prices
    equal_prices = [
        {"price": 1.0, "timestamp": 0.0},
        {"price": 1.0, "timestamp": 1.0},  # Same price
    ]
    assert is_decreasing(equal_prices) == False


def test_unsorted_data():
    # Test that functions work with unsorted data
    unsorted_convex = [
        {"price": 4.0, "timestamp": 2.0},
        {"price": 1.0, "timestamp": 0.0},
        {"price": 2.0, "timestamp": 1.0},
    ]
    assert is_convex(unsorted_convex) == True

    unsorted_increasing = [
        {"price": 3.0, "timestamp": 2.0},
        {"price": 1.0, "timestamp": 0.0},
        {"price": 2.0, "timestamp": 1.0},
    ]
    assert is_increasing(unsorted_increasing) == True
