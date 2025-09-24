import pandas as pd
from typing import Tuple

def load_data(filepath: str) -> Tuple[pd.Series, pd.Series]: # # ts module contains functions for loading and preprocessing data.
    try:
        # use 'latin-1' encoding cuz is common for this particular public dataset.
        df = pd.read_csv(filepath, encoding='latin-1')
        
        # MAKING sure the required 2 columns existed..
        if 'label' not in df.columns or 'message' not in df.columns:
            raise ValueError("CSV file must contain 'label' and 'message' columns.")

        # CAUTIOUS LINE FOR ERROR PREVENTION: replace any potential missing values (NaN) in 'message' with an empty string.
        df['message'] = df['message'].fillna('')
        
        return df['message'], df['label']
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path '{filepath}' was not found.")
    except Exception as e:
        # catch other potential pandas errors (e.g., empty file)
        raise RuntimeError(f"An error occurred while reading the CSV file: {e}")