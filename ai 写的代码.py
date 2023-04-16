import openai
openai.api_key = "api"
# 定义一个聊天类
class Chat:
  def __init__(self,conversation_list=[]):
    # 初始化对话列表，可以加入一个key为system的字典，有助于形成更加个性化的回答
    # self.conversation_list = [ {'role':'system','content':'你是一个非常友善的助手'}]
    self.conversation_list = []

  # 打印对话
  def show_conversation(self,msg_list):
    for msg in msg_list:
      if msg['role'] == 'user':
        print(f"\U0001f47b: {msg['content']}\n")
      else:
        print(f"\U0001f47D: {msg['content']}\n")

  # 提问chatgpt
  def ask(self,prompt):
    self.conversation_list.append( {"role":"user","content":prompt})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=self.conversation_list)
    answer = response.choices[0].message['content']
    # 下面这一步是把chatGPT的回答也添加到对话列表中，这样下一次问问题的时候就能形成上下文了
    self.conversation_list.append( {"role":"assistant","content":answer})
    self.show_conversation(self.conversation_list)

# 创建一个聊天对象
chat = Chat()

# 循环输入问题，直到输入q退出
while True:
  prompt = input("请输入问题：")
  if prompt == "q":
    break
  else:
    chat.ask(prompt)