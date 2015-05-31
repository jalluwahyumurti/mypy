# Stubs for logging.handlers (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import logging

threading = ...  # type: Any
DEFAULT_TCP_LOGGING_PORT = ...  # type: Any
DEFAULT_UDP_LOGGING_PORT = ...  # type: Any
DEFAULT_HTTP_LOGGING_PORT = ...  # type: Any
DEFAULT_SOAP_LOGGING_PORT = ...  # type: Any
SYSLOG_UDP_PORT = ...  # type: Any
SYSLOG_TCP_PORT = ...  # type: Any

class BaseRotatingHandler(logging.FileHandler):
    mode = ...  # type: Any
    encoding = ...  # type: Any
    namer = ...  # type: Any
    rotator = ...  # type: Any
    def __init__(self, filename, mode, encoding=None, delay=False): pass
    def emit(self, record): pass
    def rotation_filename(self, default_name): pass
    def rotate(self, source, dest): pass

class RotatingFileHandler(BaseRotatingHandler):
    maxBytes = ...  # type: Any
    backupCount = ...  # type: Any
    def __init__(self, filename, mode='', maxBytes=0, backupCount=0, encoding=None,
                 delay=False): pass
    stream = ...  # type: Any
    def doRollover(self): pass
    def shouldRollover(self, record): pass

class TimedRotatingFileHandler(BaseRotatingHandler):
    when = ...  # type: Any
    backupCount = ...  # type: Any
    utc = ...  # type: Any
    atTime = ...  # type: Any
    interval = ...  # type: Any
    suffix = ...  # type: Any
    extMatch = ...  # type: Any
    dayOfWeek = ...  # type: Any
    rolloverAt = ...  # type: Any
    def __init__(self, filename, when='', interval=1, backupCount=0, encoding=None, delay=False,
                 utc=False, atTime=None): pass
    def computeRollover(self, currentTime): pass
    def shouldRollover(self, record): pass
    def getFilesToDelete(self): pass
    stream = ...  # type: Any
    def doRollover(self): pass

class WatchedFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='', encoding=None, delay=False): pass
    stream = ...  # type: Any
    def emit(self, record): pass

class SocketHandler(logging.Handler):
    host = ...  # type: Any
    port = ...  # type: Any
    address = ...  # type: Any
    sock = ...  # type: Any
    closeOnError = ...  # type: Any
    retryTime = ...  # type: Any
    retryStart = ...  # type: Any
    retryMax = ...  # type: Any
    retryFactor = ...  # type: Any
    def __init__(self, host, port): pass
    def makeSocket(self, timeout=1): pass
    retryPeriod = ...  # type: Any
    def createSocket(self): pass
    def send(self, s): pass
    def makePickle(self, record): pass
    def handleError(self, record): pass
    def emit(self, record): pass
    def close(self): pass

class DatagramHandler(SocketHandler):
    closeOnError = ...  # type: Any
    def __init__(self, host, port): pass
    def makeSocket(self, timeout=1): pass # TODO: Actually does not have the timeout argument.
    def send(self, s): pass

class SysLogHandler(logging.Handler):
    LOG_EMERG = ...  # type: Any
    LOG_ALERT = ...  # type: Any
    LOG_CRIT = ...  # type: Any
    LOG_ERR = ...  # type: Any
    LOG_WARNING = ...  # type: Any
    LOG_NOTICE = ...  # type: Any
    LOG_INFO = ...  # type: Any
    LOG_DEBUG = ...  # type: Any
    LOG_KERN = ...  # type: Any
    LOG_USER = ...  # type: Any
    LOG_MAIL = ...  # type: Any
    LOG_DAEMON = ...  # type: Any
    LOG_AUTH = ...  # type: Any
    LOG_SYSLOG = ...  # type: Any
    LOG_LPR = ...  # type: Any
    LOG_NEWS = ...  # type: Any
    LOG_UUCP = ...  # type: Any
    LOG_CRON = ...  # type: Any
    LOG_AUTHPRIV = ...  # type: Any
    LOG_FTP = ...  # type: Any
    LOG_LOCAL0 = ...  # type: Any
    LOG_LOCAL1 = ...  # type: Any
    LOG_LOCAL2 = ...  # type: Any
    LOG_LOCAL3 = ...  # type: Any
    LOG_LOCAL4 = ...  # type: Any
    LOG_LOCAL5 = ...  # type: Any
    LOG_LOCAL6 = ...  # type: Any
    LOG_LOCAL7 = ...  # type: Any
    priority_names = ...  # type: Any
    facility_names = ...  # type: Any
    priority_map = ...  # type: Any
    address = ...  # type: Any
    facility = ...  # type: Any
    socktype = ...  # type: Any
    unixsocket = ...  # type: Any
    socket = ...  # type: Any
    formatter = ...  # type: Any
    def __init__(self, address=..., facility=..., socktype=None): pass
    def encodePriority(self, facility, priority): pass
    def close(self): pass
    def mapPriority(self, levelName): pass
    ident = ...  # type: Any
    append_nul = ...  # type: Any
    def emit(self, record): pass

class SMTPHandler(logging.Handler):
    username = ...  # type: Any
    fromaddr = ...  # type: Any
    toaddrs = ...  # type: Any
    subject = ...  # type: Any
    secure = ...  # type: Any
    timeout = ...  # type: Any
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None,
                 timeout=0.0): pass
    def getSubject(self, record): pass
    def emit(self, record): pass

class NTEventLogHandler(logging.Handler):
    appname = ...  # type: Any
    dllname = ...  # type: Any
    logtype = ...  # type: Any
    deftype = ...  # type: Any
    typemap = ...  # type: Any
    def __init__(self, appname, dllname=None, logtype=''): pass
    def getMessageID(self, record): pass
    def getEventCategory(self, record): pass
    def getEventType(self, record): pass
    def emit(self, record): pass
    def close(self): pass

class HTTPHandler(logging.Handler):
    host = ...  # type: Any
    url = ...  # type: Any
    method = ...  # type: Any
    secure = ...  # type: Any
    credentials = ...  # type: Any
    def __init__(self, host, url, method='', secure=False, credentials=None): pass
    def mapLogRecord(self, record): pass
    def emit(self, record): pass

class BufferingHandler(logging.Handler):
    capacity = ...  # type: Any
    buffer = ...  # type: Any
    def __init__(self, capacity): pass
    def shouldFlush(self, record): pass
    def emit(self, record): pass
    def flush(self): pass
    def close(self): pass

class MemoryHandler(BufferingHandler):
    flushLevel = ...  # type: Any
    target = ...  # type: Any
    def __init__(self, capacity, flushLevel=..., target=None): pass
    def shouldFlush(self, record): pass
    def setTarget(self, target): pass
    buffer = ...  # type: Any
    def flush(self): pass
    def close(self): pass

class QueueHandler(logging.Handler):
    queue = ...  # type: Any
    def __init__(self, queue): pass
    def enqueue(self, record): pass
    def prepare(self, record): pass
    def emit(self, record): pass

class QueueListener:
    queue = ...  # type: Any
    handlers = ...  # type: Any
    def __init__(self, queue, *handlers): pass
    def dequeue(self, block): pass
    def start(self): pass
    def prepare(self, record): pass
    def handle(self, record): pass
    def enqueue_sentinel(self): pass
    def stop(self): pass