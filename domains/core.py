import re
import urlparse


_scheme_re = re.compile('^\w+://')


class Domain(object):
    def __init__(self, url):
        if not _scheme_re.search(url):
            url = 'http://{url}'.format(url=url)

        parts = urlparse.urlparse(url)
        self.netloc = parts.netloc

    def __str__(self):
        return self.netloc

domain = Domain
