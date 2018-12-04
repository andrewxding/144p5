import sys, random
from locust import HttpLocust, TaskSet

def getPost(locust):
    postid = random.randint(1, 500)
    prefix = '/blog/cs144'
    url = prefix + '/{num}'.format(num=postid)
    locust.client.get(url, name=prefix)

class MyTaskSet(TaskSet):
    tasks = [getPost]

class MyLocust(HttpLocust):
    task_set = MyTaskSet