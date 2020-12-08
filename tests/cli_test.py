import pytest
import kraitTests.main as main

from click.testing import CliRunner


@pytest.mark.cli
def test_cli():
    runner = CliRunner()

    result = runner.invoke(main.main)

    assert not result.exception
