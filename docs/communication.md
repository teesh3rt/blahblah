# Communication in BlahBlah

A typical conversation between a BlahBlah system (server) and a BlahBlah service (client) goes like this:

```
> {"what": "system", "content": "bb"}
< {"what": "service", "content": "bbok"}
> {"what": "system", "content": "bbidentification"}
< {"what": "service", "service": "an example bb service"}
> {"what": "system", "content": "bbready"}
< {"what": "service", "content": "the service can now send messages", "user": "a user", "channel": "main"}
> {"what": "system", "content": "gotmessage", "using": "an example bb service", "from": "a user", "message": "the service can now send messages", "channel": "main"}
< {"what": "service", "content": "to any channel from any username", "user": "another user", "channel": "other"}
> {"what": "system", "content": "gotmessage", "using": "an example bb service", "from": "another user", "message": "to any channel from any username", "channel": "other"}
```