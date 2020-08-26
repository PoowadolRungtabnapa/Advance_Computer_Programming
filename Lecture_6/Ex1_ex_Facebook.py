from facebook_scraper import get_posts

index = 0

for post in get_posts('FITM', pages=50) :
    Ntext = post['text'][:100]
    Mlink = post['link']
    if 'นักศึกษาแลกเปลี่ยนนานาชาติ' in Ntext :
        while index < 3 :
            index += 1 
            print(Ntext)
            print('post :', post['post_url'])
            print('link')
