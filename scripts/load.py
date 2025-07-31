import pandas as pd
from extract import extract_data
from transform import transform_data

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    raw_df = extract_data('../raw_data/sales_data_2025.csv')
    transformed_df = transform_data(raw_df)
    load_data(transformed_df, '../clean_data/cleaned_sales_data_2025.csv')
