# sbtop500banlist
Johnshall/Shadowrocket-ADBlock-Rules-Forever. This is a very good rule.
So I did a remote config to automatically generate sing-box verson1 rules.
GFW rule
Automatically generated every day at 9:00 Taipei time
LINK: https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json

Example sing-box client configuration:
    "rule_set": [
      {
        "type": "remote",
        "tag": "sbrule",
        "format": "source",
        "url": "[https://op.tomyi.link/point/rule/sbautorule.json](https://raw.githubusercontent.com/kyrostown/sbtop500banlist/refs/heads/main/sbautorule.json)"
      },
***
***
***
    "final": "direct",
    "find_process": true,
    "auto_detect_interface": true
  }
