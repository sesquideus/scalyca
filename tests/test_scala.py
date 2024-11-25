import subprocess
import pytest

from scalyca import Scala


@pytest.fixture
def out():
    return subprocess.run(['python', './show_scala.py', 'foo', '5', './LICENSE', '--debug'], capture_output=True)


class TestScala():
    def test_can_be_run_with_showcase(self, out):
        assert out.returncode == 0

    def test_showcase_stderr_is_empty(self, out):
        assert len(out.stderr) == 0

    def test_scala_is_abstract(self):
        """ Scala should be abstract """
        with pytest.raises(TypeError):
            Scala()
