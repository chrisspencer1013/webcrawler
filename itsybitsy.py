import os
from datetime import datetime

# will contain stuff for the actual crawler


def initialize(project_dir, url):
    if not os.path.exists(project_dir):
        print("Project Directory created at: " + project_dir)
        os.makedirs(project_dir)
    queue = project_dir + "/queue.txt"
    crawled = project_dir + "/all_links.txt"
    if not os.path.isfile(queue):
        write_me(path = queue, data = str(datetime.now()) + " | " + url, isNewFile = 1, isOverWrite = 1) #TODO: Format pretty
    if not os.path.isfile(crawled):
        write_me(path = crawled, data = "", isNewFile = 1, isOverWrite = 1)

def write_me(path, data, isNewFile, isOverWrite):
    if isOverWrite:
        file = open(path, 'w')
        if isNewfile:
            file.write(data)
        file.close()
    else:
        with open(path, 'a') as file:
            file.write(data + '\n')

        
