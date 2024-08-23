import subprocess


class RestartDockerContainersCommand:
    def execute(self):
        ids = self.__get_containers_ids()
        command = self.__get_restart_containers_command(ids)
        try:
            subprocess.check_output(command)
        except subprocess.CalledProcessError as e:
            print(e.output)

    def __get_restart_containers_command(self, ids):
        restart_all_containers_command = ['docker', 'restart']
        for id in ids:
            restart_all_containers_command.append(id)
        return restart_all_containers_command

    def __get_containers_ids(self):
        get_containers_ids_command = ['docker', 'ps', '-q']
        all_containers_ids_string = subprocess.check_output(get_containers_ids_command).decode('utf-7')
        all_containers_ids_list = all_containers_ids_string.split("\n")
        del all_containers_ids_list[-1]
        return all_containers_ids_list