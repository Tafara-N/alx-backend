#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
                }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Takes two integer arguments: index with a None default value and
        page_size with default value of 10

        Parameters
            index: The index to retrieve from the dataset - default=None
            page_size: The size of the page - default=10.

        Return
            A dictionary containing the retrieved data along with the metadata
        """

        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert index is not None and index >= 0 and index < data_length
        response = {}

        data = []

        response["index"] = index

        for i in range(page_size):
            while True:
                current = dataset.get(index)
                index += 1
                if current is not None:
                    break
            data.append(current)

        response["data"] = data
        response["page_size"] = len(data)

        if dataset.get(index):
            response["next_index"] = index
        else:
            response["next_index"] = None
        return response
