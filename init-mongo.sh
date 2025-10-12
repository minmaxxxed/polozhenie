#!/bin/bash

MONGO_INITDB_ROOT_PASSWORD_QUOTED=$(jq --arg v "$MONGO_INITDB_ROOT_PASSWORD" -n '$v')
DB_PASSWORD_QUOTED=$(jq --arg v "$DB_PASSWORD" -n '$v')
DB_USERNAME_QUOTED=$(jq --arg v "$DB_USERNAME" -n '$v')

# Run MongoDB commands
mongosh -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD_QUOTED" admin <<EOF
    use $MONGO_INITDB_DATABASE;
    db.createUser({
        user: $DB_USERNAME_QUOTED,
        pwd: $DB_PASSWORD_QUOTED,
        roles: ["readWrite"],
    });
EOF
