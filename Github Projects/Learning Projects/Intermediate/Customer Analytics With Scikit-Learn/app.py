import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

np.random.seed(67) 

def generate_company_data():
    customers = []
    
    customer_types = ['Startup', 'SMB', 'Enterprise'] # To differentiate results 
    
    for i in range(1000):
        cust_type = np.random.choice(customer_types, p=[0.5, 0.3, 0.2])
        
        if cust_type == 'Startup':
            monthly_spend = np.random.normal(250, 75)
            usage_hours = np.random.normal(80, 25)
            support_tickets = np.random.poisson(2)
        elif cust_type == 'SMB':
            monthly_spend = np.random.normal(850, 200)
            usage_hours = np.random.normal(200, 50)
            support_tickets = np.random.poisson(5)
        else:
            monthly_spend = np.random.normal(2500, 500)
            usage_hours = np.random.normal(500, 100)
            support_tickets = np.random.poisson(12)
        
        monthly_spend = max(50, monthly_spend)
        usage_hours = max(10, usage_hours)
        
        customers.append({
            'customer_id': f'CUST_{i+1:04d}',
            'customer_type': cust_type,
            'monthly_spend': round(monthly_spend, 2),
            'usage_hours': round(usage_hours, 1),
            'support_tickets': max(0, support_tickets),
            'account_age_months': np.random.randint(1, 36),
            'has_premium': np.random.choice([0, 1], p=[0.7, 0.3])
        })
    
    return pd.DataFrame(customers)

def analyze_spending(df):
    print("\nSPENDING ANALYSIS")
    print("-" * 40)
    
    avg_spend = df['monthly_spend'].mean()
    median_spend = df['monthly_spend'].median()
    
    print(f"Average customer spend: ${avg_spend:.2f}/month")
    print(f"Median customer spend: ${median_spend:.2f}/month")
    
    type_spending = df.groupby('customer_type')['monthly_spend'].agg(['mean', 'count'])
    print(f"\nBy customer type:")
    for ctype in type_spending.index:
        avg = type_spending.loc[ctype, 'mean']
        count = type_spending.loc[ctype, 'count']
        print(f"  {ctype}: ${avg:.0f} avg ({count} customers)")
    
    premium_analysis = df.groupby('has_premium')['monthly_spend'].mean()
    regular_spend = premium_analysis[0]
    premium_spend = premium_analysis[1]
    
    print(f"\nPremium vs Regular:")
    print(f"  Regular: ${regular_spend:.0f}")
    print(f"  Premium: ${premium_spend:.0f} ({premium_spend/regular_spend:.1f}x more)")
    
    return avg_spend, type_spending

def check_usage_patterns(df):
    print("\nUSAGE PATTERNS")
    print("-" * 40)
    
    avg_usage = df['usage_hours'].mean()
    high_usage = df[df['usage_hours'] > df['usage_hours'].quantile(0.8)]
    
    print(f"Average usage: {avg_usage:.1f} hours/month")
    print(f"Top 20% users: {high_usage['usage_hours'].mean():.1f} hours")
    
    avg_tickets = df['support_tickets'].mean()
    high_support = df[df['support_tickets'] > 5]
    
    print(f"\nSupport tickets:")
    print(f"  Average: {avg_tickets:.1f} per month")
    print(f"  High support users: {len(high_support)} customers ({len(high_support)/len(df)*100:.1f}%)")
    
    spend_usage_corr = df['monthly_spend'].corr(df['usage_hours'])
    print(f"\nSpending-Usage correlation: {spend_usage_corr:.2f}")
    
    return avg_usage, spend_usage_corr

def segment_customers(df):
    print("\nCUSTOMER SEGMENTATION")
    print("-" * 40)
    
    features = ['monthly_spend', 'usage_hours', 'support_tickets', 'account_age_months']
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])
    
    best_score = -1
    best_k = 2
    
    for k in range(2, 7):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(scaled_data)
        score = silhouette_score(scaled_data, labels)
        
        if score > best_score:
            best_score = score
            best_k = k
    
    kmeans = KMeans(n_clusters=best_k, random_state=42)
    df['segment'] = kmeans.fit_predict(scaled_data)
    
    print(f"Found {best_k} customer segments")
    print(f"Silhouette score: {best_score:.2f}")
    
    segment_summary = df.groupby('segment').agg({
        'monthly_spend': 'mean',
        'usage_hours': 'mean',
        'support_tickets': 'mean',
        'customer_id': 'count'
    }).round(1)
    
    segment_summary.columns = ['Avg_Spend', 'Avg_Usage', 'Avg_Tickets', 'Count']
    
    print(f"\nSegment details:")
    for seg in segment_summary.index:
        row = segment_summary.loc[seg]
        print(f"  Segment {seg}: {row['Count']} customers")
        print(f"    ${row['Avg_Spend']}/mo, {row['Avg_Usage']}hrs, {row['Avg_Tickets']} tickets")
        
        if row['Avg_Spend'] > 1500:
            print(f"    Type: High value")
        elif row['Avg_Usage'] > 300:
            print(f"    Type: Power users")
        elif row['Avg_Tickets'] > 8:
            print(f"    Type: Support heavy")
        else:
            print(f"    Type: Standard")
    
    return best_k, segment_summary

