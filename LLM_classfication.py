import os
from openai import OpenAI
import requests
import json
from memory import save_memory
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url=os.environ.get("API_URL"))

save_dir=os.environ.get("save_dir")#Input your folder dir
file_name="carrot_memory.jsonl"
path = os.path.join(save_dir, file_name)
def filter_memory(user_input):
    """
    记忆分类器：判断用户的输入是否有长期保存的价值
    """
    filter_prompt = """
    你是一个冷酷无情的记忆分类器。你只需要判断用户的输入是否包含感情丰富的，长期的、结构化的重要信息（如个人喜好、近期重大计划、人际关系等）。
    如果是无价值的日常闲聊，返回 {"is_important": false, "fact": ""}。
    如果有价值，提炼成第三人称的简短陈述句，返回 {"is_important": true, "fact": "提炼的事实"}。
    记住只输出JSON!!!!不要任何废话!!!!!!
    """
    response = client.chat.completions.create(
        model=os.environ.get("MODEL"),
        messages=[
            {"role": "system", "content": filter_prompt},
            {"role": "user", "content": user_input}
        ],

        response_format={"type": "json_object"}, 
        temperature=0.1
    )
    result_str = response.choices[0].message.content

    try:
        result_dict = json.loads(result_str)
        if result_dict.get("is_important"):
            save_memory(result_dict,path)
        return result_dict
    except:
        return {"is_important": False, "fact": ""}