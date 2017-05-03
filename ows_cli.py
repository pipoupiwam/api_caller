#!/usr/bin/env python
import argcomplete
import os, sys, argparse
from api_caller import call_api
from xml.etree import cElementTree
import xmltodict, json
from ConfigParser import ConfigParser
from action_choices import get_ows_action_choices
from argcomplete.completers import ChoicesCompleter


def call(service, call_arg):
    endpoint = os.environ.get('{}_ENDPOINT'.format(service.upper()))
    status_code, call_response = call_api('GET', endpoint, call_arg)
    response = xmltodict.parse(call_response)
    return status_code, response


def help():
    conf=ConfigParser()
    conf.read('ows.cfg')


    print '''
Expected arguments are:\n
--service  fcu | lbu | eim | osu...
--action ExpectedAction, use tab to autocomplete if autocomplete activated.

Options: #OptionKey=OptionValue'''
    print
    sys.exit(1)




if __name__ == '__main__':
    choices = get_ows_action_choices()
    parser  =  argparse.ArgumentParser() 
    parser.add_argument('--service', required=True).completer = ChoicesCompleter(['fcu', 'lbu', 'eim', 'osu'])  
    parser.add_argument( '--action', required=True).completer = ChoicesCompleter(choices)
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    action =  args.action
    service = args.service

    try:
        arg_list = []
        for arg in sys.argv[4:]:
            if arg.startswith('#'):
                arg_list.append(arg[1:])
        print arg_list
        parsed_string = '&'.join(arg_list)
        print parsed_string
        # Action=MyAction&param1=value1&param2=value2&tags.keyn=valuen&tags.keym=valuem
        status_code, response = call(service, parsed_string)
    except Exception as e:
        print e
        help()

    print "\nCode: {}".format(status_code)
    print json.dumps(response)
