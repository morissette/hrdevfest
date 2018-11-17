FROM tiangolo/uwsgi-nginx:python3.6

# This should be in its own container but for simplicity sake
RUN apt-get update && \
    apt-get install -y mongodb

ENV UWSGI_INI /app/uwsgi.ini
ENV LISTEN_PORT 80

# Setup supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/bin/supervisord"]
