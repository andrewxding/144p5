import sys, random
from locust import HttpLocust, TaskSet

def updatePost(locust):
    postid = random.randint(1, 500)
    prefix = '/api/cs144'
    url = prefix + '/{num}'.format(num=postid)
    locust.client.put(url, {"title": "Loading Test", "body": "***Hello World!***"}, name=prefix)

class MyTaskSet(TaskSet):
    tasks = [updatePost]
    def on_start(locust):
        # locust.client.get("/login?username=cs144&password=password&redirect=/", name='/login')
        response = locust.client.post("/login", data={"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit()

class MyLocust(HttpLocust):
    task_set = MyTaskSet