from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perform_customer_segmentation(df, n_clusters=4):
    """Perform customer segmentation using K-means clustering"""
    # Select features for clustering
    features = ['total_items', 'avg_order_value']
    X = df[features]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['customer_segment'] = kmeans.fit_predict(X_scaled)
    
    return df, kmeans.cluster_centers_