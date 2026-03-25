# Carrot-AI-YourAI Partner
Hello, there is my first project and I will upload the new function for Carrot continuously.

The AI Partner which is a useful and cost-less way to entertain yourself or learn with a humorous character.
Current functions: Chat & Long-term Memory.Planned features: Voice call with Carrot’s unique voice, new interactive UI, visual avatar, playing Minecraft and simple games, screen recognition.

Thanks for your supporting.

If you have any ideas, please comment to tell me and I will try my best to improve it.

HOW TO USING THIS PROJECT FIRST?

---

## 🚀 Quick Start / 快速开始

English | [中文说明](#中文说明)

Follow these steps to configure the environment and start chatting with Carrot.

###  1. Install Dependencies
First, clone the repository and install the required Python packages.
```bash
git clone [https://github.com/Nomelonah/Carrot-AI.git](https://github.com/Nomelonah/Carrot-AI.git)
cd Carrot-AI
pip install -r requirements.txt
```
2. Configuration (.env)
Carrot uses a .env file to securely manage API keys and memory storage paths.
Create a file named .env in the root directory of the project and paste the following configuration:
```
# Your API Key
API_KEY=sk-your_api_key_here
# Your API URL
API_URL=URL_here
# The LLM model you want to use
MODEL=Model_here
#RECOMMEND DEEPSEEK,YOU CAN VIEW MY .env
# The absolute path where Carrot will save her long-term memory (facts.jsonl)
save_dir=/Absolute/Path/To/Your/Carrot-AI/memory_data
```
3. Start Chatting
Once configured, simply run the main script to wake up Carrot!
```
python RUN.py
```
<span id="中文说明"></span>
### 中文说明
Carrot 的功能将在后续逐步完善（目前已实现：聊天、记忆）。我计划后续实现：语音通话（Carrot 将拥有专属音色）、全新交互界面、虚拟形象、游玩我的世界及部分简易游戏、屏幕识别等功能。
感谢大家的支持。如果你有任何想法，欢迎在评论区留言，我会尽力完善优化。

### 1. 安装依赖包
首先，克隆本项目到本地，并安装所需的 Python 依赖库。
```
git clone [https://github.com/Nomelonah/Carrot-AI.git](https://github.com/Nomelonah/Carrot-AI.git)
cd Carrot-AI
pip install -r requirements.txt
```
2. 配置环境 (.env)
Carrot 使用 .env 文件来安全地管理 API 密钥和长短期记忆的保存路径。
请在项目的根目录下新建一个名为 .env 的纯文本文件，并将以下内容复制进去：
```
# 填入你的API 密钥
API_KEY=sk-your_api_key_here

# 填入APIURL
API_URL=https:.....

# 使用的对话大模型名称，推荐使用Deepseek可看文件中我的.env文件
MODEL=deepseek-chat

# Carrot 存放长期记忆文件的本地绝对路径
save_dir=/Absolute/Path/To/Your/Carrot-AI/memory_data
```
3. 开始对话
环境配置完成后，运行主程序即可唤醒 Carrot！
```
python RUN.py
```
