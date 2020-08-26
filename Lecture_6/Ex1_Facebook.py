from facebook_scraper import get_posts

for post in get_posts('thairath', pages=50) :
    Ntext = post['text'][:100]
    if ('โควิด19' in Ntext) :
        print(Ntext)
        print('Likes :', post['likes'])
        print('Post :', post['post_url'])
        print('link :', post['link'])
        print('------')