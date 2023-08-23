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

    def mapper(self, _, line):
        """Parse each log line, extract and transform relevant lines.

        Emit key value pairs of the form:

        (2016-01, url0), 1
        (2016-01, url0), 1
        (2016-01, url1), 1
        """
        url = self.extract_url(line)
        period = self.extract_year_month(line)
        yield (period, url), 1
