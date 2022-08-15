import datetime as dt
from typing import Optional

 
class MyTimer(object):

    def __init__(self) -> None:
        self._start: Optional[dt.datetime] = None
        self._total: Optional[dt.timedelta] = None
        self._lap_time: Optional[dt.timedelta] = None
        self._is_running = False
    
    def start(self) -> None:
        if not self._is_running:
            self._total = None
            self._is_running = True
            self._start = dt.datetime.now()
            self._lap_time = self._start

    def stop(self) -> Optional[dt.timedelta]:
        if self._is_running:
            self._total = dt.datetime.now() - self._start
            self._start = None
            self._is_running = False
            return self._total
        return None

    def lap_time(self) -> Optional[dt.timedelta]:
        if self._is_running:
            now = dt.datetime.now()
            lap_time = now - self._lap_time
            self._lap_time = now
            return lap_time
        else:
            None

    @property
    def message(self) -> str:
        if self._is_running:
            return "Timer is running =3 =3 =3"
        else:
            return f"TotalTime: {self.total_time}"

    @property
    def total_time(self) -> dt.timedelta:
        return self._total
