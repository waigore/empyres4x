import logging
from pubsub import pub
from .topic import *

logger = logging.getLogger(__name__)

def publish(topic, **kwargs):
    pub.sendMessage(topic, **kwargs)

def eventGamePhaseEnter(name, phase, turn):
    publish(GamePhaseTopics.PhaseEnter, name = name, phase = phase, turn = turn)

def eventGamePhaseExit(name, phase, turn):
    publish(GamePhaseTopics.PhaseExit, name = name, phase = phase, turn = turn)

def eventGameSetupDone():
    publish(GameSetupTopics.GameSetupDone)

def eventGameSetupPlayersCreated():
    publish(GameSetupTopics.PlayersCreated)

def subscribe(func, topic):
    pub.subscribe(func, topic)

def logEvent(topic=pub.AUTO_TOPIC, *args):
    logger.debug('Event: {} args: {}'.format(topic.getName(), args))

subscribe(logEvent, 'Game')
