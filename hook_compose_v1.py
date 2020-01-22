#!/usr/bin/env python
import os
import sys
import json
import requests
from azure.servicebus import QueueClient, Message

# config
try:
    API_HOST = os.environ['ALCOLIZER_API_HOST']
    ALCOLIZER_KEY = os.environ['ALCOLIZER_API_KEY']
    AZURE_SERVICE_BUS_CONNECTION_STRING = os.environ['AZURE_SERVICE_BUS_CONNECTION_STRING']
    AZURE_SERVICE_BUS_QUEUE = os.environ['AZURE_SERVICE_BUS_QUEUE']
except KeyError as e:
    print("ERROR: missing environment variable!")
    raise e


def get_api_response(resource_name, resource_id):
    """ get the api result object from the API server """

    url = "{api_host}/v1/result/{table_name}/{table_id}".format(api_host=API_HOST,
                                                                table_name=resource_name,
                                                                table_id=resource_id)
    headers = {'x-alcolizer-key': ALCOLIZER_KEY}
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        # need to convert utf-8 to ascii for the output to work when printed.
        # load the body with utf-8
        body = response.content.decode('utf-8')
        # return the body as ascii with xml references
        return json.loads(body.encode("ascii", "xmlcharrefreplace"))
        # return response.json()

    raise ValueError('response was not 200')


def send_message_to_queue(message):
    """ send the message to the api queue """
    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(AZURE_SERVICE_BUS_CONNECTION_STRING, AZURE_SERVICE_BUS_QUEUE)

    # Send a message to the queue
    msg = Message(message)
    response = queue_client.send(msg)
    # the response is a list of tuple pairs (sent boolean, error string)
    # so convert the response to something we can work with
    sent, errors = response[0]
    return {'message_queued': sent, 'errors': errors}


def main():
    """ main processing loop for when run directly """

    # Load the data that PHP sent us
    data = json.loads(sys.argv[1])

    # sanitise input
    try:
        table_name = data['table_name']
        table_id = data['table_id']
    except KeyError as e:
        print("table_name or table_id missing")
        raise e
    headers = data.get('headers', {})
    if not isinstance(headers, dict):
        # if headers is not an object, raise an error
        raise ValueError('headers is not a dict (key-value-pair object)')

    # fetch the json payload from the server
    api_payload = get_api_response(table_name, table_id)

    # build the job payload
    job_payload = {'id': data['hook_log_id'], 'url': data['url'], 'headers': headers, 'payload': api_payload}
    print(json.dumps(job_payload))

    # send the payload to the queue
    response = send_message_to_queue(json.dumps(job_payload))

    print(json.dumps(response))


if __name__ == "__main__":
    # if this is being run from the command line
    # run the main function
    main()
