"""
BBB23 Twitter Data Processing

author: Anderson Sprenger, Gabriel Souza, Vinicius Dias
email: anderson.sprenger@edu.pucrs.br, gabrielzds03@gmail.com, 
date: June 04, 2023

This script is used to process the twitter data of the BBB23 Final extracted by tweet utils.

It will:
    - Separate the tweets by participant
    - Plot graphics of the tweets
"""

import json

data = {}
with open('coleta_bbb_pt_new.json', 'r') as f:
    data = json.load(f)

participants = {}
participants['Amanda'] = []
participants['Aline'] = []
participants['Bruna'] = []

for tweet in data:
    if any('amanda' in person.lower() for person in tweet['people_cited']):
        participants['Amanda'].append(tweet)

    if any('aline' in person.lower() for person in tweet['people_cited']):
        participants['Aline'].append(tweet)

    if any('bruna' in person.lower() for person in tweet['people_cited']):
        participants['Bruna'].append(tweet)

for key, value in participants.items():
    with open(f'participantes/{key}.json', 'w') as f:
        json.dump(value, f, ensure_ascii=False, indent=4, sort_keys=True)