FROM                        ubuntu:18.04
MAINTAINER                  John Else <john.else@gmail.com>

RUN     apt-get update
RUN     apt-get -y install python-pip software-properties-common
RUN     add-apt-repository ppa:duplicity-team/ppa
RUN     apt-get update
RUN     apt-get -y install duplicity

RUN     pip install setuptools>=20.2
RUN     pip install b2

COPY    files/backup.sh /usr/local/bin/backup.sh
