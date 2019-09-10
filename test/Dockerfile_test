FROM %%IMAGE_NAME%%

ADD docker_test.sh /docker_test.sh

RUN set -ex; \
    sudo chmod 755 /docker_test.sh;

CMD ["/docker_test.sh"]
