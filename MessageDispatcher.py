from CURLMessage import CURLMessage
from ServiceExceptions import DispatcherFailed
import pycurl
import cStringIO
from Config import Config
import time


class MessageDispatcher:
    def dispatch(self, curlMsg):
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(c.URL, curlMsg.getPath())
        c.setopt(c.HTTPPOST, [('data',curlMsg.getBody())])
        #c.setopt(c.VERBOSE, True)
        c.setopt(c.FAILONERROR, True)

        try:
            c.perform()
        except pycurl.error, msg:
            raise DispatcherFailed(msg)
        finally:
            print buf.getvalue() #TODO: log value in buffer
            c.close()
