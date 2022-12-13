"""Test cases for the console module."""
import pytest
from click.testing import CliRunner

from {{cookiecutter.package_name}} import {{ cookiecutter.package_name }}_cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke({{ cookiecutter.package_name }}_cli.main)
    assert result.exit_code == 0