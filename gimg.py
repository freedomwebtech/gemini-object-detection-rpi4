import os
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage, ImageBlock,MessageRole, TextBlock

img_path="2.jpg"


os.environ["GOOGLE_API_KEY"] = "AIzaSyDjJRCQS235Lozk3vmBnEOZZR5yiyiNBUs"




gemini_pro = Gemini(model_name="models/gemini-1.5-flash")

msg = ChatMessage(
    role=MessageRole.USER,
    blocks=[
        TextBlock(text="can you difference between of them"),
        ImageBlock(path=img_path, image_mimetype="image/jpeg"),
    ],
)

response = gemini_pro.chat(messages=[msg])
print(response.message.content)
