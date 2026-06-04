from chat import chat
from embeddings import chunk_text, find_relevant_chunks

def load_document(filepath):
    with open(filepath, "r") as f:
        return f.read()

document = load_document("documents/faq.txt")
chunks = chunk_text(document)

print(f"Document split into {len(chunks)} chunks.\n")

conversation = []

while True:
    user_input = input("You: ")
    relevant_chunks = find_relevant_chunks(user_input, chunks)
    context = "\n\n".join(relevant_chunks)
    reply = chat(conversation, user_input, context=context)
    print(f"Claude: {reply}\n")