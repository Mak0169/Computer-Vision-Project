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

for _, row in df.iterrows():
    img_path = src_root / row['filepath']
    label = row['label']
    dst_dir = dst_root / label
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst_path = dst_dir / img_path.name
    shutil.copy(img_path, dst_path)