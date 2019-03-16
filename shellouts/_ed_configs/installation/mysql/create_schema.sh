#!/bin/bash
  
MYSQL=`which mysql`

SCRIPT_DIR=${SCRIPT_DIR:="/var/tmp"}
SQL_FILE=${SQL_FILE:="/var/tmp/seed.sql"}
cd $SCRIPT_DIR
$MYSQL -u "$DB_USER" -p"${DB_PASS}" $DB_NAME -h $DB_HOST < $SQL_FILE
