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
        write_me(path = queue, data = str(datetime.now()) + " | " + url, isOverWrite = 1) #TODO: Format pretty
    if not os.path.isfile(crawled):
        write_me(path = crawled, data = "", isOverWrite = 1)

def write_me(path, data, isOverWrite):
    if isOverWrite:
        file = open(path, 'w')
        if len(data) > 0:
            file.write(data)
        file.close()
    else:
        with open(path, 'a') as file:
            file.write(data + '\n')

def file_to_set(path):
    results = set()
    with open(path, 'rt') as file:
        for line in file:
            results.add(line.strip())
    return results

def set_to_file(path, data):
    for line in data:
        write_me(path = path, data = line, isOverWrite = 1)
    
