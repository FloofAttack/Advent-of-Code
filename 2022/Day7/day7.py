# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:51:44 2022

@author: sfoster
"""
import sys
import numpy as np

def line_reader(lines):
    output_lines = []
    for i in range(0,len(lines)):
        if i < len(lines):
            output_lines.append(lines[i].split("\n")[0])
        else:
            output_lines.append(lines[i])
    return output_lines

class directory:
    def __init__(self,name):
        self.name = name
        # a "disk_object" can be either a FILE or DIRECTORY
        self.contents = []
        
    def add_item(self,item):
        self.contents.append(item)
        
    def total_size(self):
        total = 0
        for i in self.contents:
            if isinstance(i,file_item):
                total += int(i.size)
            elif isinstance(i,directory):
                total += i.total_size()
        return total
    
    def cwd(self,stack):
        cwd = self
        cwd_contents = cwd.contents
        for s in stack[1:]:
            for c in cwd_contents:
                if isinstance(c,directory) and c.name == s:
                    cwd = c
                    cwd_contents = cwd.contents
        return cwd
    
    def get_sub_dir_object(self,subdir):
        flag = False
        for c in self.contents:
            if isinstance(c,directory) and c.name == subdir:
                flag = True   
        return flag
        
class file_item:
    def __init__(self,name,size):
        self.name = name
        self.size = size
        
# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)
 
# a = directory("a",file_item("test_file",123))

# create a directory called "dir1" in the variable a (root)
a = directory("dir1")
a.add_item(file_item("file1",1))
a.add_item(file_item("file2",2))
a.add_item(file_item("file3",3))
a.add_item(directory("dir2"))

# add a directory!
a.get_sub_dir_object("dir2")

##############################################################################################
# Part 1
# Building the tree: capturing all directories and files.
dir_stack = []
level = 0
root = directory("/")
dir_stack.append("/")
all_subdirs = []

# file tree builder
for i in range(1,len(lines)):
# for i in range(1,10):    
# assume we always start from root: $ cd /

    if "$ cd" in lines[i] and "$ cd .." not in lines[i]:
        # we are in a different directory
        dir_stack.append(lines[i].split(" ")[2])
    
    if "$ cd .." in lines[i]:
        # pop off the directory stack
        dir_stack.pop()

    if "$ ls" in lines[i]:
        # if we ask to list: loop through lines between $
        for j in range(i+1,len(lines)):
            if "$" in lines[j]:
                break
            else:
                if lines[j].split(" ")[0] == "dir":
                    dir_name = lines[j].split(" ")[1]
                    cwd = root.cwd(dir_stack)
                    cwd.add_item(directory(dir_name))
                else:
                    file_size = lines[j].split(" ")[0]
                    file_name = lines[j].split(" ")[1]
                    cwd = root.cwd(dir_stack)
                    cwd.add_item(file_item(file_name,file_size))
    if cwd not in all_subdirs:
        all_subdirs.append(cwd)    
                    
# bang all the directories into a list of items to be checked for sizes
# create an empty list to store directories
sub_sizes = []
sub_names = []
for s in all_subdirs:
    sub_sizes.append(s.total_size())
    sub_names.append(s.name)

# find all directories with size > 100000
sum = 0
for i in range(1,len(sub_sizes)):
    if sub_sizes[i] <= 100000:
        print(sub_names[i])
        sum += sub_sizes[i]
        
print(f"sum of dirs meeting criteria {sum}")

################################################################
# Part 2
disk_capacity = 70000000
required_space = 30000000
remaining_space = disk_capacity - sub_sizes[0]
required_to_free = required_space - remaining_space

dirs_to_consider = []
for i in range(1,len(sub_sizes)):
    if sub_sizes[i] >= required_to_free:
        dirs_to_consider.append(sub_sizes[i])
# find name of the smallest dir in dirs_to_consider
print(np.min(dirs_to_consider))