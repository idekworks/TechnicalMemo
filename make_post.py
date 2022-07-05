import datetime
from datetime import datetime, timedelta

dt_now = datetime.now()
print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
file_name = dt_now.strftime('_posts/%Y-%m-%d-%b%d.md')
print(file_name)

yesterday = dt_now - timedelta(1)
prev_name = yesterday.strftime('https://idekworks.github.io/TechnicalMemo/%Y/%m/%d/%b%d.html')
tomorrow = dt_now + timedelta(1)
next_name = tomorrow.strftime('https://idekworks.github.io/TechnicalMemo/%Y/%m/%d/%b%d.html')

with open(file_name, 'x') as f:
    f.write('---\n') 
    title = dt_now.strftime('%b%d-memo')
    date = dt_now.strftime('%Y-%m-%d')
    f.write(f'title: {title} \n') 
    f.write(f'date: {date} \n') 
    f.write('---\n\n') 
    f.write(f'[<prev]({prev_name}) | [next>]({next_name}) \n\n')
    sl = ['# atcoder','\n\n' '# kaggle', '\n\n' '# 統計', '\n\n',
            '# python algo', '\n\n', '# dev app', '\n\n', '# other' '\n\n']
    f.writelines(sl) 
    f.write('***\n') 
    f.write(f'[<prev]({prev_name}) | [next>]({next_name})\n\n')


