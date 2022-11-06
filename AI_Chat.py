from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
 
# for a small or large model, change the word ‘medium’
model_name = "microsoft/DialoGPT-medium"
 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
nickname = input('Your nickname: ')
print('\nChat (ask a question to start a conversation): ')
 
for response_num in range(7):
     
    # ask bot something
    question = input('{}: '.format(nickname))
     
    # encode the input and add end of string token
    user_input = tokenizer.encode(question + tokenizer.eos_token, return_tensors="pt")
     
    # concatenate new user input with the chat history
    chatbot_input = torch.cat([chat_history, user_input], dim=-1) if response_num > 0 else user_input
     
    # generate a response
    chat_history = model.generate(
        chatbot_input,
        max_length=500,
        pad_token_id=tokenizer.eos_token_id,
    )
     
    #print the output
    chat = tokenizer.decode(chat_history[:, chatbot_input.shape[-1]:][0], skip_special_tokens=True)
     
    print(f"Bot: {chat}")