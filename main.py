import csv
from recombee_api_client.api_client import RecombeeClient, Region, Batch
from recombee_api_client.api_requests import SetItemValues, AddItemProperty
 
# Initialize Recombee client
recombee_client = RecombeeClient(
    'srlab-dev',
    'oFeJzszty6c0gAm5xARLtOd73gvKC7tDm7xrldzk8NVXqK1ZHAMN3nIFHcYCQJJe',
    region=Region.EU_WEST
)
 
def add_item_properties(client):
    try:
        properties = [
            AddItemProperty('age', 'int'),
            AddItemProperty('alcoholism', 'boolean'),
            AddItemProperty('appointmentDay', 'string'),
            AddItemProperty('diabetes', 'boolean'),
            AddItemProperty('gender', 'string'),
            AddItemProperty('handicap', 'boolean'),
            AddItemProperty('hipertension', 'boolean'),
            AddItemProperty('neighbourhood', 'string'),
            AddItemProperty('patientId', 'string'),
            AddItemProperty('scholarship', 'boolean'),
            AddItemProperty('showed_up', 'boolean'),
        ]
        client.send(Batch(properties))
        print("Item properties added successfully.")
    except Exception as err:
        print(f"Error setting item properties: {err}")
 
def upload_appointments(recombee_client, csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        requests = []
        for record in reader:
            requests.append(SetItemValues(
                    record['appointmentId'],
                    {
                        'age': int(record['age']),
                        'alcoholism': record['alcoholism'].lower() == 'true',
                        'appointmentDay': record['appointmentDay'],
                        'diabetes': record['diabetes'].lower() == 'true',
                        'gender': record['gender'],
                        'handicap': record['handicap'].lower() == 'true',
                        'hipertension': record['hipertension'].lower() == 'true',
                        'neighbourhood': record['neighbourhood'],
                        'patientId': record['patientId'],
                        'scholarship': record['scholarship'].lower() == 'true',
                        'showed_up': record['showed_up'].lower() == 'true',
                    },
                    cascade_create=True
                )
            )
             
        try:
            recombee_client.send(Batch(requests))
            print(f"Uploaded {len(requests)} items")
        except Exception as err:
            print(f"Error uploading items {len(requests)}: {err}")
            
 
if __name__ == "__main__":
    add_item_properties(recombee_client)
    upload_appointments(recombee_client, 'healthcare_noshows.csv')