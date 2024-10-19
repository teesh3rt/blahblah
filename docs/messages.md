# Messages in BlahBlah

A message is a simple JSON object. it can have any fields, but there is one that is mandatory: `what`.
The BlahBlah server always communicates using the `system` type, and the service (client) is expected to communicate using the `service` type for all client-related things (setting your name, setting other things if the server supports them, etc)
