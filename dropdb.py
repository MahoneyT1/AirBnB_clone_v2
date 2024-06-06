from models.base_model import BaseModel, Base
from models import storage

db_storage = storage()
engine = db_storage.__engine

Base.metada.drop_all(engine)
print("sucessfully droped all tables")