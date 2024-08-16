# A1 Mediator
references:
* https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-a1/en/latest/


## Installation
### Kubernetes Deployment
The official Helm chart for the A1 Mediator is in a deployment repository, which holds all of the Helm charts for the RIC platform. There is a helm chart in integration_tests here for running the integration tests as discussed above.

### Local Deployment
#### Build the Image
```bash
docker build --no-cache -t a1:latest .
```
```bash
root@node1:~# docker build --no-cache -t a1:latest .
[+] Building 10.3s (10/10) FINISHED                                                                                                                                                            docker:default
 => [internal] load .dockerignore                                                                                                                                                                        0.1s
 => => transferring context: 2B                                                                                                                                                                          0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                     0.1s
 => => transferring dockerfile: 149B                                                                                                                                                                     0.1s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                                                       2.1s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                            0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:a6c12ec09f13df9d4b8b4e4d08678c1b212d89885be14b6c72b633bee2a520f4                                                                                 0.0s
 => [internal] load build context                                                                                                                                                                        0.0s
 => => transferring context: 28B                                                                                                                                                                         0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                                                            0.0s
 => [3/4] COPY app.py .                                                                                                                                                                                  0.0s
 => [4/4] RUN pip install Flask                                                                                                                                                                          7.7s
 => exporting to image                                                                                                                                                                                   0.2s
 => => exporting layers                                                                                                                                                                                  0.2s
 => => writing image sha256:17518dbeed863be3e702c71983b42cfa26c7d7d2ed40206c8e131a4d7ca24c1a                                                                                                             0.0s
 => => naming to docker.io/library/a1:latest                                                                                                                                                             0.0s
```
#### Start the Container
The A1 container depends on a companion DBaaS (SDL) container, but if that is not convenient set an environment variable as shown below to mock that service. Also a sample RMR routing table is supplied in file local.rt for mounting as a volume. The following command uses both:
```bash
docker run -e USE_FAKE_SDL=True -p 10000:10000 -v /path/to/local.rt:/opt/route/local.rt a1:latest
```
output:
```bash
root@node1:~# docker run -e USE_FAKE_SDL=True -p 10000:10000 -v /path/to/local.rt:/opt/route/local.rt a1:latest
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
```

#### Check container health
The following command requests the container health. Expect an internal server error if the Storage Data Layer (SDL) service is not available or has not been mocked as shown above.
```bash
curl <docker-host-name-or-ip>:10000/A1-P/v2/healthcheck
```

## User Guide and APIs
How to communicate with the A1 Mediator.

### Example Message
Send the following JSON to create policy type 20008, which supports instances with a single integer value:
```jsonld
{
  "name": "tsapolicy",
  "description": "tsa parameters",
  "policy_type_id": 20008,
  "create_schema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "threshold": {
        "type": "integer",
        "default": 0
      }
    },
    "additionalProperties": false
  }
}
```
For example, if you put the JSON above into a file called “create.json” you can use the curl command-line tool to send the request:
```bash
curl -X PUT –header “Content-Type: application/json” –data-raw @create.json “http://192.168.0.237:30091/A1-P/v2/policytypes/20008”
```
Send the following JSON to create an instance of policy type 20008:
```jsonld
{
  "threshold" : 5
}
```
```bash
curl -X PUT –header “Content-Type: application/json” –data ‘{“threshold” : 5}’ “http://localhost/A1-P/v2/policytypes/20008/policies/tsapolicy145”
```

### Integrating Xapps with A1
The schema for messages sent by A1 to Xapps is labeled `downstream_message_schema` in the Southbound API Specification section below. A1 sends policy instance requests using message type 20010.

The schemas for messages sent by Xapps to A1 appear in the Southbound API Specification section below. Xapps must use a message type and content appropriate for the scenario:
1. When an xApp receives a CREATE message for a policy instance, the Xapp must respond by sending a message of type 20011 to A1. The content is defined by schema `downstream_notification_schema`. The most convenient way is to use RMR’s return-to-sender (RTS) feature after setting the message type appropriately.
2. Since policy instances can “deprecate” other instances, there are times when Xapps need to asynchronously tell A1 that a policy is no longer active. Use the same message type and schema as above.
3. xApps can request A1 to re-send all instances of policy type T using a query, message type 20012. The schema for that message is defined by `policy_query_schema` (just a body with `{policy_type_id: ... }`). When A1 receives this, A1 will send the Xapp a CREATE message N times, where N is the number of policy instances for type T. The Xapp should reply normally to each of those as the first item above. That is, after the xApp performs the query, the N CREATE messages sent and the N replies are “as normal”. The query just kicks off this process rather than an external caller to A1.

