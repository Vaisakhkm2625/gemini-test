"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI'])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi there"]
  },
  {
    "role": "model",
    "parts": ["Hello! How can I assist you today?"]
  },
])

convo.send_message("<div class=\"document-embed drive-embed\" contenteditable=\"false\" data-drive-file-name=\"out.pdf\" data-drive-file-id=\"1duwHBKTPPKXJ9VwdepGHszaz5xCsIcq-\" data-drive-file-or-folder-id=\"1duwHBKTPPKXJ9VwdepGHszaz5xCsIcq-\" data-drive-folder-name=\"\" data-blot-name=\"document-embed\"><div class=\"inner-container\"><span class=\"document-embed-loading google-symbols\" style=\"display: block;\">progress_activity</span><span class=\"document-embed-icon material-symbols-outlined\" aria-hidden=\"true\" style=\"display: none;\">docs</span><span class=\"document-embed-label gmat-body-medium truncate\" title=\"out.pdf\" alt=\"out.pdf\" aria-label=\"out.pdf\">out.pdf</span><span class=\"document-embed-token-count gmat-body-medium\">Extracting</span></div></div><br>")
print(convo.last.text)
