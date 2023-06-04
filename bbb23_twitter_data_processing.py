"""
BBB23 Twitter Data Processing

author: Anderson Sprenger, Gabriel Souza, Vinicius Dias
email: anderson.sprenger@edu.pucrs.br
date: June 04, 2023

This script is used to process the twitter data of the BBB23 Final extracted by tweet utils.

It will:
    - Separate the tweets by participant
    - Plot graphics of the tweets
"""

import json

data = {}
with open('data.json', 'r') as f:
    data = json.load(f)

participants = {}
participants['Amanda'] = []
participants['Aline'] = []
participants['Bruna'] = []

count = 0

for tweet in data:
    if 'amanda' in tweet['text'].lower():
        participants['Amanda'].append(tweet)

    if 'aline' in tweet['text'].lower():
        participants['Aline'].append(tweet)

    if 'bruna' in tweet['text'].lower():
        participants['Bruna'].append(tweet)

    count += 1
    print(f'Processing tweet {count} of {len(data)}')

print('Saving files...')

for key, value in participants.items():
    with open(f'participantes/{key}.json', 'w') as f:
        json.dump(value, f, ensure_ascii=False, indent=4, sort_keys=True)

print('Done!')