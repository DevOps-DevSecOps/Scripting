# """ Regular Expression """ #

import re
patterns = ['Hi', 'ATK']
text = 'Hi it is ATK'
for content in patterns:
    print('Searching for "%s" in : \n "%s"' %(content, text))

    if re.search(content, text):
        print('Match was found.')
    else:
        print('No match was found.')
