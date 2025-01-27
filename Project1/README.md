# eCommerce Data Analysis Project

This project is designed to analyze eCommerce transaction data to derive insights about customer behavior and sales patterns. It includes data preprocessing, exploratory data analysis (EDA), customer segmentation, and the development of a lookalike model for targeted marketing.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ecommerce-data-analysis.git
   cd ecommerce-data-analysis
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main script**:
   ```bash
   python main.py
   ```

   This will download the necessary data files, preprocess the data, perform exploratory data analysis, and execute customer segmentation.

## Expected Output

- **Data Download**: The project will download the necessary CSV files containing customer, product, and transaction data.
- **Merged Data**: A merged file named `ecommerce_data.csv` will be created, containing all relevant transaction data.
- **Exploratory Data Analysis (EDA)**: The `plot_purchase_patterns` function will generate a bar chart visualizing total sales by day of the week.
- **Customer Segmentation**: The project will perform customer segmentation based on purchasing behavior, which can be further analyzed.
- **Lookalike Model**: A trained lookalike model will be generated, which can be used for targeted marketing strategies.

## Usage

- The main script `main.py` orchestrates the entire process, including downloading data, preprocessing, and analysis.
- The `src/eda.py` file contains functions for exploratory data analysis, such as `plot_purchase_patterns`, which visualizes sales data.
- The `src/data_preprocessing.py` file includes functions for loading and cleaning the data, as well as feature engineering.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
