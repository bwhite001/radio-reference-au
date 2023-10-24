"""
This script fetches state URLs from the RadioReference website and creates directories based on the state names.
"""

import os
import re
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from radio_reference_scrape.rrdb import get_db_freq
from radio_reference_scrape.scrape import get_sublinks_from_path
from util.files import create_directory, save_csv_to_file


def main() -> None:
    """
    Main function to fetch state URLs and print them.
    """
    country_id = "16"
    path = f"/db/browse/coid/{country_id}"
    paths = get_sublinks_from_path(path)
    root = create_directory(os.getcwd(), "csv")
    for path in paths:
        state_path = create_directory(root, path.get("text"))
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


if __name__ == '__main__':
    main()
