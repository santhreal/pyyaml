import pytest
import yaml


def test_dump():
    assert yaml.dump(['foo'])


def test_load_no_loader():
    with pytest.raises(TypeError):
        yaml.load("- foo\n")


def test_load_safeloader():
    assert yaml.load("- foo\n", Loader=yaml.SafeLoader)


def test_empty_timestamp_scalar():
    for s in ('!!timestamp', '!!timestamp ""', 'a: !!timestamp', '!!timestamp not-a-date'):
        with pytest.raises(yaml.constructor.ConstructorError):
            yaml.safe_load(s)
    assert yaml.safe_load('!!timestamp 2020-01-02') == __import__('datetime').date(2020, 1, 2)
