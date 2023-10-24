"""
This script fetches state URLs from the RadioReference website and creates directories based on the state names.
"""

import settings
from radio_reference_scrape.rrdb import get_db_freq, state_entity_list
from radio_reference_scrape.scrape import get_sublinks_from_path
from util.files import create_directory, modify_string, save_csv_to_file

import os


def make_csv_state_entity(state_path: str, path: dict) -> None:
    """
    Fetches state entities from a given path, retrieves their data, and saves it to a CSV file.

    Args:
        state_path (str): The path to the state directory.
        path (dict): The dictionary representing the path.
    """

    entity_list = state_entity_list(path)
    entities = entity_list.get('state_entities')
    column_names = entity_list.get('column_names')
    if len(entities) > 0:
        filename = os.path.join(state_path, modify_string(path.get('text')) + '_statewide.csv')
        save_csv_to_file(entities, filename, column_names)
        print(f"Wrote {len(entities)} lines to {filename}")


def make_csv_regions(state_path: str, path: dict) -> None:
    """
    Fetches sublinks from a given path and saves the data to CSV files.

    Args:
        state_path (str): The path to the state directory.
        path (dict): The dictionary representing the path.
    """

    regions = get_sublinks_from_path(path.get("href"))
    if len(regions) > 0:
        for region in regions:
            region_path = create_directory(state_path, region.get("text"))
            if region is not None:
                rows = get_db_freq(region.get('href'))
                if len(rows) > 0:
                    filename = f"{region_path}.csv"
                    save_csv_to_file(rows, filename)
                    print(f"Wrote {len(rows)} lines to {filename}")


def main() -> None:
    """
    Main function to fetch state URLs and save them as CSV files.
    """

    country_id = settings.country_id
    path = f"/db/browse/coid/{country_id}"
    paths = get_sublinks_from_path(path)
    root = create_directory(os.getcwd(), "csv")
    for path in paths:
        state_path = create_directory(root, path.get("text"))
        # make_csv_regions(state_path, path)
        make_csv_state_entity(state_path, path)


if __name__ == '__main__':
    main()
