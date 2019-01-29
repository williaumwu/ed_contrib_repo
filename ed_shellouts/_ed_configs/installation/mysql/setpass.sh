#!/bin/bash

SetRootPassword()
{
        if [ "$DB_ROOT_PASS" = "**Random**" ]; then
            unset DB_ROOT_PASS
        fi

        export PASS=${DB_ROOT_PASS:-$(pwgen -s 12 1)}
        export USER=${DB_ROOT_USER:-"root"}

        echo "=> Setting MySQL user ${USER} with ${PASS} password"

        mysqladmin -u ${USER} password $PASS

        echo "=> Done!"
        echo "========================================================================"
        echo "You can now connect to this MySQL Server using:"
        echo ""
        echo "    mysql -u$USER -p$PASS -h<host> -P<port>"
        echo ""
        echo "========================================================================"
}

SetRootPassword

