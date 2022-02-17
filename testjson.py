# take id from user and check if the id matches with the id in the database

# import variables
import requests
import json

class Post():
    def __init__(self,userid,id,title,body):
            self.userid=userid
            self.id=id
            self.title=title
            self.body=body

    def __str__(self):
            return f'userid:{self.userid},id: {self.id},title: {self.title},body: {self.body}'

    def find_user_by_id():
            url='https://jsonplaceholder.typicode.com/posts/'
            response=requests.get(url).json()
            id=int(input('Enter a id: '))
            for post in response:
                url='https://jsonplaceholder.typicode.com/posts/'+str(id)
                response=requests.get(url).json()
                if id==post['id']:
                    print(response.__str__())
                    break
                



# test code

Post.find_user_by_id()       
