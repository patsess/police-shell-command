
import click
from policeshellcommand.utils import (get_street_crimes_from_keyword,
    get_street_crimes_from_lat_long, get_n_crimes, show_info)

__author__ = 'psessford'

"""
tutorial:
https://realpython.com/
comparing-python-command-line-parsing-libraries-argparse-docopt-click/
"""


@click.group()
def main():
    """Main entrypoint for click app
    """
    pass


@main.command()
@click.argument('location')
@click.option('--minimal', '-m', is_flag=True,
              help="(bool) whether the infromation shown is minimal")
def location(location, minimal):
    """Entrypoint to click app if location key word is provided

    :param location: (str) e.g. 'ickenham'
    """
    crimes_df = get_street_crimes_from_keyword(location=location)
    show_info(location=location, crimes_df=crimes_df, is_minimal=minimal)


@main.command()
@click.argument('coords')
@click.option('--minimal', '-m', is_flag=True,
              help='(bool) whether the infromation shown is minimal')
def coords(coords, minimal):
    """Entrypoint to click app if lat-long coordinates are provided

    :param coords: (str) e.g. '51.5640,-0.4423'
    """
    split_coords = coords.split(',')
    lat, long = split_coords[0], split_coords[1]
    crimes_df = get_street_crimes_from_lat_long(lat=lat, long=long)
    location = f"({lat}, {long})"
    show_info(location=location, crimes_df=crimes_df, is_minimal=minimal)


if __name__ == '__main__':
    main()
