#!/usr/bin/env python3

"""
Simple helper function that takes two integer arguments page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Parameters
        page: The page number
        page_size: The number of items per page

    Return
        A tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters
    """

    return ((page - 1) * page_size, page * page_size)
