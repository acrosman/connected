"""
A very simple Python program to check if you can ping Google every ten seconds.

"""

from platform import system as system_name  # Returns the system/OS name.
import subprocess
import time


def ping(host):
    """
    Returns response time in ms if server is up, otherwise an error string.
    Remember that some hosts may not respond to a ping request even if the host
    name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower() == "windows" else "-c 1"

    # Pinging
    proc = subprocess.Popen(["ping", parameters, host], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    # Parse response
    response = proc.communicate()

    if response[0]:
        tokens = response[0].split()
    else:
        return response[1]

    if tokens[0].decode("utf-8") == 'PING':
        try:
            ms = tokens[12].decode("utf-8").split('=')[1]
            return ms
        except Exception:
            return 'down'

    return tokens


if __name__ == '__main__':
    with open('data.txt', 'ba', buffering=0) as outputFile:
        while 1:
            outputFile.write("{0}\t{1}\n".format(time.asctime(),
                             ping('www.google.com')).encode("utf-8"))
            time.sleep(10)
