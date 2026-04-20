from openai import OpenAI
from ai.prompts import PLANNER_PROMPT
import os, json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def plan_project(history):
    res = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'system', 'content': PLANNER_PROMPT}, *history]
    )
    content = res.choices[0].message.content.strip()
    if content.endswith('?'):
        return {'type': 'question', 'content': content}
    return {'type': 'plan', 'content': json.loads(content)}