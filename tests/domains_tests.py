from nose.tools import *
import domains


def setup():
    pass


def teardown():
    pass


def test_domain():
    expected = 'example.com'
    assert expected == str(domains.domain('example.com'))
    assert expected == str(domains.domain('*.example.com'))
    assert expected == str(domains.domain('//example.com'))
    assert expected == str(domains.domain('http://example.com'))
    assert expected == str(domains.domain('https://example.com'))
    assert expected == str(domains.domain('ftp://user:password@example.com'))
    assert expected == str(domains.domain('ftps://user:password@example.com'))

    expected = 'www.example.com'
    assert expected == str(domains.domain('www.example.com'))
    assert expected == str(domains.domain('//www.example.com'))
    assert expected == str(domains.domain('http://www.example.com'))
    assert expected == str(domains.domain('https://www.example.com'))
    assert (expected ==
            str(domains.domain('ftp://user:password@www.example.com/')))
    assert (expected ==
            str(domains.domain('ftps://user:password@www.example.com/')))


def test_subdomain():
    expected = 'www.example.com'
    assert expected == str(domains.domain('example.com').subdomain('www'))
    assert expected == str(domains.domain('*.example.com').subdomain('www'))
    assert expected == str(domains.domain('www.example.com').subdomain('www'))
    assert (expected ==
            str(domains.domain('http://example.com').subdomain('www')))
    assert (expected ==
            str(domains.domain('https://www.example.com').subdomain('www')))


def test_www():
    expected = 'www.example.com'
    assert expected == str(domains.domain('example.com').www)
    assert expected == str(domains.domain('*.example.com').www)
    assert expected == str(domains.domain('www.example.com').www)
    assert expected == str(domains.domain('http://example.com').www)
    assert expected == str(domains.domain('https://www.example.com').www)
