import openai

def echo(user_input):
    return f"GPT Echo 결과값: {user_input}"

# Example usage of the echo function
user_input = "오늘 날씨 어때?"
result = echo(user_input)
print(result)

# Uncomment the following code when you want to use the OpenAI API
# import openai
# openai.api_key = "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"
#
# def chatGPT(user_input):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ],
#         response_format={"type": "json_object"}
#     )
#
#     return response['choices'][0]['message']['content']
#
# # Example usage of the chatGPT function
# user_input = "오늘 날씨 어때?"
# result = chatGPT(user_input)
# print(result)
