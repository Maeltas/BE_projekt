#!/bin/bash

tar -xf /tmp/img.tar.gz -C /var/www/html && rm /tmp/img.tar.gz
echo "copied img"
chown -R www-data:www-data /var/www/html/img
echo "changed img owner"
tar -xf /tmp/modules.tar.gz -C /var/www/html && rm /tmp/modules.tar.gz
echo "copied modules"
chown -R www-data:www-data /var/www/html/modules
echo "changed modules owner"
tar -xf /tmp/img_import.tar.gz -C /var/www/html && rm /tmp/img_import.tar.gz
echo "copied img_import"
chown -R www-data:www-data /var/www/html/img_import
echo "changed img_import owner"
tar -xf /tmp/mails.tar.gz -C /var/www/html && rm /tmp/mails.tar.gz
echo "copied mails"
chown -R www-data:www-data /var/www/html/mails
echo "changed mails owner"
tar -xf /tmp/localization.tar.gz -C /var/www/html && rm /tmp/localization.tar.gz
echo "copied localization"
chown -R www-data:www-data /var/www/html/img/localization
echo "changed localization owner"
tar -xf /tmp/themes.tar.gz -C /var/www/html && rm /tmp/themes.tar.gz
echo "copied themes"
chown -R www-data:www-data /var/www/html/img/themes
echo "changed themes owner"

echo "post-install finished!"