### Northbound API Specification
This section shows the Open API specification for the A1 Mediator’s northbound interface, which accepts policy type and policy instance requests. Following are the api and the response:
```bash
curl -v -X GET "http://localhost/A1-P/v2/healthcheck"
```
```bash
< HTTP/1.1 200 OK
```
#### 1. Get all policy types
```bash
curl -X GET "http://localhost/A1-P/v2/policytypes/"
```
```bash
[20001,5003,21001,21000,21002]
```
#### 2. Get Policy Type based on policyid
```bash
curl -s -X GET "http://localhost/A1-P/v2/policytypes/20001" | jq .
```
```bash
{
  "create_schema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
      "additionalProperties": false,
      "blocking_rate": {
        "default": 10,
        "description": "% Connections to block",
        "maximum": 1001,
        "minimum": 1,
        "type": "number"
      },
      "enforce": {
        "default": "true",
        "type": "boolean"
      },
      "window_length": {
        "default": 1,
        "description": "Sliding window length (in minutes)",
        "maximum": 60,
        "minimum": 1,
        "type": "integer"
      }
    },
    "type": "object"
  },
  "description": "various parameters to control admission of dual connection",
  "name": "admission_control_policy_mine",
  "policy_type_id": 20001
}
```
#### 3. Get all policy instances for a given policy type
```bash
curl -s -X GET "http://localhost/A1-P/v2/policytypes/20001/policies/" | jq .
```
```bash
[
  "1234",
  "1235"
]
```
#### 4. Get policy instance for a policy id and policy instance id
```bash
curl -s -X GET "http://localhost/A1-P/v2/policytypes/20001/policies/1234" | jq .
```
```bash
{
  "blocking_rate": 20,
  "enforce": true,
  "trigger_threshold": 20,
  "window_length": 20
}
```
#### 5. Create Policy type
```bash
curl -X PUT "http://localhost/A1-P/v2/policytypes/21003/" -H "Content-Type: application/json" -d @policy_schema_ratecontrol.json

cat policy_schema_ratecontrol.json
```
```bash
{
"name": "Policy for Rate Control",
  "policy_type_id":21003,
  "description":"This policy is associated with rate control. Entities which support this policy type must accept the following policy inputs (see the payload for more specifics) : class, which represents the class of traffic for which the policy is being enforced",

  "create_schema":{
      "$schema":"http://json-schema.org/draft-07/schema#",
      "type":"object",
      "additionalProperties":false,
      "required":["class"],
      "properties":{
          "class":{
              "type":"integer",
              "minimum":1,
              "maximum":256,
              "description":"integer id representing class to which we are applying policy"
          },
          "enforce":{
              "type":"boolean",
              "description": "Whether to enable or disable enforcement of policy on this class"
          },
          "window_length":{
              "type":"integer",
              "minimum":15,
              "maximum":300,
              "description":"Sliding window length in seconds"
          },
          "trigger_threshold":{
              "type":"integer",
              "minimum":1
          },
          "blocking_rate":{
              "type":"number",
              "minimum":0,
              "maximum":100
          }

      }
  },

  "downstream_schema":{
      "type":"object",
      "additionalProperties":false,
      "required":["policy_type_id", "policy_instance_id", "operation"],
      "properties":{
          "policy_type_id":{
              "type":"integer",
              "enum":[21000]
          },
          "policy_instance_id":{
              "type":"string"
          },
          "operation":{
              "type":"string",
              "enum":["CREATE", "UPDATE", "DELETE"]
          },
          "payload":{
              "$schema":"http://json-schema.org/draft-07/schema#",
              "type":"object",
              "additionalProperties":false,
              "required":["class"],
              "properties":{
                  "class":{
                      "type":"integer",
                      "minimum":1,
                      "maximum":256,
                      "description":"integer id representing class to which we are applying policy"
                  },
                  "enforce":{
                      "type":"boolean",
                      "description": "Whether to enable or disable enforcement of policy on this class"
                  },
                  "window_length":{
                      "type":"integer",
                      "minimum":15,
                      "maximum":300,
                      "description":"Sliding window length in seconds"
                  },
                  "trigger_threshold":{
                      "type":"integer",
                      "minimum":1
                  },
                  "blocking_rate":{
                      "type":"number",
                      "minimum":0,
                      "maximum":100
                  }


              }
          }
      }
  },
  "notify_schema":{
      "type":"object",
      "additionalProperties":false,
      "required":["policy_type_id", "policy_instance_id", "handler_id", "status"],
      "properties":{
          "policy_type_id":{
              "type":"integer",
              "enum":[21000]
          },
          "policy_instance_id":{
              "type":"string"
          },
          "handler_id":{
              "type":"string"
          },
          "status":{
              "type":"string",
              "enum":["OK", "ERROR", "DELETED"]
          }
      }
  }
}
```
#### 6. Create policy instance
```bash
curl -X PUT "http://localhost/A1-P/v2/policytypes/21003/policies/1234" -H "Content-Type: application/json" -d @policy_instance_ratecontrol.json

cat policy_instance_ratecontrol.json
```
```jsonld
{
    "class":12,
    "enforce":true,
    "window_length":20,
    "blocking_rate":20,
    "trigger_threshold":10
}
```
#### 7. Get policy instance status:
```bash
curl -s -X GET "http://localhost/A1-P/v2/policytypes/21004/policies/1235/status" | jq .
```
```jsonld
{
  "created_at": "0001-01-01T00:00:00.000Z",
  "instance_status": "IN EFFECT"
}
```
#### 8. Delete policy type
```bash
curl -s -X DELETE "http://localhost/A1-P/v2/policytypes/21004/"
```

