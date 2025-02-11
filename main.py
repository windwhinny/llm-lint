import os
from openai import OpenAI
import ollama

project_root = os.path.dirname(__file__)
rules_dir = os.path.join(project_root, 'rules')

files = [f for f in os.listdir(rules_dir) if f != 'main.md']

rule_prompt = ''
for file in ['main.md'] + files:
    if not file in ['main.md', 'rule1.md']:
        continue
    f = open(os.path.join(rules_dir, file))
    content = f.read()
    rule_prompt = rule_prompt+content.strip()+'\n\n'

rule_prompt += '下面是需要被检查的代码：\n\n'

sample_path=os.path.join(project_root, 'test', 'sample.js')
test_prompt = open(sample_path).read()

rule_prompt = rule_prompt + '```js\n' + test_prompt + '\n```'

messages = [{
    "role": "user",
    "content": rule_prompt,
}]

def chat_with_ollama():
    print('starting ollama')
    response = ollama.chat('deepseek-r1:32b', messages=messages)
    print(response['message']['content'])

def chat_with_api():
    client = OpenAI(api_key="sk-75402e85b35e423ba73e18e105065d79", base_url="https://api.deepseek.com/beta")
    print('send request-----------')
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages,
        stop=[']']
    )

    reasoning_content = response.choices[0].message.reasoning_content
    content = response.choices[0].message.content

    print(reasoning_content)
    print('response-----------')
    print(content)

chat_with_ollama()