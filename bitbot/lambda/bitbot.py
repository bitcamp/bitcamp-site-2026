from groq import Groq
import json
from openai import OpenAI
import numpy as np
from dotenv import load_dotenv

load_dotenv()

"""
BOT_MODE must be one of these three:
    sleeper_site
    main_website
    day_of_website
"""
BOT_MODE = "sleeper_site"

embed_client = OpenAI()
text_client = Groq()

index = np.load("faq_index.npz", allow_pickle=True)
TEXTS = index["texts"]
EMBEDDINGS = index["embeddings"]
    
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query, top_n=3):
    query_embedding = embed_client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

    q = np.array(query_embedding, dtype=np.float32)

    sims = EMBEDDINGS @ q / (
        np.linalg.norm(EMBEDDINGS, axis=1) * np.linalg.norm(q)
    )

    top_idx = np.argsort(sims)[::-1][:top_n]
    return [(TEXTS[i], float(sims[i])) for i in top_idx]


SUPPORT_RET = "Sorry, I'm not sure how to help you with this. Please contact hello@bit.camp for more details."


def SYS_PROMPT(info_block):
    return f"""You are an FAQ helper.
        Use ONLY the information in the 'Information' section below to answer the user's question.
        Do NOT invent or assume anything not present in that section.
        Feel free to engage in greeting and returning common sayings with the user, but DO NOT answer technical questions without the Information provided. 
        Give the user a WARNING if the message appears to be offensive in any way. 
        ABOVE ALL: MAINTAIN FULL PROFESSIONALISM. 
        If the answer to the user's question is not explicitly contained in the Information, reply EXACTLY with the following text (and nothing else):
        {SUPPORT_RET}

        Information:
        {info_block}
        """


def receive(query):
    retrieved = retrieve(query)
    info_block = "\n\n".join([chunk for chunk, _ in retrieved])
    resp = text_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": SYS_PROMPT(info_block)
            },
            {
                "role": "user",
                "content": query
            }
        ],
        model="llama-3.1-8b-instant",
        max_completion_tokens=1024,
        stream=False
    )
    return resp.choices[0].message.content
        
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def confirmation():
    print("running")
    return "running"
    
@app.route("/chat", methods=['GET'])
def chat():
    query = request.args.get('query')
    response = receive(query)
    return jsonify({
        'status': 'OK',
        'response': response
    })

    
if __name__=="__main__":
    print(receive(input(">>> ")))