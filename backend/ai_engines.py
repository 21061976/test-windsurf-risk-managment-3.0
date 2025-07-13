# ai_engines.py

import os
import json
import requests
from ai_prompt import PROMPT_TEMPLATE

def analyze_with_ai(text, engine):
    prompt = PROMPT_TEMPLATE + "\n\nתוכן המסמך:\n" + text[:6000]
    if engine == 'claude':
        return call_claude(prompt)
    elif engine == 'openai':
        return call_openai(prompt)
    elif engine == 'gemini':
        return call_gemini(prompt)
    elif engine == 'copilot':
        return call_copilot(prompt)
    else:
        raise Exception('Unknown AI engine')

def call_claude(prompt):
    api_key = os.environ.get('CLAUDE_API_KEY')
    if not api_key:
        raise Exception('Missing CLAUDE_API_KEY')
    url = 'https://api.anthropic.com/v1/messages'
    headers = {
        'x-api-key': api_key,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
    }
    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 2048,
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    content = resp.json()['content'][0]['text']
    return json.loads(content)

def call_openai(prompt):
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise Exception('Missing OPENAI_API_KEY')
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2048,
        "temperature": 0.3
    }
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    content = resp.json()['choices'][0]['message']['content']
    return json.loads(content)

def call_gemini(prompt):
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        raise Exception('Missing GOOGLE_API_KEY')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    resp = requests.post(url, json=data)
    resp.raise_for_status()
    content = resp.json()['candidates'][0]['content']['parts'][0]['text']
    return json.loads(content)

def call_copilot(prompt):
    api_key = os.environ.get('AZURE_COPILOT_KEY')
    endpoint = os.environ.get('AZURE_COPILOT_ENDPOINT')
    if not api_key or not endpoint:
        raise Exception('Missing AZURE_COPILOT_KEY or AZURE_COPILOT_ENDPOINT')
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2048,
        "temperature": 0.3
    }
    resp = requests.post(endpoint, headers=headers, json=data)
    resp.raise_for_status()
    content = resp.json()['choices'][0]['message']['content']
    return json.loads(content)
