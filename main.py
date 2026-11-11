import sys
from explainer import explain

# The CSV file name is given when you run the program
if len(sys.argv) < 2:
    print("Usage: python main.py yourfile.csv")
    sys.exit()

path = sys.argv[1]

# Try to read the file and explain it
try:
    print("Reading", path, "...")
    print()
    print(explain(path))
except FileNotFoundError:
    print("File not found:", path)