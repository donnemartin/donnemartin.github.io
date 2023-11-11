# -*- coding: utf-8 -*-


class PagesDataStore(object):

    def __init__(self, db):
        self.db = db
        pass

    def add_link_to_crawl(self, url):
        """Add the given link to `links_to_crawl`."""
        pass

    def remove_link_to_crawl(self, url):
        """Remove the given link from `links_to_crawl`."""
        pass

    def reduce_priority_link_to_crawl(self, url):
        """Reduce the priority of a link in `links_to_crawl` to avoid cycles."""
        pass

    def extract_max_priority_page(self):
        """Return the highest priority link in `links_to_crawl`."""
        pass

    def insert_crawled_link(self, url, signature):
        """Add the given link to `crawled_links`."""
        pass

    def crawled_similar(self, signature):
        """Determine if we've already crawled a page matching the given signature"""
        pass


class Page(object):

    def __init__(self, url, contents, child_urls):
        self.url = url
        self.contents = contents
        self.child_urls = child_urls
        self.signature = self.create_signature()

    def create_signature(self):
        # Create signature based on url and contents
        pass
