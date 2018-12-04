import sys, random
from locust import HttpLocust, TaskSet

def getList(locust):
    locust.client.get('/api/cs144')
    locust.client.get('/editor/post?action=list&username=cs144')

def previewPage(locust):
    postid = random.randint(1, 500) # generate a random number from 1 to 100 (include 1 and 100)
    url_prefix = '/blog/cs144/'
    locust.client.get(url_prefix + str(postid), name=url_prefix)

class MyTaskSet(TaskSet):
    tasks = {getList: 2, previewPage: 1}
    def on_start(locust):
        response = locust.client.post("/login", {"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit();

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000