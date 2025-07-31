import pandas as pd
from extract import extract_data

def transform_data(df):
    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create TotalPrice column
    df['TotalPrice'] = df['Quantity'] * df['Price']

    # Optional: Drop rows with missing values
    df.dropna(inplace=True)

    return df

if __name__ == "__main__":
    raw_df = extract_data('../raw_data/sales_data_2025.csv')
    transformed_df = transform_data(raw_df)
    print(transformed_df.head())
