#!/usr/bin/env python3
"""
Bank Greeting Analyzer

A simple program that analyzes greetings and determines the appropriate tip amount
based on politeness level. The program follows these rules:
- If the greeting starts with "hello" (case-insensitive): $0
- If the greeting starts with "h" (case-insensitive): $20  
- Otherwise: $100

Usage:
    python bank.py
"""

from typing import str


def analyze_greeting(greeting: str) -> int:
    """
    Analyze a greeting and return the appropriate tip amount.
    
    Args:
        greeting: The greeting string to analyze
        
    Returns:
        int: Tip amount in dollars (0, 20, or 100)
    """
    # Normalize the greeting: convert to lowercase and remove spaces
    normalized = greeting.lower().replace(" ", "")
    
    # Check if greeting starts with "hello"
    if normalized.startswith("hello"):
        return 0
    
    # Check if greeting starts with "h"
    elif normalized.startswith("h"):
        return 20
    
    # All other cases
    else:
        return 100


def main() -> None:
    """Main function to run the bank greeting analyzer."""
    try:
        greeting = input("Greeting: ").strip()
        
        if not greeting:
            print("$100")  # Empty greeting gets $100
            return
            
        tip_amount = analyze_greeting(greeting)
        print(f"${tip_amount}")
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
