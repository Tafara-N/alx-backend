#!/usr/bin/env python3

"""
Simple helper function that takes two integer arguments page and page_size
"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size

    Parameters
        page: The page number
        page_size: The number of items per page

    Return
        A tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters
    """

    return ((page - 1) * page_size, page * page_size)


class Server:
    """
    Server class to paginate a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes two integer arguments page with default value 1 and page_size
        with default value 10

        Parameters
            page: The page number
            page_size: The number of items per page

        Return
            A list of lists of strings, where each list represents a row in the
            dataset
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)

        return self.dataset()[start:end]
