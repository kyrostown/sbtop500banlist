# sbtop500banlist

## Rule Source

*   **Johnshall/Shadowrocket-ADBlock-Rules-Forever:** This is an excellent rule list.
*   **Automatically Generated:** I've configured it remotely to automatically generate rules for sing-box v1.

## Rule Content

*   **GFW Rule**
*   **Daily Automatic Updates:** Generated daily at 9:00 AM Taipei time.

## Rule Link

*   [https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json](https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json)

## sing-box Client Configuration Example

```json
"rule_set": [
  {
    "type": "remote",
    "tag": "sbrule",
    "format": "source",
    "url": "[https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json](https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json)"
  },
  ..
  ..
]
