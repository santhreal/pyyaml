import pytest
import yaml


def test_dump():
    assert yaml.dump(['foo'])


def test_load_no_loader():
    with pytest.raises(TypeError):
        yaml.load("- foo\n")


def test_load_safeloader():
    assert yaml.load("- foo\n", Loader=yaml.SafeLoader)


def test_empty_int_float_scalar():
    for s in ('!!int', '!!int ""', '!!int +', 'a: !!int', '!!float', '!!float ""', 'a: !!float'):
        with pytest.raises(yaml.constructor.ConstructorError):
            yaml.safe_load(s)
    assert yaml.safe_load('!!int 1') == 1
    assert yaml.safe_load('!!float 1.5') == 1.5
