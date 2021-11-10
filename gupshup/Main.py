class Client:
    clientID = None
    messageQueue = []
    clientTps = None
    msgsLeft = None
    overflowMsgs = None


clients = []


def init(totalTps, noClients, clientTps):
    spare_tps = (totalTps - sum(clientTps)) / noClients
    for i in range(noClients):
        temp = Client()
        temp.clientTps = clientTps[i] + spare_tps
        temp.clientID = i
        clients.append(temp)


def reset():
    for i in clients:
        i.msgsLeft = 0.0
        i.overflowMsgs = 0.0


def tick():
    for i in clients:
        i.msgsLeft += (i.clientTps / 10)
        if i.msgsLeft > i.clientTps:
            i.msgsLeft = i.clientTps


def msgReceived(clientID, messageID):
    clients[clientID].messageQueue = clients[clientID].messageQueue + [messageID]
    if clients[clientID].msgsLeft <= clients[clientID].clientTps:
        clients[clientID].msgsLeft += 1
    else:
        clients[clientID].overflowMsgs += 1


def sendMsg():
    cp = [0] * len(clients)

    # HIGHER MSGS LEFT

    max_msg_left = [-99999999999]
    max_msg_left_index = [-1]
    for i, j in enumerate(clients):
        if max_msg_left[0] < j.msgsLeft:
            max_msg_left = [j.msgsLeft]
            max_msg_left_index = [i]

        elif max_msg_left[0] == j.msgsLeft:
            max_msg_left = max_msg_left + [j.msgsLeft]
            max_msg_left_index = max_msg_left_index + [i]

    if not clients[max_msg_left_index[0]].messageQueue:
        print(-1)
        return
    if len(max_msg_left_index) == 1:
        print(clients[max_msg_left_index[0]].messageQueue.pop(0))
        clients[max_msg_left_index[0]].msgsLeft -= 1
        return

    # priority update

    for i in max_msg_left_index:
        cp[clients[i].clientID] += 1

    # HIGHER TPS

    max_tps = [-99999999999]
    max_tps_index = [-1]
    for i, j in enumerate(clients):
        if i in max_msg_left_index:
            if max_tps[0] < j.clientTps:
                max_tps = [j.clientTps]
                max_tps_index = [i]

            elif max_tps[0] == j.clientTps:
                max_tps = max_tps + list(j.clientTps)
                max_tps_index = max_tps_index + [i]
    if not clients[max_tps_index[0]].messageQueue:
        print(-1)
        return

    if len(max_tps_index) == 1:
        print(clients[max_tps_index[0]].messageQueue.pop(0))
        clients[max_tps_index[0]].msgsLeft -= 1
        return

    # priority update

    for i in max_tps_index:
        cp[clients[i].clientID] += 1

    flag = False
    for i in cp:
        if i != 0:
            flag = True

    if flag:
        if not clients[max(cp)].messageQueue:
            print(-1)
            return
        else:
            print(clients[max(cp)].messageQueue.pop(0))
            clients[max(cp)].msgsLeft -= 1

    # checks for overflow

    if not flag:
        min_overflow = [99999999999]
        min_overflow_index = [-1]
        for i, j in enumerate(clients):
            if min_overflow[0] > j.overflowMsgs:
                min_overflow = [j.overflowMsgs]
                min_overflow_index = [i]

            elif min_overflow[0] == j.overflowMsgs:
                min_overflow = min_overflow + list(j.overflowMsgs)
                min_overflow_index = min_overflow_index + [i]

        flag = False
        for i in min_overflow:
            if i != 0:
                flag = True

        if not flag:
            print(-1)
            return
        else:
            if not clients[min_overflow_index[0]].messageQueue:
                print(-1)
                return
            else:
                print(clients[min_overflow_index[0]].messageQueue.pop(0))
                clients[min_overflow_index[0]].overflowMsgs += 1
                return


if __name__ == "__main__":
    flag = True
    while flag:
        temp = list(input().split())
        if temp[0] == "end":
            flag = False
        elif temp[0] == "init":
            init(int(temp[1]), int(temp[2]), list(map(int, temp[3].split(","))))
        elif temp[0] == "reset":
            reset()
        elif temp[0] == "msgReceived":
            msgReceived(int(temp[1]), int(temp[2]))
        elif temp[0] == "tick":
            tick()
        elif temp[0] == "sendMsg":
            sendMsg()