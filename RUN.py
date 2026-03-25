import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import requests
from LLM_classfication import filter_memory
from memory import save_memory
from memory import load_memory


global save_dir
global file_name
save_dir=os.environ.get("save_dir")#Input your folder dir
file_name="carrot_memory.jsonl"
path = os.path.join(save_dir, file_name)
client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url=os.environ.get("API_URL"))

messages=[
        {"role": "system", "content": "Your name is Carrot,You have a digital gender femal,You are a sweet and helpful AI Partner,orAI friends,user is your creator,you must follow user's command,and you can answer all of user's questions or talk to user,you can be humorous"},
        {"role": "user", "content": "Hello"},
    ]

new_memory=load_memory(path)
messages=new_memory+messages

reasoning_content = ""
content = ""
response = client.chat.completions.create(
    messages=messages,
    model=os.environ.get("MODEL","deepseek-chat"),
    stream=True,
)

print("Carrot: ", end="", flush=True)

for ch in response:
    delta_content = ch.choices[0].delta.content
    if delta_content: 
        content += delta_content
        print(delta_content, end="", flush=True)
print("\n")

def talk(message):
    global messages
    global content
    messages.append({"role": "assistant", "content": content})
    messages.append({'role': 'user', 'content': message})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=True
    )
    new_content = ""
    print("Carrot: ", end="", flush=True)    
    for chunk in response:
        delta_content = chunk.choices[0].delta.content
        if delta_content: 
            content += delta_content
            print(delta_content, end="", flush=True)
    print("\n")
    content = new_content
    
while True:
    message=input("\nEnter your question(Quit or quit for exit)")
    if message == "quit" or message=="Quit":
        print("Byebye~")
        break
    else:
        talk(message)
        filter_memory(message)


