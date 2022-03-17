import unittest
from survey import AnonymousSurvey
# survey is the module/file name AnonymousSurvey is the class


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """Create a survey and a set of responses to use in all test methods."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Spanish']

    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored correctly."""
        question = 'What language did you first learn to speak? '
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Mandarin', 'Spanish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

    if __name__ == '__main__':
        unittest.main()