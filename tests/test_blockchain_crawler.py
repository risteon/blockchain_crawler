#!/usr/bin/env python3

import unittest

from context import blockchain_crawler
from blockchain_crawler.playground import get_latest_block


class TestBlockChainCrawler(unittest.TestCase):

    def test_dummy(self):
        json_data = get_latest_block()
        print(json_data['block_index'])

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
