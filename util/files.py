import csv
import os
import re
import csv


def save_csv_to_file(rows: list, filename: str, mode: str = "w") -> None:
    """
    Saves the given rows of data to a CSV file.

    Args:
        rows (list): The list of dictionaries representing the rows of data.
        filename (str): The name of the file to save the data to.
        mode (str, optional): The file mode. Defaults to "w" (write mode).
            Use "a" for append mode.

    Raises:
        ValueError: If an invalid mode is provided.
        FileNotFoundError: If the file cannot be opened or created.
    """

    if mode not in ["w", "a"]:
        raise ValueError("Invalid mode. Use 'w' for write mode or 'a' for append mode.")

    try:
        with open(filename, mode, newline='', encoding='utf-8') as csvfile:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            if mode == "w":
                writer.writeheader()

            # Write each row of data
            for row in rows:
                writer.writerow(row)

    except FileNotFoundError:
        raise FileNotFoundError("File not found or cannot be opened.")


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
