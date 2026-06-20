# tip-calculator

A small Python utility that calculates the tip and total for a restaurant bill.

## Usage

```bash
python tip_calculator.py <bill_amount> <tip_percent>
```

**Example:**

```bash
python tip_calculator.py 45.00 18
```

Output:
```
Bill:  $45.00
Tip:   $8.10
Total: $53.10
```

## Running the tests

```bash
python -m pytest test_tip_calculator.py
```

## Requirments

- Python 3.8+
