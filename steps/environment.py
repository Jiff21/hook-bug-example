# -*- coding: UTF-8 -*-
# Redifining context: pylint: disable=W0621
# Using context to pass functions: pylint: disable=R0201

'''Test setup done with fixtures here per pytest-bdd docs'''
import pytest
import requests

class Context():
    """An empty object to add stuff to"""

    def __init__(self):
        self.current_url = None

@pytest.fixture
def context(scope="module"): # pylint: disable=W0613
    """A context for passing information between steps"""
    context = Context()
    return context
