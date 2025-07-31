import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = extract_data('../raw_data/sales_data_2025.csv')
    print(df.head())
