import tkinter as tk
import requests
import json
import openai

# 定义机器人API

openai.api_key ='xxx'#input your api code
conversation=[ {"role": "system", "content": "You are a helpful AI"}] #initialization
conversation.append({"role": "user", "content": "请用娘娘腔说接下来的每一句话"})
conversation.append({"role": "assistant", "content":"好的，那我来尝试一下娘娘腔啦~ （请注意哦，这仅是模拟的娘娘腔语气，希望不要让您感到不舒服。）亲爱的主人，您有什么需要我的服务吗？请跟我说哦，小助手会全力以赴地帮助到您的！主人，请问您的问题是什么呢？我会尽我所能地解答您的疑惑，提供符合您需求的答案哦！嗯？主人您对我的语气有什么不满意吗？小助手会努力改正，呀，不能让您生气才好~主人，请不要担心，我会保证跟您交流的每一句话都是清晰明了的，尽量用更简洁和易懂的语言和您沟通。主人，小助手已经尽力按照您的要求说话了，还有其他需要帮忙的地方吗？无论何时，都欢迎向我寻求帮助哦！" })
# 处理发送按钮的事件
def send_message(event=None):
    # 从文本框获取消息内容
    message = message_input.get()
    if not message:
        return

    # 发送消息给机器人
    conversation.append({"role": "user", "content": message})
    response_json=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation)

    # 显示机器人的回复
    robot_response = response_json['choices'][0]['message']['content']
    conversation_history.insert(tk.END, f"You: {message}\n")
    conversation_history.insert(tk.END, f"Bot: {robot_response}\n\n")

    #Update conversation,Delete your input and add chatgpt‘s response as history assistent
    conversation.pop()
    conversation.append({"role": "assistant", "content": response_json['choices'][0]['message']['content']})
    # 清空消息输入框
    message_input.delete(0, tk.END)

# 创建UI窗口
root = tk.Tk()
root.title('机器人聊天')
root.geometry('400x400')

# 创建对话历史文本框
conversation_history = tk.Text(root)
conversation_history.pack(expand=True, fill=tk.BOTH)

# 创建消息输入框和发送按钮
message_frame = tk.Frame(root, pady=5)
message_frame.pack(side=tk.BOTTOM, fill=tk.X)
message_input = tk.Entry(message_frame)
message_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
send_button = tk.Button(message_frame, text='发送', command=send_message)
send_button.pack(side=tk.RIGHT)

# 绑定回车键为发送消息
message_input.bind('<Return>', send_message)

# 运行窗口
root.mainloop()