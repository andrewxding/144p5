import sys, random
from locust import HttpLocust, TaskSet

def updatePost(locust):
    postid = random.randint(1, 500) 
    prefix = '/editor/post?action=save'
    url = prefix + 'username=cs144&postid={num}&title=Loading%20Test&body=***Hello%20World!***'.format(num=postid)
    locust.client.post(url, name=prefix)

class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = [updatePost]

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet