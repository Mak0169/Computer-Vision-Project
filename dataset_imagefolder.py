from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
import os
import shutil
from tqdm import tqdm

load_dotenv()
csv_file = Path(os.getenv("CSV_FILE"))
src_root = Path(os.getenv("DATA_ROOT"))
dst_root = Path(os.getenv("DIR"))

df = pd.read_csv(csv_file)
print(df.head())