import numpy as np

def generate_sample_data():
    print("1. FAKE DATA GENERATION")
    print("=" * 50)
    
    np.random.seed(42)  # same random numbers every time -> to lessen confusions
    
    # set up our business: 365 days, 5 products, 3 sales regions
    days = np.arange(365)
    products = 5
    regions = 3
    
    # holiday season boost - sales go up near end of year
    seasonal = 1 + 0.3 * np.sin(2 * np.pi * days / 365 + np.pi)
    
    # start with random daily sales between $50-200 per product per region
    base_sales = np.random.randint(50, 200, size=(365, products, regions))
    
    # add the holiday boost to our base sales
    sales_data = base_sales * seasonal.reshape(-1, 1, 1)
    
    print(f"Generated sales data shape: {sales_data.shape}")
    print(f"Data type: {sales_data.dtype}")
    print(f"Total elements: {sales_data.size}")
    print(f"Dimensions: {sales_data.ndim}")
    
    return sales_data, days

def analyze_sales_performance(sales_data):
    print("\n2. SALES PERFORMANCE ANALYSIS")
    print("=" * 50)
    
    # add up sales different ways to see patterns
    daily_totals = np.sum(sales_data, axis=(1, 2))  # Each day's total
    
    # how well each product did overall
    product_totals = np.sum(sales_data, axis=(0, 2))
    
    # how well each region performed
    regional_totals = np.sum(sales_data, axis=(0, 1))
    
    print("SUMMARY STATISTICS:")
    print(f"Total sales: ${np.sum(sales_data):,.0f}")
    print(f"Average daily sales: ${np.mean(daily_totals):,.0f}")
    print(f"Median daily sales: ${np.median(daily_totals):,.0f}")
    print(f"Sales standard deviation: ${np.std(daily_totals):,.0f}")
    
    print(f"\nBest single day: ${np.max(daily_totals):,.0f} (Day {np.argmax(daily_totals) + 1})")
    print(f"Worst single day: ${np.min(daily_totals):,.0f} (Day {np.argmin(daily_totals) + 1})")
    
    print(f"\nProduct Rankings:")
    for i, total in enumerate(product_totals):
        print(f"  Product {i+1}: ${total:,.0f}")
    
    print(f"\nRegional Performance:")
    for i, total in enumerate(regional_totals):
        print(f"  Region {i+1}: ${total:,.0f}")
    
    return daily_totals, product_totals, regional_totals

def advanced_analysis(sales_data, daily_totals):
    print("\n3. ADVANCED ANALYTICS")
    print("=" * 50)
    
    # Group days into quarters (90 days each, skip last 5 days)
    quarterly_data = sales_data[:360].reshape(4, 90, 5, 3)
    quarterly_sales = np.sum(quarterly_data, axis=(1, 2, 3))
    
    print("QUARTERLY PERFORMANCE:")
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    for i, q_sales in enumerate(quarterly_sales):
        print(f"  {quarters[i]}: ${q_sales:,.0f}")
    
    # monthly breakdown (30 days per month)
    monthly_data = sales_data[:360].reshape(12, 30, 5, 3)
    monthly_sales = np.sum(monthly_data, axis=(1, 2, 3))
    
    # see how much we grew each month
    growth_rates = np.zeros(11)
    for i in range(11):
        growth_rates[i] = (monthly_sales[i+1] - monthly_sales[i]) / monthly_sales[i] * 100
    
    print(f"\nGROWTH ANALYSIS:")
    print(f"Average monthly growth: {np.mean(growth_rates):.1f}%")
    print(f"Best growth month: {np.max(growth_rates):.1f}%")
    print(f"Worst growth month: {np.min(growth_rates):.1f}%")
    
    # find unusually good days (more than 2 standard deviations above average)
    mean_sales = np.mean(daily_totals)
    std_sales = np.std(daily_totals)
    outliers = daily_totals[daily_totals > mean_sales + 2 * std_sales]
    
    print(f"\nOUTLIER ANALYSIS:")
    print(f"Days with exceptional performance (>2σ): {len(outliers)}")
    if len(outliers) > 0:
        print(f"Average outlier value: ${np.mean(outliers):,.0f}")
    
    return quarterly_sales, monthly_sales, growth_rates

def product_correlation_analysis(sales_data):
    print("\n4. PRODUCT CORRELATION MATRIX")
    print("=" * 50)
    
    # get daily sales for each product (combine all regions)
    product_daily_sales = np.sum(sales_data, axis=2)  # Shape: (365, 5)
    
    # build correlation matrix by hand
    n_products = product_daily_sales.shape[1]
    correlation_matrix = np.zeros((n_products, n_products))
    
    for i in range(n_products):
        for j in range(n_products):
            if i == j:
                correlation_matrix[i, j] = 1.0  # product always correlates with itself
            else:
                # math for correlation between two products
                x = product_daily_sales[:, i]
                y = product_daily_sales[:, j]
                
                x_mean = np.mean(x)
                y_mean = np.mean(y)
                
                # standard correlation formula
                numerator = np.sum((x - x_mean) * (y - y_mean))
                denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
                
                correlation_matrix[i, j] = numerator / denominator
    
    print("Correlation Matrix (Product vs Product):")
    print("Product   ", end="")
    for i in range(n_products):
        print(f"P{i+1:2d}   ", end="")
    print()
    
    for i in range(n_products):
        print(f"Product {i+1} ", end="")
        for j in range(n_products):
            print(f"{correlation_matrix[i, j]:5.2f} ", end="")
        print()
    
    # find which products are most/least related
    upper_tri = np.triu(correlation_matrix, k=1)
    max_corr_idx = np.unravel_index(np.argmax(upper_tri), upper_tri.shape)
    
    # skip zeros when finding minimum
    masked_corr = np.where(upper_tri > 0, upper_tri, np.inf)
    min_corr_idx = np.unravel_index(np.argmin(masked_corr), masked_corr.shape)
    
    print(f"\nMost related products: {max_corr_idx[0]+1} & {max_corr_idx[1]+1} "
          f"({correlation_matrix[max_corr_idx]:.3f})")
    print(f"Least related products: {min_corr_idx[0]+1} & {min_corr_idx[1]+1} "
          f"({correlation_matrix[min_corr_idx]:.3f})")
    
    return correlation_matrix

