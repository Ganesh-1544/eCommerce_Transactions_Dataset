# from src.data_preprocessing import load_and_clean_data, create_features, scale_features
# from src.eda import plot_purchase_patterns, customer_segmentation_analysis
# from src.lookalike_model import LookalikeModel
# from src.clustering import perform_customer_segmentation

# def main():
#     # Load and preprocess data
#     df = load_and_clean_data('ecommerce_data.csv')
#     df = create_features(df)
    
#     # Perform EDA
#     plot_purchase_patterns(df)
#     customer_segmentation_analysis(df)
    
#     # Customer segmentation
#     features_to_scale = ['total_items', 'avg_order_value']
#     df = scale_features(df, features_to_scale)
#     df, cluster_centers = perform_customer_segmentation(df)
    
#     # Train lookalike model
#     lookalike_model = LookalikeModel()
#     X, y = lookalike_model.prepare_features(df, target_segment=1)
#     model = lookalike_model.train(X, y)
    
# if __name__ == "__main__":
#     main()


from src.data_preprocessing import load_and_clean_data, create_features, scale_features
from src.eda import plot_purchase_patterns, customer_segmentation_analysis
from src.lookalike_model import LookalikeModel
from src.clustering import perform_customer_segmentation
from src.download_merge import download_csv_files, merge_csv_files  # Add this import

def main():
    # Step 1: Download and merge data
    download_csv_files()
    merge_csv_files()
    
    # Step 2: Load and preprocess data
    df = load_and_clean_data('ecommerce_data.csv')
    df = create_features(df)
    
    # Step 3: Perform EDA
    plot_purchase_patterns(df)
    customer_segmentation_analysis(df)
    
    # Step 4: Customer segmentation
    features_to_scale = ['total_items', 'avg_order_value']
    df = scale_features(df, features_to_scale)
    df, cluster_centers = perform_customer_segmentation(df)
    
    # Step 5: Train lookalike model
    lookalike_model = LookalikeModel()
    X, y = lookalike_model.prepare_features(df, target_segment=1)
    model = lookalike_model.train(X, y)
    
if __name__ == "__main__":
    main()
