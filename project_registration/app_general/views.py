from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key= os.getenv('OPENAI_API_KEY'),
)

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def chatbot_view(request):
    if request.method == 'POST':

        user_input = request.POST.get('message', '') 

      
        prompt = "You are a medical assistant program.  The patient is from Songkhla, Thailand. His name is Chinnapong.  Please help diagnose his question, and guide him. "
        prompt += "Here is his message in Thai Language: " + user_input

       
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        # Extract the response text from the API response
        response_text = response.choices[0].message.content.strip()

        # Set the response text in the context dictionary
        context = {
            "result": response_text
        }


        # Render the template with the context containing the response
        return render(request, 'app_general/home.html', context)

    else:
        return render(request, 'app_general/home.html' )