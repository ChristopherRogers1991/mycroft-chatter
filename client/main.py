from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from lib import send_message

def construct_arg_parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-H", "--host", help=" ", default="localhost")
    parser.add_argument("-p", "--port", help=" ", type=int, default=8181)
    parser.add_argument("-P", "--path", help=" ", default="/core")
    parser.add_argument("-s", "--scheme", help="ws or wss", default="ws")
    parser.add_argument("message", nargs="+",
                        help="The message to send to mycroft. All values "
                             "will be concatinated together into one message.")
    return parser

def main():
    parser = construct_arg_parser()
    args = parser.parse_args()
    message = ' '.join(args.message)
    send_message(message, host=args.host, port=args.port,
                 path=args.path, scheme=args.scheme)


if __name__ == "__main__":
    main()