import piippy.identity as identity


def test_ip_segments():
    assert len(identity.get_ip().split('.')) == 4


def test_ip_range():
    for segment in identity.get_ip().split('.'):
        assert 0 <= int(segment) <= 255
    assert int(segment[0]) != 0


def test_mac_segments():
    assert len(identity.get_mac().split(':')) == 6


def test_mac_range():
    for segment in identity.get_mac().split(':'):
        assert 0 <= int(segment, 16) <= 255
