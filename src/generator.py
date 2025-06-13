import os
from openai import OpenAI

llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_prompt(query, web_context, local_context):
    return f"""
⚠️ This info is for educational use only.

Query: {query}

--- Web ---
{web_context}

--- Local ---
{local_context}

Respond in the following JSON structure:

{{
  "condition": "Name of likely condition",
  "steps": ["Step 1...", "Step 2...", "Step 3..."],
  "medications": "Any medicine details or say 'None'",
  "follow_up": "Post-action advice or dietary follow-up",
  "source": "Include link to trusted source (if any)"
}}

Avoid extra text. Return valid JSON only.
"""

def generate_response(prompt):
    response = llm.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        )
    return response.choices[0].message.content
