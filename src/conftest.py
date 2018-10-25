"""Global fixtures for tests."""

import pytest

from accounts.factories import UserFactory
from backers.factories import BackerFactory
from geofr.factories import PerimeterFactory


@pytest.fixture
def user():
    """Generates a valid and active user."""

    user = UserFactory()
    return user


@pytest.fixture
def backer():
    """Generates a valid Backer."""

    backer = BackerFactory()
    return backer


@pytest.fixture
def perimeter():
    """Generates a valid Perimetes."""

    perimeter = PerimeterFactory()
    return perimeter