"""Utility functions for backend."""
from english_words import get_english_words_set


def get_english_words() -> list:
    """Get all English words."""
    english_words = list(get_english_words_set(sources=["web2"]))
    assert len(set(english_words)) == len(english_words), "English words are unique."
    return english_words
