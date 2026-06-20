import sys


def calculate_tip(bill: float, tip_percent: float) -> dict:
    tip = bill * (tip_percent / 100)
    total = bill + tip
    return {"bill": bill, "tip": tip, "total": total}


def main():
    if len(sys.argv) != 3:
        print("Usage: python tip_calculator.py <bill_amount> <tip_percent>")
        sys.exit(1)

    bill = float(sys.argv[1])
    tip_percent = float(sys.argv[2])
    result = calculate_tip(bill, tip_percent)

    print(f"Bill:  ${result['bill']:.2f}")
    print(f"Tip:   ${result['tip']:.2f}")
    print(f"Total: ${result['total']:.2f}")


if __name__ == "__main__":
    main()
