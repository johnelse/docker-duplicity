#!/usr/bin/env python

"""
Helper script for launching duplicity in a docker container.
"""

import argparse
import os
import subprocess
import sys


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('configfile', nargs=1,
                        help='Configuration file')
    parser.add_argument('backupdir', nargs=1,
                        help='Root directory to be backed up')

    args = parser.parse_args(sys.argv[1:])
    image = "%s/duplicity" % os.getenv("USER")
    docker_args = [
        "docker", "run", "-it", "--rm", "--name", "duplicity",
        "-h", "duplicity.johnel.se",
        "-v", "%s:/tmp/duplicity/config/%s:ro"
            % (args.configfile[0], os.path.basename(args.configfile[0])),
        "-v", "%s:/tmp/duplicity/backupdir:ro" % args.backupdir[0],
        image,
        "/usr/local/bin/backup.sh"
        ]
    sys.stderr.write("Launching docker with args %s\n" % docker_args)
    subprocess.call(docker_args)


if __name__ == "__main__":
    main()
