from models import storage
from models.state import State

data = storage.all()
print(data)

new_object = {}
new_list =[]

# for d in data:
#     key = "[{}] ".format(str(d.__class__.__name__))
#     new_object[key] = vars(d)
# print(new_object)