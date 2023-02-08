# Libraries
import os
import openai
import json

# Variables
openai.api_key = "" # PUT YOUR API KEY HERE
running = True

# Starting Question
question = input("Enter your question: ")

# Main Loop
while running:
    
    # API Response (you may change the parameters if you want)
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=question,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    
    # Converting to string & retrieving just text value
    string = json.loads(str(response))
    answer = string["choices"][0]["text"]
    
    # Print answer 
    print(answer)
    
    # Ask question and repeat loop
    question = input("")
    
    # Break loop if user provides "stop"
    if question == "stop":
        break