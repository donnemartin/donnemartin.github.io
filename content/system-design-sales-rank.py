# -*- coding: utf-8 -*-

from mrjob.job import MRJob


class SalesRanker(MRJob):

    def __init__(self):
        pass

    def within_past_week(self, timestamp):
        """Return True if timestamp is within past week, False otherwise."""
        ...

    def mapper(self, _, line):
        """Parse each log line, extract and transform relevant lines.

        Emit key value pairs of the form:

        (foo, p1), 2
        (bar, p1), 2
        (bar, p1), 1
        (foo, p2), 3
        (bar, p3), 10
        (foo, p4), 1
        """
        timestamp, product_id, category, quantity = line.split('\t')
        if self.within_past_week(timestamp):
            yield (category, product_id), quantity

    def reducer(self, key, values):
        """Sum values for each key.

        (foo, p1), 2
        (bar, p1), 3
        (foo, p2), 3
        (bar, p3), 10
        (foo, p4), 1
        """
        yield key, sum(values)
