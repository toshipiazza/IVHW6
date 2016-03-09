#!/usr/bin/env python2

# prints out a csv representing what files changed and when
# we use the csv format defined by
#   http://bl.ocks.org/WillTurman/4631136
# <key>,<value>,<date>

import pygit2

def datamineRepo(repo):
    repo = pygit2.clone_repository(repo, "/tmp/datamine")
    flags = pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_REVERSE
    for commit in repo.walk(repo.head.target, flags):
        print(commit.message) # or some other operation

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--repo', help='url of repo to datamine')
    args = parser.parse_args()
    datamineRepo(args.repo)
