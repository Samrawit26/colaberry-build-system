import sys
sys.path.insert(0, "src")

from colaberry_build_system import greet


def test_greet():
    assert greet("Tester") == "Hello, Tester from colaberry-build-system"
