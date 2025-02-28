import pytest


@pytest.fixture
def e2e_data(request):
    return request.param