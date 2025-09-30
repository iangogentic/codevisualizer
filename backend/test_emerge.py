import sys
sys.path.insert(0, 'C:/Users/ianig/Desktop/CodeVisualizer/backend')
sys.path.insert(0, 'C:/Users/ianig/Desktop/CodeVisualizer/emerge')

from analysis.emerge_wrapper import EmergeAnalyzer

analyzer = EmergeAnalyzer()
print("Testing emerge analysis...")
try:
    results = analyzer.run_analysis('C:/Users/ianig/Desktop/flask/src', 'py')
    print(f"SUCCESS! Found {results['statistics']['scanned_files']} files")
    print(f"Total LOC: {results['overall_metrics']['total-sloc-in-files']}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

