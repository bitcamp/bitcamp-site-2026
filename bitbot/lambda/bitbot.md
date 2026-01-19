# BitBot System Documentation
Using Retrieval-Augmented Generation (RAG), BitBot allows an LLM to answer questions based on a useful subset of the local FAQ dataset rather than hallucinating off training data. 

## Components
### `build_index.py`
Processes raw data from `faq.json` into formatted Q/A that the bot can search. Filters the data based on specified `BOT_MODE`. Uses OpenAI's `text-embedding-3-small` embedding model to convert text strings into numerical vector embeddings. Saves embeddings as a compressed NumPy file `faq_index.npz`. 

### `bitbot.py`
Live bot that interacts with the frontend. The `retrieve` function returns the top 3 best results which are fed to the LLM in the system prompt. Uses `llama-3.1-8b-instant` via Groq API. Returns a strict fallback message if no viable data is found. Prompt may be changed in future versioning. 

## Maintenance/Deployment

FOLLOW THESE STEPS WHEN YOU HAVE NEW QUESTIONS FOR THE FAQ OR YOU WANT TO CHANGE BOT MODE:

STEP 1:
Make appropriate edits to `faq.json` as needed, and change the `BOT_MODE` variable to the correct key from `faq.json`. 

STEP 2:
Run the script locally to generate a new index: `python build_index.py` (ensuring dependencies are installed: `pip install -r requirements.txt` and the environment file `.env` is configured with `OPENAI_API_KEY`). 

Finally, upload the new `faq_index.npz` to the AWS Lambda production environment under function name `bitbot`. 

STEP 3:
You would want to have the following in your local vscode environment under ../bitbot/lambda: (bitbot.py, build_index.py, faq_index.npz, faq.json, lambda_function.py, requirements.txt) you can IGNORE everything else except if you see a lambda_package.zip then delete that

STEP 4:
make sure you are in the directory ../bitbot/lambda and run the following:
wsl bash -c "cd build && zip -r ../lambda_package.zip . && cd .. && zip -g lambda_package.zip lambda_function.py bitbot.py faq.json faq_index.npz build_index.py requirements.txt"

this will create a zipfile, now go to the lambda funciton on aws and click upload from then choose .zip file and upload the generated zip file (will be called lambda_package.zip)