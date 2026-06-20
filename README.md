# tip-calculator

A small Python utility that calculates the tip and total for a restaurant bill.

## Installation

1. Make sure you have Python 3.8 or higher installed. Check with:
   ```bash
   python --version
   ```
   If you don't have it, download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
   ```bash
   git clone https://github.com/beepdeha/tip-calculator.git
   cd tip-calculator
   ```

3. No additional dependencies are required — the calculator uses only the Python standard library.

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

## Requirements

- Python 3.8+
