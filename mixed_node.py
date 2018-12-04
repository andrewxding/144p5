import sys, random
from locust import HttpLocust, TaskSet

def getPost(locust):
    postid = random.randint(1, 500)
    prefix = '/blog/cs144'
    url = prefix + '/{num}'.format(num=postid)
    locust.client.get(url, name=prefix)

def updatePost(locust):
    postid = random.randint(1, 500)
    prefix = '/api/cs144'
    url = prefix + '/{num}'.format(num=postid)
    locust.client.put(url, {"title": "Loading Test", "body": "***Hello World!***"}, name=prefix)

class MyTaskSet(TaskSet):
    tasks = {getPost: 9, updatePost: 1}
    def on_start(locust):
        response = locust.client.post("/login", data={"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit()

class MyLocust(HttpLocust):
    task_set = MyTaskSet