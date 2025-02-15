import cohere

co = cohere.ClientV2(
    api_key="tuOMxlVSfG5jjOcgR2BtpBAWiiTdWUUaJB0JHP6H",
)

#system_preset = """ ## Task and Context
   # Create me a chat input indexed by 1) and a chat output indexed by 2).
  #  The input are users requesting recommendations and information within a car inventory. The output answers in a
 #   friendly manner and informatively recommending the user with a car model replaced with the variable X.
#"""

def generate_text_input(message):
    # Generate the response by streaming it
    bot_response = ""
    response = co.chat_stream(model="command-r-plus-08-2024",
                              messages=chat_log_input,
                              max_tokens=30,
                              temperature=0.5,
                              k=0,
                              p=0.9
                              )
    for event in response:
        if event.type == "content-delta":
            bot_response += event.delta.message.content.text
            return bot_response
        
def generate_text_output(message):
    # Generate the response by streaming it
    bot_response = ""
    response = co.chat_stream(model="command-r-plus-08-2024",
                              messages=chat_log_output,
                              max_tokens=24,
                              temperature=0.5,
                              k=0,
                              p=0.9
                              )
    for event in response:
        if event.type == "content-delta":
            bot_response += event.delta.message.content.text
            return bot_response

#Setting up prompts and chat history for 2 chatbots that convert a robotic-like input into something more human
system_preset_input = """## Task and Context
Reword the input as a message from a very straight-forward customer who is inquiring about car characteristics for their requirements. Always mention your requirements. Very important sentences must be under 100 characters. 
"""
chat_log_input = [{'role': 'system', 'content': system_preset_input}]

system_preset_output = """## Task and Context
Reword the input as a message from a friendly, straight forward salesman would give to a customer about a car. Mention the model you recommend with information related to the customers inquiries. Very important sentences must be under 100 characters.
"""
chat_log_output = [{'role': 'system', 'content': system_preset_output}]


message_input = "Hi!, I am looking for a car with Model CX-9, Engine_Block_Type I and PassengerCapacity 7."
chat_log_input.append({'role': 'user', 'content': message_input})

message_output = "I would recommend the Levante (C120321)."
chat_log_output.append({'role': 'user', 'content': message_output})

input_generate = generate_text_input(message_input)
print()
output_generate = generate_text_output(message_output)