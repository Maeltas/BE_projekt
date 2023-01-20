FROM prestashop/prestashop:1.7.8.7-apache

COPY backup/*.tar.gz /tmp/
COPY post_install.sh /tmp/post-install-scripts/
COPY cert/selfsigned.crt /etc/ssl/certs/
COPY cert/selfsigned.key /etc/ssl/private/
COPY cert/ssl.conf /etc/apache2/sites-available/default-ssl.conf

RUN a2enmod ssl
RUN a2ensite default-ssl
