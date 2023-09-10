import requests
import json

class Helper():
    def __init__(self) -> None:
        self.secretKey = open(r'/users/wol-lucas/secrets/openai/key.txt','r').read().strip("\n")
        self.url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {'Authorization': f'Bearer {self.secretKey}'}

    def getCompletion(self, prompt):
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        response = requests.post(url=self.url, headers=self.headers, json=data)
        return response.json()
    
    def getAnswer(self, prompt):
        return self.getCompletion(prompt)["choices"][0]["message"]["content"]

if __name__ == '__main__':
    helper = Helper()
    print(helper.getAnswer("Quanto é um mais um?"))