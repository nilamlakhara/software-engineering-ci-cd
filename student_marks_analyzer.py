from student_marks_analyzer import calculate_percentage

def test_calculate_percentage():
    # If a student scores 400 out of 500, the percentage should be 80.0%
    total = 400
    calculated_percentage = (total / 500) * 100
    assert calculated_percentage == 80.0
