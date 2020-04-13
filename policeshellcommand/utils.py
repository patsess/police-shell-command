
import requests
import pandas as pd

__author__ = 'psessford'


LAT_LONG_DICT = {
    'ickenham': (51.5640, -0.4423),
}


def get_street_crimes_from_keyword(location):
    """Get data on street crimes from a location key word

    :param location (str): e.g. 'ickenham'
    :return crimes_df (pd.DataFrame): data on crimes
    """
    if location not in LAT_LONG_DICT:
        raise ValueError(f"location {location} not supported")

    lat, long = LAT_LONG_DICT[location]
    crimes_df = get_street_crimes_from_lat_long(lat=lat, long=long)
    return crimes_df


def get_street_crimes_from_lat_long(lat, long):
    """Get data on street crimes from a latitude and longitude

    :param lat: (str or float) e.g. 51.56640
    :param long: (str or float) e.g. -0.4423
    :return crimes_df (pd.DataFrame): data on crimes
    """
    url = (
        f"https://data.police.uk/api/crimes-street/all-crime?"
        f"lat={lat}&lng={long}")  # &date=2019-02
    response = requests.get(url=url)
    if not response:
        return None

    crimes_df = pd.DataFrame(response.json())
    return crimes_df


def get_n_crimes(crimes_df):
    """Get number of crimes from data

    :param crimes_df: (pd.DataFrame) data on crimes
    :return n_crimes: (int) number of crimes
    """
    n_crimes = crimes_df.shape[0]
    return n_crimes


def show_info(location, crimes_df, is_minimal=False):
    """Show information from crime data

    :param location (str): e.g. 'ickenham'
    :param crimes_df (pd.DataFrame): data on crimes
    :param is_minimal: (bool) whether the infromation shown is minimal
    """
    assert isinstance(is_minimal, bool)
    n_crimes = get_n_crimes(crimes_df=crimes_df)
    print(f"number of crimes at {location}: {n_crimes}")
    if is_minimal:
        return None

    print(crimes_df.groupby('month')[['category']].agg(['count']))
