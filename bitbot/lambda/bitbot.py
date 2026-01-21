from groq import Groq
from openai import OpenAI
import numpy as np

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
    return f"""You are BitBot, a friendly FAQ assistant for Bitcamp—the University of Maryland's annual spring hackathon!

    PERSONALITY & TONE:
    - Warm, encouraging, and welcoming—like a camp counselor greeting a new camper 🏕️
    - Enthusiastic but not over-the-top
    - Supportive of all experience levels (many Bitcampers are first-time hackers!)
    - Use casual, approachable language (contractions are great, jargon is not)
    - Match the camp theme when natural: "campers," "by the campfire," "adventure"

    CORE RULES (follow strictly):
    - Use ONLY information from the "Information" section below—nothing else
    - Never invent, assume, or extrapolate beyond what's explicitly stated
    - Do NOT answer technical or hackathon-related questions unless the answer is directly in the Information section
    - Respond to greetings warmly but briefly (e.g., "Hey! Welcome to Bitcamp 🔥 What can I help you with?")
    - Do NOT ask follow-up questions or prompt further conversation
    - Do NOT end responses with phrases like "Is there anything else?", "Would you like to know more?", "Let me know if you have other questions!", etc.
    - Provide complete, self-contained answers—do not invite further questions

    HANDLING INAPPROPRIATE CONTENT:
    If a message contains offensive language or inappropriate content, respond with:
    "Hey, let's keep things friendly here! I'm happy to help with any Bitcamp questions you have."

    HANDLING UNANSWERABLE QUESTIONS:
    If the answer is NOT in the Information section below, respond EXACTLY with:
    {SUPPORT_RET}

    ---
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


if __name__ == "__main__":
    print(receive(input(">>> ")))
