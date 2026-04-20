from openai import OpenAI
from ai.prompts import GENERATOR_PROMPT
import os, json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_project(plan):
    res = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': GENERATOR_PROMPT},
            {'role': 'user', 'content': json.dumps(plan)}
        ]
    )
    return res.choices[0].message.content