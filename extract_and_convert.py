import requests
import re
import yaml

def extract_rules(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text

    rules = []

    for line in content.splitlines():
        if line.startswith('DOMAIN-KEYWORD'):
            keyword = line.split(',')[1].strip()
            rules.append({'type': 'domain_keyword', 'value': keyword, 'action': 'block'})
        elif line.startswith('DOMAIN-SUFFIX'):
            match = re.search(r'DOMAIN-SUFFIX,([^,]+),', line)
            if match:
                domain = match.group(1).strip()
                rules.append({'type': 'domain_suffix', 'value': domain, 'action': 'block'})
        elif line.startswith('IP-CIDR'):
            ip = line.split(',')[1].strip()
            rules.append({'type': 'ip_cidr', 'value': ip, 'action': 'block'})

    return rules

def write_to_yaml(rules, filename):
    rule_set = {'version': 3, 'rules': rules}
    with open(filename, 'w', encoding='utf-8') as f:
        yaml.dump(rule_set, f, sort_keys=False)

if __name__ == '__main__':
    url = 'https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist.conf'
    rules = extract_rules(url)
    write_to_yaml(rules, 'singbox_rules.yaml')

    print(f'规则已提取并保存到 singbox_rules.yaml 文件中。')
