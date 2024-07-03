from ratelimit import limits
import requests


class TVMazeInfoFetcher:

    LIMIT_TIME_PERIOD = 60  # time period in seconds
    BASE_URL = "https://api.tvmaze.com/"


    @staticmethod
    @limits(calls=15, period=LIMIT_TIME_PERIOD)
    def fetch_episode_info(show_id):

        url = f"{TVMazeInfoFetcher.BASE_URL}shows/{show_id}/episodes"
        print(url)

        try:
            response = requests.get(url)
            return response.json()

        except Exception as e:
            print(f"API end call failed:{e}")


# print(TVMazeInfoFetcher.fetch_episode_info('52339'))




