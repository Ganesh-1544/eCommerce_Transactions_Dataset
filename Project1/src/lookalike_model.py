from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class LookalikeModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def prepare_features(self, df, target_segment):
        """Prepare features for lookalike modeling"""
        feature_cols = ['total_items', 'avg_order_value', 'hour', 
                       'day_of_week', 'month']
        X = df[feature_cols]
        y = (df['customer_segment'] == target_segment).astype(int)
        return X, y
        
    def train(self, X, y):
        """Train the lookalike model"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        
        print("Model Performance:")
        print(classification_report(y_test, y_pred))
        
        return self.model
        
    def predict_lookalikes(self, X):
        """Predict lookalike customers"""
        return self.model.predict_proba(X)[:, 1]