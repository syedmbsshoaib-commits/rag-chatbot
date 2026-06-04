import anthropic

client = anthropic.Anthropic()

def chat(conversation, user_input, context=""):
    conversation.append({"role": "user", "content": user_input})
    
    if context:
        system = f"You are a helpful assistant. Use the following document to answer questions. Only answer based on this document. If the answer isn't in the document, say so.\n\nDOCUMENT:\n{context}"
    else:
        system = "You are a helpful assistant."
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=conversation
    )
    
    reply = response.content[0].text
    conversation.append({"role": "assistant", "content": reply})
    return reply