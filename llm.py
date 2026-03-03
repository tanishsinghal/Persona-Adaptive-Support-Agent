from openai import OpenAI

client = OpenAI(api_key="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")

def generate_response(persona, kb_response, user_message):
    system_prompt = ""

    if persona == "technical_expert":
        system_prompt = "You are a concise technical support engineer. Give precise and direct responses."
    elif persona == "frustrated_user":
        system_prompt = "You are a calm and empathetic support agent. Acknowledge frustration first, then provide solution."
    elif persona == "business_executive":
        system_prompt = "You are a professional business support agent. Provide high-level and strategic responses."
    else:
        system_prompt = "You are a helpful customer support assistant."

    prompt = f"""
    User message: {user_message}
    Knowledge Base Info: {kb_response}
    
    Generate a response based on the persona tone.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content