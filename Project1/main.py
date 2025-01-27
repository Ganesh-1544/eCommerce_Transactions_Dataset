import pandas as pd
from src.data_preprocessing import load_and_clean_data, create_features, scale_features
from src.clustering import perform_customer_segmentation

def main():
    # Load and clean data
    df = load_and_clean_data('transactions.csv')
    
    # Create features
    df = create_features(df)
    
    # Optionally scale features
    df = scale_features(df, ['total_items', 'avg_order_value'])
    
    # Perform customer segmentation
    df, cluster_centers = perform_customer_segmentation(df)
    
    # Output the results
    print("DataFrame with Customer Segments:")
    print(df.head())
    print("Cluster Centers:", cluster_centers)
    # Output the results
    print("DataFrame with Customer Segments:")
    print(df.head())
    print("Cluster Centers:", cluster_centers)


if __name__ == "__main__":
    main()
