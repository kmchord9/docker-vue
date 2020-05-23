FROM node:12.16.3-stretch as build-stage

COPY src/vuecli /code
COPY .envs/.env /code/
WORKDIR /code

RUN yarn global add \
    vue \
    @vue/cli \
    webpack-cli &&\
    yarn install &&\
    yarn run build 

FROM httpd:alpine
COPY --from=build-stage /code/dist /usr/local/apache2/htdocs/
COPY compose/apache/my-httpd.conf /usr/local/apache2/conf/httpd.conf