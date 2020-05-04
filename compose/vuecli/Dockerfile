FROM node:12.16.3-stretch

RUN yarn global add \
    vue \
    @vue/cli \
    webpack-cli
    

COPY yarn-install-start.sh /

CMD [ "/bin/bash" ]