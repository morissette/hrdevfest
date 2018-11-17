FROM perl:5.20
RUN curl -L https://cpanmin.us | perl - -M https://cpan.metacpan.org -n Mojolicious::Lite
COPY categories.pl /usr/src/app/categories.pl
WORKDIR /usr/src/app
CMD ["perl", "./categories.pl", "daemon", "-m", "category-service", "-l", "http://*:80"]
