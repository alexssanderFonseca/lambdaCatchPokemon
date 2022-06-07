import os
import random
import uuid
from io import BytesIO

import boto3
import requests


def lambda_handler(event, context):
    pokemon = catch()
    env = os.getenv("env")
    if env == "LOCAL":
        save_to_s3_locally(pokemon)
        return
    save_to_s3_remote(pokemon)


def catch():
    random_number = random.randint(1, 150)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_number}").json()
    name = response["name"]
    sprite_url = response["sprites"]["front_default"]
    return {
        "name": name,
        "sprite": get_sprite(sprite_url)
    }


def get_sprite(sprite_url):
    response = requests.get(sprite_url)
    return BytesIO(response.content)


def save_to_s3(s3, pokemon):
    s3.put_object(
        Key=f"{pokemon['name']}-{uuid.uuid4()}.png",
        Body=pokemon["sprite"],
        Bucket="pokedex"
    )


def save_to_s3_locally(pokemon):
    s3 = boto3.client('s3', endpoint_url="http://host.docker.internal:4566", use_ssl=False)
    save_to_s3(s3, pokemon)


def save_to_s3_remote(pokemon):
    s3 = boto3.client('s3')
    save_to_s3(s3, pokemon)