#### 9. Delete policy instance
```bash
curl -s -X DELETE "http://localhost/A1-P/v2/policytypes/21004/policies/1234/"
```

#### 10. A1-EI data delivery for a job id:
```bash
curl -X POST "http://localhost/data-delivery" -H "Content-Type: application/json" -d @a1eidata.json

cat a1eidata.json
```

```jsonld
{
    "job":"100",
    "payload":"payload"
}
```

### Southbound API Specification
This section shows Open API schemas for the A1 Mediator’s southbound interface, which communicates with xApps via RMR. A1 sends policy instance requests using message type 20010. xApps may send requests to A1 using message types 20011 and 20012.
```bash
openapi: 3.0.0
info:
  version: 1.0.0
  title: Contract between A1 and RIC Xapps

components:
  schemas:

    policy_type_id:
      description: >
        represents a policy type identifier. Currently this is restricted to an integer range.
      type: integer
      minimum: 1
      maximum: 2147483647

    policy_instance_id:
      description: >
        represents a policy instance identifier. UUIDs are advisable but can be any string
      type: string
      example: "3d2157af-6a8f-4a7c-810f-38c2f824bf12"

    policy_query_schema:
      type: object
      required:
        - policy_type_id
      additionalProperties: false
      properties:
        policy_type_id:
          "$ref": "#/components/schemas/policy_type_id"

    downstream_message_schema:
      type: object
      required:
        - operation
        - policy_type_id
        - policy_instance_id
        - payload
      additionalProperties: false
      properties:
        operation:
          description: the operation being performed
          type: string
          enum:
            - CREATE
            - DELETE
            - UPDATE
        policy_type_id:
          "$ref": "#/components/schemas/policy_type_id"
        policy_instance_id:
          "$ref": "#/components/schemas/policy_instance_id"
        payload:
          description: payload for this operation
          type: object
      example:
        operation: CREATE
        policy_type_id: 12345678
        policy_instance_id: 3d2157af-6a8f-4a7c-810f-38c2f824bf12
        payload:
          enforce: true
          window_length: 10
          blocking_rate: 20
          trigger_threshold: 10

    downstream_notification_schema:
      type: object
      required:
        - policy_type_id
        - policy_instance_id
        - handler_id
        - status
      additionalProperties: false
      properties:
        policy_type_id:
          "$ref": "#/components/schemas/policy_type_id"
        policy_instance_id:
          "$ref": "#/components/schemas/policy_instance_id"
        handler_id:
          description: >
            id of the policy handler
          type: string
        status:
          description: >
            the status of this policy instance in this handler
          type: string
          enum:
            - OK
            - ERROR
            - DELETED
      example:
        policy_type_id: 12345678
        policy_instance_id: 3d2157af-6a8f-4a7c-810f-38c2f824bf12
        handler_id: 1234-5678
        status: OK
```