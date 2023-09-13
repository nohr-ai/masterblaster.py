from masterblaster.headers import Header


def test_add_field():
    """
    Test adding field to header
    """

    header = Header()
    header.add("test", "test")
    assert header.fields["test"] == "test"
