from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'mean' in results
    assert isinstance(results['mean'], (int, float))
    assert results['mean'] > 0  # Adjust this condition based on your data
