from tip_calculator import calculate_tip


def test_standard_tip():
    result = calculate_tip(100.00, 20)
    assert result["tip"] == 20.00
    assert result["total"] == 120.00


def test_zero_tip():
    result = calculate_tip(50.00, 0)
    assert result["tip"] == 0.00
    assert result["total"] == 50.00


def test_rounding():
    result = calculate_tip(45.00, 18)
    assert round(result["tip"], 2) == 8.10
    assert round(result["total"], 2) == 53.10
