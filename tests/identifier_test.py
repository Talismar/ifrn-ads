from src import Identifier

def test_should_return_false_when_the_user_inputs_an_empty_string():
    instance = Identifier()
    assert  instance.validate_identifier("") == False

def test_should_return_true_when_the_user_inputs_an_valid_string():
    instance = Identifier()
    assert  instance.validate_identifier("stdlib") == True

def test_should_return_false_when_the_user_starts_the_string_with_a_number():
    instance = Identifier()
    assert  instance.validate_identifier("1") == False

def test_should_return_true_when_the_user_starts_with_capital_letter():
    instance = Identifier()
    assert  instance.validate_identifier("A564") == True

def test_should_return_true_when_the_user_starts_with_a_letter_and_number():
    instance = Identifier()
    assert  instance.validate_identifier("a7") == True

def test_should_return_true_when_the_string_has_a_single_letter():
    instance = Identifier()
    assert  instance.validate_identifier("S") == True

def test_should_return_false_when_the_string_starts_with_special_characters():
    instance = Identifier()
    assert  instance.validate_identifier("/**~'") == False


def test_should_return_false_when_string_size_is_greater_than_six():
    instance = Identifier()
    assert instance.validate_identifier("abcdefg") == False