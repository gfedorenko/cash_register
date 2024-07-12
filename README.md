# Cash Register CLI Application

## Overview

This CLI application functions as a simple cash register. It allows you to input a list of item codes and calculates the total price based on a predefined list of products and available offers. 

## Features

- Loads a list of all products with prices.
- Loads a list of available offers.
- Supports three types of offers:
  1. Buy N get one free.
  2. After N items of the same type, the price lowers by a specific amount.
  3. After N items of the same type, the price lowers by a percentage.
- Calculates the final sum of the entered item codes.
- Throws exceptions for unknown item codes, unknown offer types, or duplicated items.

## Usage

To run the application, use:
```sh
python3 main.py
```
To run the tests, use:
```sh
python3 specs.py
```

## Example

Given the following inputs:

- Input: `GR1 GR1 SR1 SR1 SR1 CF1 CF1 CF1`

The application will calculate the final sum and display the result.

## Error Handling

The application will throw exceptions in the following cases:
- Unknown item code: if an item code not present in the products list is entered.
- Unknown offer type: if an offer type not supported by the application is encountered.
- Duplicated items: if the same item appears more than once in the initial products list.

---

Happy Shopping!
