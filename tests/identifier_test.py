from src import Identifier

class TestIdentifier:
    
    def setup_method(self, method):
        """
            setup any state specific to the execution of the given class 
            (which usually contains tests).
        """
        self.instance = Identifier()
        
    def teardown_method(self, method):
        """
            teardown any state that was previously setup with a call to
            setup_class.
        """
        
    def test_should_return_false_when_the_user_inputs_an_empty_string(self):
        assert  self.instance.validate_identifier("") == False

    def test_should_return_true_when_the_user_inputs_an_valid_string(self):
        assert  self.instance.validate_identifier("stdlib") == True

    def test_should_return_false_when_the_user_starts_the_string_with_a_number(self):
        assert  self.instance.validate_identifier("1") == False

    def test_should_return_true_when_the_user_starts_with_capital_letter(self):
        assert  self.instance.validate_identifier("A564") == True

    def test_should_return_true_when_the_user_starts_with_a_letter_and_number(self):
        assert  self.instance.validate_identifier("a7") == True

    def test_should_return_true_when_the_string_has_a_single_letter(self):
        assert  self.instance.validate_identifier("S") == True

    def test_should_return_false_when_the_string_starts_with_special_characters(self):
        assert  self.instance.validate_identifier("/**~'") == False

    def test_should_return_false_when_string_size_is_greater_than_six(self):
        assert self.instance.validate_identifier("abcdefg") == False