#!/bin/bash

export DB_ROOT_USER=${DB_ROOT_USER:-"root"}
export DB_ROOT_PASS=${DB_ROOT_PASS:-"admin123"}
export DB_NAME=${DB_NAME:-"testdb"}
export DB_USER=${DB_USER:-"testdb"}
export DB_PASS=${DB_PASS:-"testdb123"}
export DB_HOST=${DB_HOST:-"localhost"}

MYSQL=`which mysql`

Q1="CREATE DATABASE IF NOT EXISTS $DB_NAME;"
Q2="GRANT USAGE ON *.* TO $DB_USER@'%' IDENTIFIED BY '$DB_PASS';"
Q3="GRANT ALL PRIVILEGES ON $DB_NAME.* TO $DB_USER@'%';"
Q4="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}${Q3}${Q4}"

#$MYSQL -u "$DB_ROOT_USER" -p"${DB_ROOT_PASS}" -e "$SQL" -h $DB_HOST
#Hacked since I couldn't get MariaDB to take outside connections from admin account
#$MYSQL -u "$DB_ROOT_USER" -p"${DB_ROOT_PASS}" -e "$SQL" -h localhost || $MYSQL -u "$DB_ROOT_USER" -p"${DB_ROOT_PASS}" -e "$SQL" -h $DB_HOST || echo "yello"

STATUS=`$MYSQL -u "$DB_ROOT_USER" -p"${DB_ROOT_PASS}" -e "$SQL" -h localhost; echo $?`
echo ""

if [ $STATUS -eq 0 ]; then
    echo "Database credentials added to localhost"
    echo ""
    exit 0
fi

STATUS=`$MYSQL -u "$DB_ROOT_USER" -p"${DB_ROOT_PASS}" -e "$SQL" -h $DB_HOST; echo $?`

if [ $STATUS -eq 0 ]; then
    echo "Database credentials added to $DB_HOST"
    echo ""
    exit 0
fi

echo "ERROR - Database credentials not added to localhost or $DB_HOST"
echo ""
exit 1
