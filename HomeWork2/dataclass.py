from dataclasses import dataclass
from datetime import datetime,timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]
    day: int = 1
    day_next: int = 1
    def schedule(self) -> Generator[datetime, None, None]:
        for data,date_two in self.dates[0],self.dates[1]:
            while data < date_two:
                data = datetime(2020,1,self.day)
                yield data
                self.day += 1
            break
        for data_three,data_four in self.dates[0],self.dates[1]:
            while datetime(2020,1,self.day_next) < data_three:
                    self.day_next += 1
            while data_three < data_four:
                data_three = datetime(2020,1,self.day_next)
                yield data_three
                self.day_next += 1
                if self.day_next == 31:
                    self.day_next = 1
                    for data_three,data_four in self.dates[0],self.dates[1]:
                        while data_three < data_four:
                            data_three = datetime(2020,2,self.day_next)
                            yield data_three
                            self.day_next += 1
                                

                    
m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
 
