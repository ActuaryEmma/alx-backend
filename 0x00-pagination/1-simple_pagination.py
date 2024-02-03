#!/usr/bin/env python3
"""
Task 1
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """
        return a tuple of size two containing a start index and an end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        page with default value 1 and page_size with default value 10.
        """
        assert page > 0
        assert type(page) == int
        assert type(page_size) == int
        assert page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
