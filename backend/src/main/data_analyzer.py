from pymongo import MongoClient
import pandas as pd

def clean_data(df):
    del_columns = ['contract_type', '_id', 'id', '__CLASS__', 'longitude', 'latitude', 'salary_is_predicted', 'adref']

    df = df.drop(columns=del_columns)

    # Remove rows where 'contract_time' is null
    df.dropna(subset=['contract_time'], inplace=True)

    return df

def calculate_quartiles(df):
    lower_quartile = df['salary_min'].quantile(0.25)
    middle_quartile = df['salary_min'].quantile(0.5)
    upper_quartile = df['salary_min'].quantile(0.75)

    # Define quartile categories and labels
    conditions = [
        (df['salary_min'] <= lower_quartile),
        (df['salary_min'] > lower_quartile) & (df['salary_min'] <= middle_quartile),
        (df['salary_min'] > middle_quartile) & (df['salary_min'] <= upper_quartile),
        (df['salary_min'] > upper_quartile)
    ]
    quartile_labels = ['Lower Quartile', 'Middle Quartile', 'Upper Quartile', 'Above Upper Quartile']

    # Create a new column 'Salary Quartile' to categorize jobs
    df['Salary Quartile'] = pd.cut(df['salary_min'], bins=[-float("inf"), lower_quartile, middle_quartile, upper_quartile, float("inf")], labels=quartile_labels)

    return df

def store_processed_data_to_mongo(df):
    MONGO_URI = 'mongodb://localhost:27017/jobdatabase'
    client = MongoClient(MONGO_URI)
    db = client.get_database()

    job_data = db['processed_job_data']

    records = df.to_dict(orient='records')
    job_data.insert_many(records)

def main():

    MONGO_URI = 'mongodb://localhost:27017/jobdatabase'
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    job_data_collection = db['job_data']

    all_job_data = job_data_collection.find()

    data_list = list(all_job_data)
    df = pd.DataFrame(data_list)

    df = clean_data(df)

    df = calculate_quartiles(df)

    store_processed_data_to_mongo(df)

if __name__ == "__main__":
    main()
