#!/usr/bin/env python2

# prints out a csv representing what files changed and when
# we use the csv format defined by
#   http://bl.ocks.org/WillTurman/4631136
# <key>,<value>,<date>

from __future__ import print_function
import datetime
import pygit2
import os

def datamineRepo(repo):
    # maps the commit time to the files changed
    git2csv = { }

    repo = pygit2.clone_repository(repo, "/tmp/datamine")
    flags = pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_REVERSE

    # get all entries changed per commit
    for commit in repo.walk(repo.head.target, flags):
        for entry in commit.tree:
            git2csv[commit.commit_time] = [
                entry.name for entry in commit.tree
                    ]

    # maps time -> file extension -> number of those
    # files changed
    flat_csv = { }
    for time in git2csv:
        for file_changed in git2csv[time]:
            extension = os.path.splitext(file_changed)[1]
            try:
                flat_csv[time][extension] += 1
            except:
                try:
                    flat_csv[time][extension] = 1
                except:
                    flat_csv[time] = {
                        extension: 1
                            }

    # print
    for time in flat_csv:
        for ext in flat_csv[time]:
            if ext == "":
                ext_out = "unknown"
            else:
                ext_out = ext
            dtime = datetime.datetime.fromtimestamp(time).strftime('%m/%d/%Y')
            print(ext_out,",",flat_csv[time][ext],",",dtime)


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='log data about a repo')
    parser.add_argument('--repo', help='url of repo to datamine', required=True)
    args = parser.parse_args()
    datamineRepo(args.repo)