def performance_scoring(sales_data):
    print("\n5. PERFORMANCE SCORING SYSTEM")
    print("=" * 50)
    
    # daily sales by region (all products combined)
    daily_regional = np.sum(sales_data, axis=1)
    
    # standardize scores so we can compare regions fairly
    regional_means = np.mean(daily_regional, axis=0)
    regional_stds = np.std(daily_regional, axis=0)
    
    # convert to z-scores (how many standard deviations from average)
    normalized_scores = (daily_regional - regional_means) / regional_stds
    
    # turn z-scores into 0-100 scale centered at 50
    performance_scores = 50 + 10 * normalized_scores
    
    # keep scores between 0 and 100
    performance_scores = np.round(np.clip(performance_scores, 0, 100))
    
    print("REGIONAL PERFORMANCE SCORES (0-100 scale):")
    for region in range(3):
        avg_score = np.mean(performance_scores[:, region])
        max_score = np.max(performance_scores[:, region])
        min_score = np.min(performance_scores[:, region])
        
        print(f"Region {region+1}:")
        print(f"  Average: {avg_score:.1f}")
        print(f"  Best day: {max_score:.0f}")
        print(f"  Worst day: {min_score:.0f}")
    
    # find our best days overall
    total_daily_scores = np.sum(performance_scores, axis=1)
    top_days_indices = np.argsort(total_daily_scores)[-5:]  # Last 5 = highest 5
    
    print(f"\nTOP 5 PERFORMING DAYS:")
    for i, day_idx in enumerate(reversed(top_days_indices)):
        print(f"  #{i+1}: Day {day_idx+1} (Score: {total_daily_scores[day_idx]:.0f})")
    
    return performance_scores

def data_export_simulation():
    print("\n6. DATA EXPORT SIMULATION")
    print("=" * 50)
    
    # summary table
    summary_data = np.array([
        [1, 1250000, 87.5],  # product 1: ID, Total Sales, Avg Score
        [2, 1180000, 82.3],  # Product 2
        [3, 1340000, 91.2],  # Product 3
        [4, 1090000, 79.8],  # Product 4
        [5, 1420000, 94.1]   # Product 5
    ])
    
    print("EXPORT-READY SUMMARY DATA:")
    print("Product ID | Total Sales | Avg Performance")
    print("-" * 45)
    for row in summary_data:
        print(f"    {row[0]:.0f}     | ${row[1]:,.0f}    |     {row[2]:.1f}")
    
    # split the table into separate arrays for analysis
    product_ids = summary_data[:, 0].astype(int)
    total_sales = summary_data[:, 1]
    avg_scores = summary_data[:, 2]
    
    # rank products by combining sales volume and performance
    combined_metric = total_sales * (avg_scores / 100)
    rankings = np.argsort(combined_metric)[::-1] + 1  # Flip to descending order
    
    print(f"\nPRODUCT RANKINGS (Sales × Performance):")
    for i, rank in enumerate(rankings):
        product_idx = np.where(rankings == rank)[0][0]
        print(f"  #{rank}: Product {product_ids[product_idx]} "
              f"(${total_sales[product_idx]:,.0f}, {avg_scores[product_idx]:.1f}%)")
    
    return summary_data

def main():
    print("NUMPY SALES DATA ANALYSIS PROJECT")
    print("=" * 50)
    print("Real-world data analysis using NumPy\n")
    
    # step 1: Create our dataset (set seed)
    sales_data, days = generate_sample_data()
    
    # step 2: Basic stats & breakdowns 
    daily_totals, product_totals, regional_totals = analyze_sales_performance(sales_data)
    
    # step 3: Time based analysis 
    quarterly_sales, monthly_sales, growth_rates = advanced_analysis(sales_data, daily_totals)
    
    # step 4: Product relations
    correlation_matrix = product_correlation_analysis(sales_data)
    
    # step 5: Performance scoring (sales)
    performance_scores = performance_scoring(sales_data)
    
    # step 6: Summary 
    summary_data = data_export_simulation()
    
    # final insights
    print("\n7. KEY INSIGHTS")
    print("=" * 50)
    
    # which quarter was best
    best_quarter = np.argmax(quarterly_sales) + 1
    quarter_growth = (quarterly_sales[-1] - quarterly_sales[0]) / quarterly_sales[0] * 100
    
    # which product has the most ups and downs -> from data
    most_volatile_product = np.argmax(np.std(np.sum(sales_data, axis=2), axis=0)) + 1
    
    # which region is most reliable ?
    regional_daily = np.sum(sales_data, axis=1)
    regional_cv = np.std(regional_daily, axis=0) / np.mean(regional_daily, axis=0)
    most_consistent_region = np.argmin(regional_cv) + 1
    
    print(f"• Best performing quarter: Q{best_quarter}")
    print(f"• Q4 vs Q1 growth: {quarter_growth:.1f}%")
    print(f"• Most unpredictable product: Product {most_volatile_product}")
    print(f"• Most reliable region: Region {most_consistent_region}")
    
    # Show top revenue makers
    top_products = np.argsort(product_totals)[-2:]  # Get indices of top 2
    print(f"• Revenue leaders: Products {top_products + 1}")
    
if __name__ == "__main__":
    main()