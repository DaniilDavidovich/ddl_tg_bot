
from typing import Optional
from enum import Enum

from config import DATA_PATH
import json
import random


class SecretType(Enum):
    free = "free_keys"
    paid = "paid_keys"

def secret_did_handle(type: SecretType) -> Optional[str]:

    json_data = None

    with open(DATA_PATH, encoding="utf-8") as file:
        json_data = json.load(file)

    if json_data is not None:
       value = json_data.get(type.value)

       if isinstance(value, list):
         return random.choice(value)