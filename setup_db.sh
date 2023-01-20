#!/bin/bash
sudo docker exec -i BE_165229_DB mysql \
    -p "BE_165229_DB" -u "root" BE_171884 < ./dump.sql
