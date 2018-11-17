#!/bin/bash
docker run -d -v `pwd`:/usr/share/nginx/html -p 8080:80 -t sample/ui
