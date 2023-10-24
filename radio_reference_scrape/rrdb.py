from radio_reference_scrape.scrape import get_soup, get_state_entities
from settings import base_url
from typing import Dict, List, Any


def get_db_freq(path: str) -> List[Dict[str, str]]:
    """
    Fetches the URL content for each state and returns a list of dictionaries containing the frequency data.

    Args:
        path (str): The path to fetch the sublinks from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the frequency data.
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


def state_entity_list(state_path: str) -> dict[str, list[dict[str, Any]] | list[str]]:
    """
    Fetches state entities from a given path, retrieves their data, and returns a dictionary containing the state entity data and column names.

    Args:
        state_path (str): The path to the state directory.

    Returns:
        dict[str, Any]: A dictionary containing the state entity data and column names.
    """

    state_entities = []
    column_names = []
    entities = get_state_entities(state_path.get('href'))
    if len(entities) > 0:
        for entity in entities:
            rows = get_db_freq(entity.get('href'))
            for row in rows:
                entity_row = {
                    'entity': entity.get('entity'),
                    'entity_type': entity.get('type'),
                }
                merge_object = {**entity_row, **row}
                state_entities.append(merge_object)
                column_names.extend(merge_object.keys())
    column_names = list(set(column_names))

    return {'state_entities': state_entities, 'column_names': column_names}
