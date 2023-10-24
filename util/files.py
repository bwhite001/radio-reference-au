import os
import re
import csv
from typing import Any


def save_csv_to_file(rows: list[dict[str, Any]], filename: str,
                     fieldnames: list[str] = None) -> None:
    """
    Saves the given rows of data to a CSV file.

    Args:
        rows (list[dict[str, Any]]): The list of dictionaries representing the rows of data.
        filename (str): The name of the file to save the data to.
        fieldnames (list[str], optional): The fieldnames for the CSV file. Defaults to None.

    Raises:
        FileNotFoundError: If the file cannot be opened or created.
    """

    if fieldnames is None:
        fieldnames = list(rows[0].keys())

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            # Write each row of data
            writer.writerows(rows)

    except FileNotFoundError as e:
        raise FileNotFoundError("File not found or cannot be opened.") from e


def modify_string(s: str) -> str:
    """
    Modifies the given string to be safe by removing any other characters with underscores and converting it to lowercase.

    Args:
        s (str): The string to be modified.

    Returns:
        str: The modified string.
    """
    # Remove non-alphanumeric characters except for whitespace
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)

    # Replace whitespace with underscores
    s = re.sub(r'\s', '_', s)

    # Remove consecutive double or triple underscores with a single underscore
    s = re.sub(r'_{2,3}', '_', s)

    # Convert to lowercase
    s = s.lower()

    return s


def create_directory(base_path: str, dir_name: str) -> str:
    """
    Creates a directory based on the given directory name using the provided base path.

    Args:
        base_path (str): The base path where the directory will be created.
        dir_name (str): The name of the directory to be created.

    Returns:
        str: The full path of the created directory.
    """

    # Create the directory if it doesn't exist
    safe_dirname = modify_string(dir_name)
    dir_path = os.path.join(base_path, safe_dirname)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path
