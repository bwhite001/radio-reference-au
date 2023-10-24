from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from settings import base_url


def get_soup(url: str) -> BeautifulSoup:
    """
    Retrieves the text content from a given URL.

    Args:
        url (str): The URL to fetch the text content from.

    Returns:
        BeautifulSoup: The parsed HTML content.
    """
    response = requests.get(url)

    assert response.status_code == 200, \
        f"Request failed with status code {response.status_code}"
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')


def get_state_entities(path: str) -> List[Dict[str, str]]:
    """
    Fetches the URL content for each state and returns a list of dictionaries containing the 'href', 'text', 'State Entity', and 'Entity Type' for each state.

    Args:
        path (str): The path to fetch the sublinks from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the 'href', 'text', 'State Entity', and 'Entity Type' for each state.
    """

    url = base_url + path
    soup = get_soup(url)
    rows = soup.select('table tbody tr')
    results = []

    for row in rows:
        state_entity = row.find_all('td')[0].text.strip()
        entity_type = row.find_all('td')[1].text.strip()
        a_element = row.find('a')

        if a_element is not None:
            result = {
                'entity': state_entity,
                'type': entity_type,
                'href': a_element['href'],
                'text': a_element.text.strip()
            }
            results.append(result)

    return results


def get_sublinks_from_path(path: str) -> List[Dict[str, str]]:
    """
    Fetches the url content for each state and appends it to a single file.

    Args:
        path (str): The path to fetch the sublinks from.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the 'href' and 'state' for each state.
    """

    url = base_url + path
    soup = get_soup(url)
    tag = soup.find("table", {"class": "locTable"})
    if tag is not None:
        a_tags = tag.find_all('a')
        return [{'href': tag['href'], 'text': tag.text} for tag in a_tags]
    else:
        return []
