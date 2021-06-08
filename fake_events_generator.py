"""
Code used to generate fake event items
"""
import sys
import json
from faker import Faker

N = int(sys.argv[1])
output_file = sys.argv[2]

fake = Faker()

events = ""
for _ in range(N):

    item = {
        "event_id":fake.uuid4(),
        "timestamp":fake.iso8601(),
        "domain":fake.random_element(elements=('account','transaction')),
        "event_type":fake.random_element(elements=('status-change','create','delete','update')),
        "data":{
            "id":fake.random_number(digits=6),
            "old_status":fake.word(),
            "new_status":fake.word(),
            "reason":fake.text(max_nb_chars=80)
        }
    }

    events+=json.dumps(item)+"\n"

with open(output_file,'+w') as file:
    file.write(events)