FROM httpd:2.4
COPY ./website/ /usr/local/apache2/htdocs/
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./.htpasswd /usr/local/apache2/.htpasswd
RUN chown -hR www-data:www-data /usr/local/apache2/

RUN apt-get update; apt-get install python2 python3 -y --no-install-recommends

#CMD [ "python3", "/usr/local/apache2/htdocs/create-db.py"] 
