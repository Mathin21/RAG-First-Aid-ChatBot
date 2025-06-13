from sqlalchemy import create_engine, text
from llama_index.core import SQLDatabase, VectorStoreIndex
from llama_index.core.schema import TextNode
from sqlalchemy.orm import sessionmaker

def setup_db_index(db_path="diseases.db"):
    engine = create_engine(f"sqlite:///{db_path}")
    sql_db = SQLDatabase(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.execute(text("SELECT disease_type FROM Diseases")).fetchall()
    nodes = [TextNode(text=row[0]) for row in rows]

    index = VectorStoreIndex(nodes)
    return index
