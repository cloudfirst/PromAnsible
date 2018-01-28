#! /bin/bash

mysql -uroot -proot mysql < init_db.sql
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python ../../manage.py shell
