import datetime
import mimesis
import random

from database import init_db, db_session
from database.models import Client, ProductArea, FeatureRequest

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


def create_and_save_fake_feature_requests() -> None:

    if FeatureRequest.query.count() > 0:
        return

    new_feature_requests: List[FeatureRequest] = []
    client_ids: List[int] = [c.id for c in Client.query.all()]
    product_area_ids: List[int] = [pa.id for pa in ProductArea.query.all()]

    development_provider = mimesis.Development()
    datetime_provider = mimesis.Datetime()
    for counter in range(1, 5):
        for client_id in client_ids:
            new_feature_requests.append(FeatureRequest(
                title=f"{development_provider.database()} {random.choice(('problem', 'optimization', 'feature'))}",
                description=development_provider.software_license(),
                client_id=client_id,
                client_priority=counter,
                target_date=datetime.datetime.strptime(datetime_provider.date(2019, 2021), "%m/%d/%Y").date(),
                product_area_id=random.choice(product_area_ids)
            ))

    db_session.bulk_save_objects(new_feature_requests)
    db_session.commit()


init_db()
print("DB Init Finished")

print("Creating Unique Mock Data")
create_and_save_with_names(Client, client_names)
create_and_save_with_names(ProductArea, product_area_names)
create_and_save_fake_feature_requests()
print("Finished Creating Unique Mock Data")
