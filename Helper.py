import requests
import pyperclip

class Helper():
    def __init__(self) -> None:
        self.secretKey = open(r'/users/wol-lucas/secrets/openai/key.txt','r').read().strip("\n")
        self.url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {'Authorization': f'Bearer {self.secretKey}'}
        self.doServe()

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

    def doServe(self):
        while True:
            prompt = self.getPrompt()
            answer = self.getAnswer(prompt)
            pyperclip.copy(answer) #copying answer to clipboard
            print(answer + "\n\n<Answer on your clipboard :)>")

    def getPrompt(self):
        print("?") #sem um print aparente para o usuário pois é para ser discreto.
        return input()




if __name__ == '__main__':
    helper = Helper()
