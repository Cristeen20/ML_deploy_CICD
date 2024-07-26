from analysis import run_analysis

def test_type_analysis():
    results = run_analysis()
    assert isinstance(results, str)  # Ensure the result is a string
    assert float(results) > 0  # Convert the result to float and check if it's positive

def test_null_analysis():
    results = run_analysis()
    assert results is not None  # Ensure the result is not None
    assert isinstance(results, str)  # Ensure the result is a string
    assert float(results) > 0