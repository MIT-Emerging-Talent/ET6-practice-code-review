import pandas as pd

def get_unique_values(file_path, column_name):
    """
    Get unique values from a specified column in a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file.
        column_name (str): Name of the column to extract unique values.
    
    Returns:
        list: Unique values in the specified column.
    
    Raises:
        FileNotFoundError: If the file path is invalid.
        KeyError: If the column name doesn't exist in the CSV.
    
    Doctests:
    >>> get_unique_values('data.csv', 'column_name')
    ['value1', 'value2', 'value3']
    
    >>> get_unique_values('data.csv', 'column_name')
    ['apple', 'banana', 'cherry']
    
    >>> get_unique_values('data.csv', 'age')
    [23, 34, 45, 56]
    
    >>> get_unique_values('missing_file.csv', 'column_name')
    Traceback (most recent call last):
        ...
    FileNotFoundError: File not found: missing_file.csv
    
    >>> get_unique_values('data.csv', 'non_existent_column')
    Traceback (most recent call last):
        ...
    KeyError: "Column 'non_existent_column' does not exist in the CSV."
    """
    try:
        df = pd.read_csv(file_path)
        if column_name not in df.columns:
            raise KeyError(f"Column '{column_name}' does not exist in the CSV.")
        return df[column_name].dropna().unique().tolist()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
