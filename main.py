from restart_docker_containers_command import RestartDockerContainersCommand
from scheduler import set_schedule_at_every_hour

command = RestartDockerContainersCommand()
hour = 4 #4 ночи
set_schedule_at_every_hour(command, hour)