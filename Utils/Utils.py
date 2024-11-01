import os
import re
import asyncio
from Config.Configs import BConfigs
from functools import wraps, partial
config = BConfigs()


class Utils:
    @classmethod
    def format_time(cls, duration) -> str:
        if not duration:
            return "00:00"

        hours = duration // 60 // 60
        minutes = duration // 60 % 60
        seconds = duration % 60

        return "{}{}{:02d}:{:02d}".format(
            hours if hours else "",
            ":" if hours else "",
            minutes,
            seconds)

    @classmethod
    def check_if_banned(cls, user, path) -> bool:
        banned_ids = []
        os.chdir(path)
        with open("./banlist.txt", "r") as file:
            for line in file:
                try:
                    banned_ids.append(int(line))
                except ValueError:
                    print("something went past the checker in the ban command, and a character is in here")
                    return
        return True if user in banned_ids else False

    @classmethod
    def convert_to_s(cls, time: str):
        units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        time_value = int(time[:-1])
        time_unit = time[-1]

        if time_unit in units:
            return time_value * units[time_unit]
        else:
            return None

    @classmethod
    def seconds_until(cls, time_str: str):
        try:
            if ':' in time_str:
                time_array = time_str.split(':')
            else:
                return False
            time_int: int = 0
            for i in range(len(time_array)):
                time_array[i] = int(time_array[i])
                time_int += time_array[i] * 3600 / (60 ** i)
            time_int = int(time_int)
        except ValueError:
            return False
        now = datetime.now()
        now_h, now_m, now_s = now.hour, now.minute, now.second
        now_seconds = now_h * 3600 + now_m * 60 + now_s
        try:
            time_int = (time_int - now_seconds) % 86400
        except ValueError:
            return False
        time = f"{time_int}s"
        return time

    @classmethod
    def is_url(cls, string) -> bool:
        regex = re.compile(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

        if re.search(regex, string):
            return True
        else:
            return False


def run_async(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        partial_func = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, partial_func)
    return run
