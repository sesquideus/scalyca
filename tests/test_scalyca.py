import subprocess
import pytest


@pytest.fixture
def out():
    return subprocess.run(['python', './show_scalyca.py', 'sample.yaml', 'foo', '5', '--debug'], capture_output=True)


class TestScalyca():
    def test_can_be_run_with_showcase(self, out):
        assert out.returncode == 0

    def test_showcase_stderr_is_empty(self, out):
        assert len(out.stderr) == 0