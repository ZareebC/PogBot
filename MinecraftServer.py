import subprocess

import mcstatus


class MinecraftServer:

    def __init__(self, ip):
        self.ip = ip


    def player_count(self):
        server = mcstatus.MinecraftServer.lookup(self.ip)
        status = server.status()
        player_count = status.players.online

        return player_count


    def player_list(self):
        command = "mcstatus {} status".format(self.ip)
        output = str(subprocess.check_output(command, shell=True))

        index = output.find("[")

        if index == -1:
            return []

        lst_string = output[index+1:-4]
        lst = lst_string.split(", ")
        players_online = [s.split(" ")[0][2:] for s in lst]

        return players_online


    def server_lookup(self):
        count = self.player_count()
        players = self.player_list()

        return (count, players)
