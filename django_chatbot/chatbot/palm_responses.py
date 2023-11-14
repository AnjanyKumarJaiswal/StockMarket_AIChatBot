import django as pd 
import google.generativeai as palm
import os 
import json
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
API_KEY = "AIzaSyD98IrWpvfg_I8vubfT-3m1bUHsKCZ90ys"
palm.configure(api_key=API_KEY)
model_list=[_ for _ in palm.list_models()]
model_id='models/text-bison-001'
def chatbot(prompt):
    """Generates a response to the given prompt using PALM."""
    if prompt is not None:
        if "write" in prompt or "report" in prompt:
            completion = palm.generate_text(
                model=model_id,
                prompt=prompt,
                temperature=0.99,
                max_output_tokens=2500,
                candidate_count=1
            )
            outputs = [output['output'] for output in completion.candidates]

            for output in outputs:
                print(output)
                print('-'*50)

        else:
            examples = [
                ("What is Stock Market"),
                ("What is the status of sensex today"),
                ("Why should I invest in stock market"),
                ("What is sensex"),
                ("What is the best stock market to invest in currently?"),
                ("Suggest me few stock market that takes less money"),
                ("Which tech giants companies stockn market should I invest in?"),
                ("What is the current stock rate of companies like Google,Microsoft,Apple,Amazone")
            ]
        try:
            response = palm.chat(
                messages=prompt,
                temperature=0.2,
                context='Speak like a Stock Market Analyst',
                
            )

            # Handle any errors that may occur when calling the PALM API.
        except Exception as e:
            print(e)
            return

        for message in response.messages:
            print(message['content'])
    else:
        return HttpResponseBadRequest("Prompt is required")
            
if __name__ == "__main__":
  prompt = input()
  chatbot(prompt)
  from chatbot import palm_responses

def palmapi(request):
  """Returns a response from the chatbot."""

  prompt = request.GET.get('prompt')
  palm_api = palm_responses.chatbot(prompt)

  return HttpResponse(palm_api, content_type='text/plain')

