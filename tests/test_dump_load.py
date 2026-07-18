import pytest
import yaml


def test_dump():
    assert yaml.dump(['foo'])


def test_load_no_loader():
    with pytest.raises(TypeError):
        yaml.load("- foo\n")


def test_load_safeloader():
    assert yaml.load("- foo\n", Loader=yaml.SafeLoader)


def test_empty_bool_scalar():
    for s in ('!!bool', '!!bool ""', 'a: !!bool', '!!bool maybe'):
        with pytest.raises(yaml.constructor.ConstructorError):
            yaml.safe_load(s)
    assert yaml.safe_load('!!bool true') is True
    assert yaml.safe_load('!!bool false') is False
