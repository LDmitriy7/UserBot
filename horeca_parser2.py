import re

fr = open('horeca_group_msgs', encoding='utf-8')
fp = open('horeca_group_phones', 'w', encoding='utf-8')

PHONES = set()

for line in fr:
    line = re.sub('[ ()-]', '', line)
    res = re.findall(r'0\d{9}', line)

    for i in res:
        i = '38' + i

        assert len(i) == 12 and i.startswith('380')

        PHONES.add(i)

for i in PHONES:
    print(i, file=fp)
