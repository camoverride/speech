"""
Utilities relating to Text-to-Speech Front-End. The FE is responsible for
producing a phoneme that can be interpreted by the Back-End and converted into
a waveform.

TODO: decide which encoding to use.
"""
import os
import re
from g2p_model import apply_g2p_model


def get_words(phrase: str, rules_path: str="rules/normalization_rules.txt"):
    """
    Converts all non-alphabetic text into words.

    Parameters
    ----------
    phrase: str
        A phrase to convert.

    rules_path: str
        Path to a rules file with special regex rules for normalizations.

    Returns
    -------
    str
        A string with items like `12:01` converted to `twelve oh one`.
    """
    # Load and apply custom rules from the ruleset document.
    rules = get_rules(rules_path)

    for match, replace in rules:
        phrase = re.sub(re.compile(match), replace, phrase)

    return phrase


def get_rules(rules_path: str):
    """
    The rules file defines special exceptions. 
    """
    rules =[]
    with open(rules_path) as f:
        for line in f:
            if "-->" in line:
                pattern, replacement = line.split("-->")
                pattern, replacement = pattern.strip(), replacement.strip()
                pattern, replacement = pattern.strip("||sub||"), replacement.strip("||sub||")
                rules.append((pattern, replacement))

    return rules


def g2p(phrase: str, rules_path: str="rules/g2p_rules.txt"):
    """
    This function converts a normalized phrase into a phoneme sequence.

    Parameters
    ----------
    phrase: str
        The phrase to be converted. Should be in words-only format.

    rules_path: str
        Path to a rules file with special regex rules for prons.

    Returns
    -------
    str
        The phoneme string. TODO: decide which encoding -- SSML?
    """
    # Apply normalizing rules.
    phrase = get_words(phrase)
    
    # Load the special g2p rules.
    rules = get_rules(rules_path)

    for match, replace in rules:
        phrase = re.sub(match, replace, phrase)

    phonemes = apply_g2p_model(phrase)

    return phonemes
