import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String

# Load CSV
df = pd.read_csv("Assignment Data Base.csv", encoding="latin-1")
df = df[['Sentence']].drop_duplicates().rename(columns={'Sentence': 'disease_type'})
df['disease_type'] = df['disease_type'].str.strip()

# Setup SQLite
engine = create_engine("sqlite:///diseases.db")
metadata = MetaData()

# Create table
Diseases = Table(
    'Diseases', metadata,
    Column("disease_type", String(256), nullable=False, unique=True)
)
metadata.create_all(engine)

# Insert into table
with engine.connect() as conn:
    for row in df.itertuples(index=False):
        try:
            conn.execute(Diseases.insert().values(disease_type=row.disease_type))
        except Exception:
            continue
