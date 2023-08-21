# -*- coding: utf-8 -*-

from mrjob.job import MRJob


class HitCounts(MRJob):

    def __init__():
        pass

    def extract_url(self, line):
        """Extract the generated url from the log line."""
        pass

    def extract_year_month(self, line):
        """Return the year and month portions of the timestamp."""
        pass
