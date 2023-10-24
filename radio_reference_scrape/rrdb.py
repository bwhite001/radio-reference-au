from radio_reference_scrape.scrape import get_soup
from settings import base_url


def get_db_freq(path: str):
    """
    Fetches the url content for each state and appends it to a single file.

    Args:
        path (str): The path to fetch the sublinks from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the 'href' and 'state' for each state.
    """
    url = base_url + path
    soup = get_soup(url)
    rows = []

    for item in soup.find_all('h4'):
        row_object = {
            'category': item.text.strip(),
        }

        parent = item.parent
        row_object['group'] = parent.find('h5').text.strip()

        headers = []

        next_table = parent.find('h5').find_next('table', class_='rrdbTable')
        if next_table is None:
            continue
        if next_table and next_table.name == 'table':
            table = next_table

            # Get headers
            for header in table.select('thead th'):
                headers.append(header.text.strip().lower())

            # Get rows
            for row in table.select('tbody tr'):
                row_data = {**row_object}  # Create a new dictionary for each row

                # Get cells in each row
                for index, cell in enumerate(row.select('td')):
                    row_data[headers[index]] = cell.text.strip()

                rows.append(row_data)

    return rows
