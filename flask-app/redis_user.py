import redis
import os


redis_client = redis.Redis(
  host='redis-11087.c91.us-east-1-3.ec2.redns.redis-cloud.com',
  port=os.getenv('REDIS_PORT'),
  password=os.getenv('REDIS_PASSWORD'))
