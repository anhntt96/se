import time
import redis

from redis import Redis

conn = redis.Redis()

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
ARTICLES_PER_PAGE = 25

def post_article(conn: Redis, user, title, link):
    article_id = str(conn.incr('article:'))

    voted = 'voted:' + article_id

    # Add author to vote
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:' + article_id
    # Add article to hash
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1
    })

    # Add to score, using to get articles, order by score or time
    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)


def article_vote(conn: Redis, user, article: str):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS
    # Check if the article can be voted
    if cutoff > conn.zscore("time:", article):
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('scores:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)

def get_articles(conn: Redis, page, order='score:'):
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    ids = conn.zremrange(order, start, end)

    articles = []

    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles

def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    article = 'article:' + article_id
    for group in to_add:
        conn.sadd('group:' + group, article)
    
    for group in to_remove:
        conn.srem('group:' + group, article)