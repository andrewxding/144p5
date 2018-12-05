import sys, random
from locust import HttpLocust, TaskSet

def getPost(locust):
    postid = random.randint(1, 500)
    prefix = '/editor/post?action=open'
    url = prefix + '&username=cs144&postid={num}'.format(num=postid)
    locust.client.get(url, name=prefix)

def updatePost(locust):
    postid = random.randint(1, 500) 
    prefix = '/editor/post?action=save'
    url = prefix + '&username=cs144&postid={num}&title=Loading%20Test&body=***Hello%20World!***'.format(num=postid)
    locust.client.post(url, name=prefix)

class MyTaskSet(TaskSet):
    tasks = {updatePost: 1, getPost: 9}

class MyLocust(HttpLocust):
    task_set = MyTaskSet