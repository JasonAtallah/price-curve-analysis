# Price Curve Analysis

A Python package for analyzing price-time series data to determine curve characteristics such as convexity, concavity, and monotonicity.

## Features

- Check if a price curve is convex (increasing rate of change)
- Check if a price curve is concave (decreasing rate of change)
- Verify if prices are strictly increasing
- Verify if prices are strictly decreasing
- Handles unsorted time series data
- Type-safe with TypedDict support

## Installation

Clone this repository:
```bash
git clone https://github.com/JasonAtallah/price-curve-analysis.git
cd price-curve-analysis
```
> Will add to pypi later

## Usage

The package provides four main functions for analyzing price curves:

```python
from main import is_convex, is_concave, is_increasing, is_decreasing

# Example data points
data = [
    {"price": 1.0, "timestamp": 0.0},
    {"price": 2.0, "timestamp": 1.0},
    {"price": 4.0, "timestamp": 2.0},
]

# Check curve properties
is_convex(data)      # Returns True
is_concave(data)     # Returns False
is_increasing(data)  # Returns True
is_decreasing(data)  # Returns False
```

### Data Format

Each data point should be a dictionary with two keys:
- `price`: float value representing the price
- `timestamp`: float value representing the time

### Function Descriptions

#### `is_convex(data)`
Checks if the price curve forms a convex shape (rate of increase is increasing).

#### `is_concave(data)`
Checks if the price curve forms a concave shape (rate of increase is decreasing).

#### `is_increasing(data)`
Verifies if prices are strictly increasing over time.

#### `is_decreasing(data)`
Verifies if prices are strictly decreasing over time.

### Special Cases

- Empty lists or single data points return `True` for all functions
- Duplicate timestamps raise a `ValueError`
- Equal prices return `False` for `is_increasing` and `is_decreasing`
- Data points can be provided in any order (timestamps will be sorted internally)

## Testing

The package includes comprehensive tests. To run the tests:

```bash
pytest main_test.py
```