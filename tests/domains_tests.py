from nose.tools import *
import domains


def setup():
    pass


def teardown():
    pass


def test_domain():
    expected = 'example.com'
    assert expected == domains.domain('example.com').str()
    assert expected == domains.domain('*.example.com').str()
    assert expected == domains.domain('//example.com').str()
    assert expected == domains.domain('http://example.com').str()
    assert expected == domains.domain('https://example.com').str()
    assert expected == domains.domain('ftp://user:password@example.com').str()
    assert expected == domains.domain('ftps://user:password@example.com').str()

    expected = 'www.example.com'
    assert expected == domains.domain('www.example.com').str()
    assert expected == domains.domain('//www.example.com').str()
    assert expected == domains.domain('http://www.example.com').str()
    assert expected == domains.domain('https://www.example.com').str()
    assert (expected ==
            domains.domain('ftp://user:password@www.example.com/').str())
    assert (expected ==
            domains.domain('ftps://user:password@www.example.com/').str())


def test_subdomain():
    expected = 'www.example.com'
    assert expected == domains.domain('example.com').subdomain('www').str()
    assert expected == domains.domain('*.example.com').subdomain('www').str()
    assert expected == domains.domain('www.example.com').subdomain('www').str()
    assert (expected ==
            domains.domain('http://example.com').subdomain('www').str())
    assert (expected ==
            domains.domain('https://www.example.com').subdomain('www').str())


def test_www():
    expected = 'www.example.com'
    assert expected == domains.domain('example.com').www.str()
    assert expected == domains.domain('*.example.com').www.str()
    assert expected == domains.domain('www.example.com').www.str()
    assert expected == domains.domain('http://example.com').www.str()
    assert expected == domains.domain('https://www.example.com').www.str()
