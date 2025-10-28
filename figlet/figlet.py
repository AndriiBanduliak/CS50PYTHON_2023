#!/usr/bin/env python3
"""
ASCII Art Generator using Figlet

A command-line tool that converts text to ASCII art using various fonts.
Supports both default and custom font selection.

Usage:
    python figlet.py                    # Use default font
    python figlet.py -f <font>          # Use specified font
    python figlet.py --font <font>      # Use specified font

Example:
    python figlet.py -f slant "Hello World"
"""

import pyfiglet
import sys
from typing import Optional


def validate_font(font_name: str) -> bool:
    """
    Validate if the specified font is available.
    
    Args:
        font_name: Name of the font to validate
        
    Returns:
        bool: True if font is valid, False otherwise
    """
    try:
        pyfiglet.figlet_format("test", font=font_name)
        return True
    except pyfiglet.FontNotFound:
        return False


def get_available_fonts() -> list:
    """
    Get a list of available fonts.
    
    Returns:
        list: List of available font names
    """
    return pyfiglet.FigletFont.getFonts()


def format_text(text: str, font: Optional[str] = None) -> str:
    """
    Convert text to ASCII art using the specified font.
    
    Args:
        text: Text to convert to ASCII art
        font: Font name (optional, uses default if None)
        
    Returns:
        str: ASCII art representation of the text
        
    Raises:
        pyfiglet.FontNotFound: If the specified font is not found
    """
    if font:
        return pyfiglet.figlet_format(text, font=font)
    else:
        return pyfiglet.figlet_format(text)


def print_usage() -> None:
    """Print usage information."""
    print("Usage:")
    print("  python figlet.py                    # Use default font")
    print("  python figlet.py -f <font>          # Use specified font")
    print("  python figlet.py --font <font>      # Use specified font")
    print("\nAvailable fonts:")
    fonts = get_available_fonts()
    for i, font in enumerate(fonts[:10]):  # Show first 10 fonts
        print(f"  {font}")
    if len(fonts) > 10:
        print(f"  ... and {len(fonts) - 10} more fonts")


def main() -> None:
    """Main function to run the ASCII art generator."""
    if len(sys.argv) == 1:
        # Default font
        text = input("Input: ")
        try:
            result = format_text(text)
            print(f"Output:\n{result}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
            
    elif len(sys.argv) == 3:
        # Custom font
        flag, font = sys.argv[1:]
        
        if flag not in ["-f", "--font"]:
            print("Invalid usage")
            print_usage()
            sys.exit(1)
            
        if not validate_font(font):
            print(f"Font '{font}' not found")
            print_usage()
            sys.exit(1)
            
        text = input("Input: ")
        try:
            result = format_text(text, font)
            print(f"Output:\n{result}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("Invalid usage")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
