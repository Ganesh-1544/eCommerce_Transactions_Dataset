import pandas as pd
import gdown

def download_csv_files():
    """Download CSV files from Google Drive."""
    file_links = {
        'customers.csv': 'https://drive.google.com/uc?id=1bu_--mo79VdUG9oin4ybfFGRUSXAe-WE',
        'products.csv': 'https://drive.google.com/uc?id=1IKuDizVapw-hyktwfpoAoaGtHtTNHfd0',
        'transactions.csv': 'https://drive.google.com/uc?id=1saEqdbBB-vuk2hxoAf4TzDEsykdKlzbF'
    }

    for file_name, url in file_links.items():
        gdown.download(url, file_name, quiet=False)

def merge_csv_files():
    """Merge CSV files into ecommerce_data.csv."""
    try:
        # Load the data with proper parameters
        customers = pd.read_csv('customers.csv', encoding='utf-8', on_bad_lines='skip')
        products = pd.read_csv('products.csv', encoding='utf-8', on_bad_lines='skip')
        transactions = pd.read_csv('transactions.csv', encoding='utf-8', on_bad_lines='skip')

        # Merge data
        merged = transactions.merge(customers, on='CustomerID', how='left')
        merged = merged.merge(products, on='ProductID', how='left')

        # Save the final merged DataFrame
        merged.to_csv('ecommerce_data.csv', index=False)
        print("Merged file saved as ecommerce_data.csv")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Step 1: Download files
    download_csv_files()
    
    # Step 2: Merge files
    merge_csv_files()
