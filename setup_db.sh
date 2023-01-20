#!/bin/bash
sudo docker exec -ti admin-mysql_db.1.0wgtxijosd6k0no4gmlskxlmw mysql \
    -p "student" -u "root" -Bse "CREATE DATABASE IF NOT EXISTS BE_165229; CREATE USER IF NOT EXISTS 'BE_165229'@'%' IDENTIFIED BY 'BE_165229'; GRANT ALL PRIVILEGES ON BE_165229.* TO 'BE_165229'@'%' WITH GRANT OPTION;"
sudo docker exec -i admin-mysql_db.1.0wgtxijosd6k0no4gmlskxlmw mysql \
    -p "BE_165229" -u "BE_165229" BE_165229 < ./dump.sql
