# Customer Analytics Project

A customer segmentation analysis project using scikit-learn to explore machine learning clustering and business analytics concepts.

## Overview

This project was built to practice customer analytics and machine learning clustering techniques. It simulates a SaaS company scenario (TechFlow Inc) to explore how data science can help understand customer behavior and spending patterns.

The main goal was to learn how to implement K-means clustering, evaluate model performance, and translate technical results into business insights that could actually be useful.

## What I Learned

- **K-means Clustering**: Implementing customer segmentation with automatic cluster optimization
- **Feature Engineering**: Creating meaningful metrics from raw customer data
- **Model Evaluation**: Using silhouette scores to assess clustering quality
- **Data Visualization**: Building charts that communicate insights clearly
- **Business Translation**: Converting ML results into actionable recommendations

## Technical Stack

- **Python**: Core programming language
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization

### Key Concepts Applied
```python
# Customer segmentation features
features = [
    'monthly_spend',      # How much they pay
    'usage_hours',        # How much they use the product
    'support_tickets',    # How much help they need
    'account_age_months'  # How long they've been customers
]
```

## How It Works

The project simulates three types of SaaS customers:
- **Startups**: Smaller budgets, around $250/month
- **SMBs**: Mid-size businesses, around $850/month  
- **Enterprise**: Large companies, around $2,500/month

Then it uses machine learning to discover these patterns automatically and see what insights emerge.

## Installation & Setup

```bash
# Clone the project
git clone https://github.com/username/customer-analytics.git
cd customer-analytics

# Install required packages
pip install numpy pandas matplotlib scikit-learn

# Run the analysis
python company_analytics.py
```

## Requirements

- Python 3.8 or higher
- NumPy, Pandas, Matplotlib, Scikit-learn

## Sample Output

When you run the analysis, you'll see something like:

```
SPENDING ANALYSIS
Average customer spend: $743.50/month

By customer type:
  Enterprise: $2,491 avg (201 customers)
  SMB: $847 avg (301 customers)  
  Startup: $251 avg (498 customers)

CUSTOMER SEGMENTATION
Found 3 customer segments
Silhouette score: 0.67

Segment 0: 334 customers
  $2,401/mo, 487hrs, 11 tickets
  Type: High value
```

Plus some helpful charts showing:
- Customer spending distribution
- Usage vs spending patterns
- Segment comparisons

## What I Found Interesting

- The clustering algorithm naturally separates customers by value tier
- Usage hours correlate pretty well with spending (makes sense)
- Some customers need way more support than others
- You can actually predict which customers might be worth focusing retention efforts on

## Project Structure

```
company_analytics.py
├── generate_company_data()    # Creates realistic fake data
├── analyze_spending()         # Basic revenue analysis
├── check_usage_patterns()     # Looks for behavioral patterns
├── segment_customers()        # The ML clustering part
├── make_charts()             # Visualization
└── business_summary()        # Translates results to insights
```

## Things I'd Improve

- Try other clustering algorithms 
- Implement churn prediction
- Build a simple web interface

## Configuration

You can tweak the data generation if you want to experiment:

```python
# In generate_company_data()
customer_types = ['Startup', 'SMB', 'Enterprise']
type_probabilities = [0.5, 0.3, 0.2]  # Adjust mix

# Change average spending patterns
startup_avg_spend = 250
smb_avg_spend = 850
enterprise_avg_spend = 2500
```

## Author

**Evan William** 
Version 1.0 (2025)

Built this to practice customer analytics and machine learning concepts. It's been a great way to understand how clustering algorithms work and how to apply them to real business problems.

Still learning, so if you spot any issues or have suggestions for improvement, I'd appreciate the feedback!

---

*Feel free to fork, modify, or use this for your own learning projects.*
