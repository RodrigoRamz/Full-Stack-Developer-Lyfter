import os
import redis


class CacheManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            password=os.getenv("REDIS_PASSWORD"),
        )

    def get_data(self, key):
        try:
            value = self.redis_client.get(key)

            if value is None:
                return None

            return value.decode("utf-8")

        except redis.RedisError as error:
            print(f"Error getting cache data: {error}")
            return None

    def store_data(self, key, value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key, value)
            else:
                self.redis_client.setex(key, time_to_live, value)

            return True

        except redis.RedisError as error:
            print(f"Error storing cache data: {error}")
            return False

    def delete_data(self, key):
        try:
            return self.redis_client.delete(key) == 1

        except redis.RedisError as error:
            print(f"Error deleting cache data: {error}")
            return False


cache_manager = CacheManager()