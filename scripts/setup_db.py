import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.seed import seed

if __name__ == "__main__":
    seed()
    print("Database setup and seeded.")