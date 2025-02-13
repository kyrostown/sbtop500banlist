import requests
import re
import json

def extract_rules(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text

    rules = {}

    for line in content.splitlines():
        if line.startswith('DOMAIN-KEYWORD'):
            keyword = line.split(',')[1].strip()
            if 'domain_keyword' not in rules:
                rules['domain_keyword'] = []
            rules['domain_keyword'].append(keyword)
        elif line.startswith('DOMAIN-SUFFIX'):
            match = re.search(r'DOMAIN-SUFFIX,([^,]+),', line)
            if match:
                domain = match.group(1).strip()
                if 'domain_suffix' not in rules:
                    rules['domain_suffix'] = []
                rules['domain_suffix'].append(domain)
        elif line.startswith('IP-CIDR'):
            ip = line.split(',')[1].strip()
            if 'ip_cidr' not in rules:
                rules['ip_cidr'] = []
            rules['ip_cidr'].append(ip)

    rules_list = []
    for rule_type, rule_values in rules.items():
        rules_list.append({rule_type: rule_values})
    return rules_list


def write_to_json(rules, filename):
    rule_set = {'version': 1, 'rules': rules}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(rule_set, f, indent=2, separators=(',', ': '))

if __name__ == '__main__':
    url = 'https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist.conf'
    rules = extract_rules(url)
    write_to_json(rules, 'sbautorule.json')

    print(f'規則已提取並儲存到 sbautorule.json 檔案中。')
