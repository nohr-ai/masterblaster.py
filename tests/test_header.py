import pytest
from masterblaster.headers import Header


def test_add_field():
    """
    Test adding field to header
    """

    header = Header()
    header.add("test", "test")
    assert header.fields["test"] == "test"


def test_remove_field():
    """
    Test removing field from header
    """

    header = Header()
    header.add("test", "test")
    header.remove("test")
    assert "test" not in header.fields


def test_remove_field_not_found():
    """
    Test removing field from header when field is not found
    """

    header = Header()
    header.remove("test")
    assert "test" not in header.fields


def test_get_field():
    """
    Test getting field from header
    """

    header = Header()
    header.add("test", "test")
    assert header["test"] == "test"


def test_getattr():
    """
    Test getting field from header
    """

    header = Header()
    header.add("test", "test")
    assert header.test == "test"


def test_setattr():
    """
    Test setting field from header
    """

    header = Header()
    header["test"] = "test"
    assert header.test == "test"


def test_del():
    """
    Test deleting field from header
    """

    header = Header()
    header.add("test", "test")
    del header["test"]
    assert "test" not in header.fields


def test_str():
    """
    Test str representation of header
    """

    header = Header()
    header.add("test", "test")
    assert str(header) == '{"test": "test"}'


def test_repr():
    """
    Test repr representation of header
    """

    header = Header()
    header.add("test", "test")
    assert repr(header) == '{"test": "test"}'
