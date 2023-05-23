from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name ():
    assert make_full_name ("Jose", "Quemba") == "Quemba; Jose"
    assert make_full_name ("Domanique", "Kemp") == "Kemp; Domanique"
    assert make_full_name ("Jose Eliud", "Quemba") == "Quemba; Jose Eliud"
    assert make_full_name ("Domanique Alyshia", "Kemp") == "Kemp; Domanique Alyshia"

def test_extract_family_name ():
    assert extract_family_name ("Quemba; Jose") == "Quemba"
    assert extract_family_name ("Domanique; Kemp") == "Domanique"
    assert extract_family_name ("Jose Eliud; Quemba") == "Jose Eliud"
    assert extract_family_name ("Domanique Alyshia; Kemp") == "Domanique Alyshia"

def test_extract_given_name ():
    assert extract_given_name ("Quemba; Jose") == "Jose"
    assert extract_given_name ("Domanique; Kemp") == "Kemp"
    assert extract_given_name ("Jose Eliud; Quemba") == "Quemba"
    assert extract_given_name ("Domanique Alyshia; Kemp") == "Kemp"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

