"""Tests for obsidian_rag_tool.utils module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from obsidian_rag_tool.utils import get_greeting


def test_get_greeting() -> None:
    """Test that get_greeting returns 'Hello World'."""
    result = get_greeting()
    assert result == "Hello World"
    assert isinstance(result, str)
