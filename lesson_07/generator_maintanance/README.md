Menu structure:

# 1. Add new generator
#   1.1 Name -> Generator in room 230
#   1.2 Description -> Brief Description
#   1.3 Model -> GS-305
#   1.4 Change oil period (in hours)
#
# 2. List generators
#   shows us all our generators -> int
#   2.1 Status
#   2.2 History
#
# 3. Start
#   3.1 *Shows us generator list -> int
#
# 4. Stop
#   4.1 Shows us generator list in status "Working" -> int
#
# 5. Exit

Generator object structure:
```json
{
  "id": "<int: generator-id>",
  "name": "<str: generator-name>",
  "description": "<str: generator-description>",
  "model": "<str: generator-model>",
  "change_oil_period": "<int: hours>",
  "motohours": "<float: hours>",
  "state": "<int: 0/1>",
  "session": {
    "start": "<int: unix-time>",
    "stop": "<int: unix-time>"
  },
  "oil": "<str: unicode-emoji>"
}
```