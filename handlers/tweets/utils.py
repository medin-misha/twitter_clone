from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Result, update, select
from sqlalchemy.orm import selectinload, joinedload
from typing import List
from core import Image, Tweet, User
from handlers import get_by_id


async def image_to_tweet(
    session: AsyncSession, tweet_id: int, images_ids: List[int]
) -> None:
    print(images_ids)
    stmt = (
        update(Image.__table__)
        .where(Image.id.in_(images_ids))
        .values(tweet_id=tweet_id)
    )
    await session.execute(stmt)
    await session.commit()


async def get_tweets(session: AsyncSession):
    stmt = select(Tweet).options(selectinload("*")).order_by(Tweet.content)
    select_result: Result = await session.execute(stmt)
    tweets = []
    for tweet in select_result.scalars().all():
        tweet_data: dict = {
            "id": tweet.id,
            "content": tweet.content,
            "attachments": [image.filename for image in tweet.attachments],
            "author": {
                "id": tweet.autor.id,
                "name": tweet.autor.name,
            },
        }
        tweets.append(tweet_data)

    return tweets
