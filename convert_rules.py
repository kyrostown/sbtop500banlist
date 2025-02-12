import requests
import re
import json

def extract_rules(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text

    rules = []

    for line in content.splitlines():
        if line.startswith('DOMAIN-KEYWORD'):
            keyword = line.split(',')[1].strip()
            rules.append({'domain': [keyword]})
        elif line.startswith('DOMAIN-SUFFIX'):
            match = re.search(r'DOMAIN-SUFFIX,([^,]+),', line)
            if match:
                domain = match.group(1).strip()
                rules.append({'domain_suffix': [domain]})
        elif line.startswith('IP-CIDR'):
            ip = line.split(',')[1].strip()
            rules.append({'ip_cidr': [ip]})

    return rules

def write_to_json(rules, filename):
    rule_set = {'version': 1, 'rules': rules}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(rule_set, f, indent=2)  # 使用 indent=2 使 JSON 格式更美观

if __name__ == '__main__':
    url = 'https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist.conf'
    rules = extract_rules(url)
    write_to_json(rules, 'sbrule.conf')

    print(f'规则已提取并保存到 sbrule.conf 文件中。')
