#!/usr/bin/env python
#
# pns.py is a simple DNS server which only allows pornagraphic material through.
#
# Bits and pieces robbed from here:
# https://gist.github.com/johnboxall/1147973
# http://twistedmatrix.com/trac/wiki/TwistedWeb
import socket
import dns.resolver as DNS
 
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server
from twisted.web import server as webserver
from twisted.web import resource
import sys
index = open('index.html').read()

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return index


class DNSServerFactory(server.DNSServerFactory):

    def gotResolverResponse(self, (ans, auth, add), protocol, message, address):
        qname = message.queries[0].name.name
        print qname
        blocked_resolver = DNS.Resolver()
        blocked_resolver.nameservers = ['208.67.222.123','208.67.220.123']


        porn = False
        results = blocked_resolver.query(qname)
        for r in results:
          print r
          if str(r).startswith('67.215.65'):
            print "PRON"
            porn = True
       
        if porn == False:
          print "NOT PRON"
          for answer in ans:
            if answer.type != dns.A:
                continue
            answer.payload.address = socket.inet_aton(ip_address)
            answer.payload.ttl = 60      
        #address = ('127.0.0.1', 43160)
        args = (self, (ans, auth, add), protocol, message, address)
        result=server.DNSServerFactory.gotResolverResponse(*args)
        print result
        return result
 
 
verbosity = 0

ip_address = ""
if len(sys.argv) > 1:
    ip_address = sys.argv[1]
else:
    ip_address = '127.0.0.1'
 
resolver = client.Resolver(servers=[('8.8.8.8', 53)])
factory = DNSServerFactory(clients=[resolver], verbose=verbosity)
protocol = dns.DNSDatagramProtocol(factory)
factory.noisy = protocol.noisy = verbosity
 
reactor.listenUDP(53, protocol)
reactor.listenTCP(53, factory)
site = webserver.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()