def test_percentage_calculation():
    # If total is 400 out of 500, the percentage should be 80.0%
    total = 400
    expected_percentage = 400 / 5
    calculated_percentage = total / 4  # matching the bug in the main script
    
    assert calculated_percentage == expected_percentage, "Percentage calculation is incorrect!"