def make_charts(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # spending histogram
    axes[0,0].hist(df['monthly_spend'], bins=30, color='skyblue', alpha=0.7)
    axes[0,0].set_title('Monthly Spending Distribution')
    axes[0,0].set_xlabel('Monthly Spend ($)')
    axes[0,0].set_ylabel('Number of Customers')
    axes[0,0].axvline(df['monthly_spend'].mean(), color='red', linestyle='--', label='Average')
    axes[0,0].legend()
    
    # customer types pie
    type_counts = df['customer_type'].value_counts()
    axes[0,1].pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', 
                  colors=['lightcoral', 'gold', 'lightgreen'])
    axes[0,1].set_title('Customer Type Breakdown')
    
    # usage vs spending
    scatter = axes[1,0].scatter(df['usage_hours'], df['monthly_spend'], 
                               c=df['segment'], cmap='viridis', alpha=0.6)
    axes[1,0].set_xlabel('Usage Hours per Month')
    axes[1,0].set_ylabel('Monthly Spend ($)')
    axes[1,0].set_title('Usage vs Spending by Segment')
    plt.colorbar(scatter, ax=axes[1,0])
    
    # segment spending comparison
    segment_spending = df.groupby('segment')['monthly_spend'].mean()
    bars = axes[1,1].bar(range(len(segment_spending)), segment_spending.values, 
                        color=['red', 'blue', 'green', 'orange'][:len(segment_spending)])
    axes[1,1].set_title('Average Spending by Segment')
    axes[1,1].set_xlabel('Segment Number')
    axes[1,1].set_ylabel('Average Monthly Spend ($)')
    axes[1,1].set_xticks(range(len(segment_spending)))
    
    # add value labels on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        axes[1,1].text(bar.get_x() + bar.get_width()/2., height + 20,
                      f'${height:.0f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def business_summary(df, avg_spend, segment_summary):
    print("\nBUSINESS INSIGHTS")
    print("=" * 40)
    
    total_revenue = df['monthly_spend'].sum()
    print(f"\nRevenue metrics:")
    print(f"  Monthly revenue: ${total_revenue:,.0f}")
    print(f"  Average per customer: ${avg_spend:.0f}")
    print(f"  Annual customer value: ${avg_spend*12:,.0f}")
    
    enterprise_pct = (df['customer_type'] == 'Enterprise').mean() * 100
    premium_pct = df['has_premium'].mean() * 100
    
    print(f"\nCustomer composition:")
    print(f"  Enterprise customers: {enterprise_pct:.1f}%")
    print(f"  Premium users: {premium_pct:.1f}%")
    
    best_segment = segment_summary.loc[segment_summary['Avg_Spend'].idxmax()]
    print(f"\nTop segment performance:")
    print(f"  {best_segment['Count']} customers")
    print(f"  ${best_segment['Avg_Spend']:.0f} average spend")
    print(f"  Revenue contribution: ${best_segment['Avg_Spend'] * best_segment['Count']:,.0f}/month")
    
    high_support = df[df['support_tickets'] > 8]
    if len(high_support) > 0:
        print(f"\nSupport risk:")
        print(f"  {len(high_support)} customers with high support needs")
        print(f"  Their average spend: ${high_support['monthly_spend'].mean():.0f}")
    
    # quick recommendations
    print(f"\nRecommendations:")
    if enterprise_pct < 25:
        print(f"  - Target more enterprise customers (higher value)")
    if premium_pct < 40:
        print(f"  - Push premium upgrades (significant revenue boost)")
    print(f"  - Focus retention on segment {segment_summary['Avg_Spend'].idxmax()} (highest value)")

def main():
    print("TechFlow Customer Analytics")
    print("=" * 30)
    
    print("Generating data...")
    df = generate_company_data()
    print(f"Loaded {len(df)} customers")
    
    avg_spend, type_breakdown = analyze_spending(df)
    avg_usage, correlation = check_usage_patterns(df)
    num_segments, segments = segment_customers(df)
    
    make_charts(df)
    business_summary(df, avg_spend, segments)
    
    save_data = input("\nSave results? (y/n): ").lower().strip()
    
    if save_data in ['y', 'yes']:
        df.to_csv('customer_data.csv', index=False)
        segments.to_csv('segments.csv')
        plt.savefig('analytics.png', dpi=300, bbox_inches='tight')
        print("Files saved")
    else:
        print("Done")

if __name__ == "__main__":
    main()