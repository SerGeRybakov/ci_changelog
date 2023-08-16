import pytest

from src.main1 import main

def test_main():
    assert main(1,1) == 2
