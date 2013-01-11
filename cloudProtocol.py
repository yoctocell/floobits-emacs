import floobitsLineReceiver


class CloudProtocol(floobitsLineReceiver.FloobitsLineReceiver):
    """Talks to the cloud"""

    def __init__(self, connectDefered, agent):
        floobitsLineReceiver.FloobitsLineReceiver.__init__(self, agent)
        self.connectDefered = connectDefered

    def dispatch(self, event):
        return getattr(self.agent, "cloud_{event}".format(event=event), None)

    def connectionMade(self):
        print('connected to server')
        self.connectDefered.callback()
        self.connectDefered = None

    def connectionLost(self, reason):
        self.agent.onConnectionLost(reason)
        print('connection to server lost', reason)
