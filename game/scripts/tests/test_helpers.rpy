init python:
    def test_expect(condition, message):
        if not condition:
            raise AssertionError(message)

    def test_expect_equal(actual, expected, message):
        if actual != expected:
            raise AssertionError(f"{message} (got {actual!r}, expected {expected!r})")
