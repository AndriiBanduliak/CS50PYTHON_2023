#!/usr/bin/env python3
"""
Bitcoin Price Calculator

A simple script to calculate the current value of Bitcoin in USD.
Takes the number of Bitcoins as a command-line argument and displays
the current USD value based on the CoinDesk API.

Usage:
    python bitcoin.py <number_of_bitcoins>

Example:
    python bitcoin.py 1.5
"""

import sys
import requests
import json
from typing import Optional


def get_bitcoin_amount() -> str:
    """
    Get the number of Bitcoins from command-line arguments.
    
    Returns:
        str: The number of Bitcoins as a string
        
    Raises:
        SystemExit: If arguments are missing or invalid
    """
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    
    try:
        amount = float(sys.argv[1])
        if amount < 0:
            print("Bitcoin amount cannot be negative")
            sys.exit(1)
        return str(amount)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


def get_bitcoin_price() -> float:
    """
    Fetch the current Bitcoin price from CoinDesk API.
    
    Returns:
        float: Current Bitcoin price in USD
        
    Raises:
        SystemExit: If API request fails
    """
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate_float"])
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error parsing Bitcoin price data: {e}")
        sys.exit(1)


def calculate_value(bitcoin_amount: str, price_per_bitcoin: float) -> float:
    """
    Calculate the total value of Bitcoins in USD.
    
    Args:
        bitcoin_amount: Number of Bitcoins as string
        price_per_bitcoin: Price per Bitcoin in USD
        
    Returns:
        float: Total value in USD
    """
    return float(bitcoin_amount) * price_per_bitcoin


def main() -> None:
    """Main function to run the Bitcoin price calculator."""
    bitcoin_amount = get_bitcoin_amount()
    price_per_bitcoin = get_bitcoin_price()
    total_value = calculate_value(bitcoin_amount, price_per_bitcoin)
    
    print(f"Amount: {bitcoin_amount} BTC")
    print(f"Current Price: ${price_per_bitcoin:,.2f}")
    print(f"Total Value: ${total_value:,.4f}")


if __name__ == "__main__":
    main()
