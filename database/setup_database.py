from database import init_db, db_session
from database.models import Client, ProductArea

from typing import Union, Type, List


client_names = ['Client A', 'Client B', 'Client C']
product_area_names = ['Policies', 'Billing', 'Claims', 'Reports']


def create_and_save_with_names(model: Union[Type[Client], Type[ProductArea]], names: List[str]) -> None:
    new_instances = []
    for name in names:
        if model.query.filter(model.name == name).count() == 0:
            new_instances.append(model(name=name))
    db_session.bulk_save_objects(new_instances)
    db_session.commit()


init_db()
print("DB Init Finished")

print("Creating Mock Data")
create_and_save_with_names(Client, client_names)
create_and_save_with_names(ProductArea, product_area_names)
print("Finished Creating Mock Data")
