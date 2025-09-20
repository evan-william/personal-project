# NumPy Sales Data Analysis

A Python project demonstrating multi-dimensional array operations and statistical analysis using NumPy for business sales data.

## What It Does

This is a data analysis script I built to practice advanced NumPy operations with realistic business scenarios. The program generates synthetic sales data for a company with 5 products across 3 regions over a full year, then performs various statistical analyses to extract business insights.

Built this to understand how NumPy handles complex multi-dimensional data and to practice statistical operations without relying on pandas or other high-level libraries.

## Features

* Generates 3D sales data array (365 days × 5 products × 3 regions)
* Implements seasonal sales patterns and random variations
* Calculates daily, monthly, and quarterly performance metrics
* Computes product correlation matrices
* Regional performance scoring system
* Time series analysis with trend identification
* Statistical operations using pure NumPy

## Project Structure

```
numpy-sales-analysis/
├── sales_analysis.py   # Main analysis script
└── README.md          # This file
```

## Requirements

* Python 3.x
* NumPy library

Install the required package:

```bash
pip install numpy
```

## How to Run

Execute the analysis:

```bash
python sales_analysis.py
```

The script will output 7 sections of analysis demonstrating different NumPy techniques and business insights.

## How It Works

The program creates a 3D NumPy array representing sales data, then applies various array operations:
* Uses broadcasting to add seasonal patterns to base sales data
* Performs axis-specific aggregations for different time periods
* Calculates correlation coefficients manually using NumPy operations
* Implements z-score normalization for performance scoring
* Demonstrates advanced indexing and reshaping techniques

## What I Learned

* Working with multi-dimensional NumPy arrays
* Understanding axis parameters in aggregation functions
* Array broadcasting for applying patterns across dimensions
* Manual implementation of statistical calculations
* Vectorized operations for performance optimization
* Complex array indexing and slicing techniques
* Time series data manipulation with NumPy

## Sample Output

The script produces structured analysis output showing:
1. Data generation summary
2. Sales performance breakdowns
3. Advanced analytics results
4. Product correlation matrices
5. Regional scoring systems
6. Export simulation data
7. Key business insights

## Known Issues

* Uses synthetic data rather than real business data
* Basic seasonal pattern modeling
* Limited to predefined analysis types
* No data visualization components
* Simple random number generation

## Possible Improvements

Could add:
* More sophisticated seasonal modeling
* Integration with matplotlib for visualizations
* Real-world data import capabilities
* More advanced statistical methods
* Performance benchmarking comparisons
* Export to different file formats
* Interactive analysis options

## Author

**Evan William** - Version 1.0 (2025)

Made this to dive deeper into NumPy's capabilities beyond basic array operations. It helped me understand how to structure complex data analysis workflows using only NumPy's core functionality.

This was my first project working with 3D arrays and advanced statistical operations, so the focus is only on demonstrating core concepts.

*Learning project - designed to explore NumPy's data analysis capabilities in business contexts.*
