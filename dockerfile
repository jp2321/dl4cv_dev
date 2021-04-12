# Docker file for running Gatsby without installing node version 10 or Gatsby.
# Attribution: https://stackoverflow.com/questions/57405792/gatsby-not-rebuilding-whenever-mounted-code-changes
# Hayley Boyce (kinda not really), February 6th, 2020

# old
#FROM node:10

## Add the package.json file and build the node_modules folder
#WORKDIR /app
#COPY ./package*.json ./
#RUN mkdir node_modules
#RUN npm install --g gatsby-cli 
#RUN npm install


# new under node 12
FROM node:12

# Add the package.json file and build the node_modules folder
# Error with sharp 0.12.3 https://github.com/gatsbyjs/gatsby/issues/11026
# Added following lines
# RUN rm -rf node_modules
# RUN rm package-lock.json
# RUN npm install sharp

WORKDIR /app
COPY ./package*.json ./
RUN mkdir node_modules
RUN npm install --g gatsby-cli
RUN rm -rf node_modules
RUN rm package-lock.json
RUN npm install sharp
RUN npm install