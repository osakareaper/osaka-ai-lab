# import pandas lib
import pandas as pd

# dataset file path
melbourne_file_path = '../../../../datasets/kaggle_datasets/melbourne_housing_dataset.csv'

# read dataset csv and set melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# describe dataset
melbourne_data.describe()