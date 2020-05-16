"""
Common utilities such as text cleaning, normalization, POS-tagging, and syntactic analysis
that is used by both the front-end and the back-end. Encapsulated in the NLP object.
"""

import re
import string


class NLP:

    def __init__(self, syntax=False):
        self.syntax = syntax


    def _clean_text(self, phrase: str):
        """
        This function takes some raw text and removes unwanted items like HTML tags,
        super long words, encoding errors, non-English characters, etc.

        Parameters
        ----------
        phrase: str
            A raw phrase to clean up.

        Returns
        -------
        str
            A cleaned-up phrase.
        """
        # Remove super long things.
        phrase = phrase.split()
        phrase = [word for word in phrase if len(word) < 30]

        # Remove common HTML tag-alongs...
        tags = ["<p>", "</p>"]
        phrase = [word for word in phrase if word not in tags]

        return " ".join(phrase)


    def _normalize(self, phrase: str):
        """
        Normalizes all text to ASCII.

        Parameters
        ----------
        phrase: str
            An un-normalized phrase.

        Returns
        -------
        str
            A normalized phrase.
        """
        # Remove non-ASCII.
        phrase = phrase.split()
        phrase = [word for word in phrase if word in string.printable]

        return " ".join(phrase)


    def _tag(self, phrase: str):
        """
        Tags the phrase with POS information.

        Parameters
        ----------
        phrase: str
            An un-tagged phrase.

        Returns
        -------
        str
            A phrase tagged in TODO: find tagging format.
        """
        return phrase


    def _get_syntax(self, phrase: str):
        """
        I WILL PROBABLY NEVER MAKE USE OF THIS.
        """
        return phrase


    def clean_text(self, text):
        """
        Driver function that completes the standard NLP pipeline.
        """
        text = self._clean_text(text)
        text = self._normalize(text)

        if self.syntax:
            text = self._tag(text)
            text = self._get_syntax(text)

        return text
