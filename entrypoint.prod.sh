!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

# // {
#         //     "name": "nginx",
#         //     "image": "nginx:latest",
#         //     "hostname": "nginx",
#         //     "essential": true,
#         //     "portMappings": [
#         //         {
#         //             "hostPort": 80,
#         //             "containerPort": 80
#         //         }
#         //     ],
#         //     "links": ["api"],
#         //     "memory": 128,
#         //     "command": [
#         //         "tail",
#         //         "-f",
#         //         "/bin/bash"
#         //     ]
#         // }