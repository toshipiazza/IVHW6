#!/usr/bin/env python2

# prints out a csv representing what files changed and when
# we use the csv format defined by
#   http://bl.ocks.org/WillTurman/4631136
# <key>,<value>,<date>

def datamineRepo(repo):
    pass

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--repo', help='url of repo to datamine')
    args = parser.parse_args()
    datamineRepo(args.repo)
