# base image
FROM ubuntu:latest

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# install node8
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_8.x  | bash -
RUN apt-get -y install nodejs

EXPOSE 3000

# install script
COPY script/* /script/
RUN chmod -R +x /script

ENV PATH /script:$PATH

# idle the container
CMD tail -f /dev/null
