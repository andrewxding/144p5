import sys, random
from locust import HttpLocust, TaskSet

def getPost(locust):
    postid = random.randint(1, 500)
    prefix = '/editor/post?action=open'
    url = prefix + '&username=cs144&postid={num}'.format(num=postid)
    locust.client.get(url, name=prefix)

class MyTaskSet(TaskSet):
    tasks = [getPost]

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    # min_wait = 1000
    # max_wait = 2000