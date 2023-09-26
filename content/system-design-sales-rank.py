# -*- coding: utf-8 -*-

from mrjob.job import MRJob


class SalesRanker(MRJob):

    def __init__(self):
        pass

    def within_past_week(self, timestamp):
        """Return True if timestamp is within past week, False otherwise."""
        ...
