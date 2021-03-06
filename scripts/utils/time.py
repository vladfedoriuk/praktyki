import re
from datetime import datetime
import sys
import logging

time_patterns_set = {
    "%Y-%m-%d", "%Y-%m-%dT%H:%M", \
        "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", \
            "%Y-%m-%dT%H:%M:%z"
}

r_time_pattern = r'[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+/-][HHMM]'
r_time_patterns = [re.sub(r'%Y', '[yyyy]', 
                          re.sub(r'%m', '[mm]', re.sub(
                             r'%d', '[dd]', re.sub(
                                 r'%H', '[HH]', re.sub(
                                    r'%M', '[MM]', re.sub(
                                        r'%S', '[SS]', re.sub(
                                            r'%z', '[+-][HHMM]', x
                                        )
                                    ) 
                                 )
                             ) 
                          )
                        )
                    )
                for x in time_patterns_set]


def validate_date(date, param_name):
    for pattern in time_patterns_set:
        try:
            valid_date = datetime.strptime(date, pattern)
            return valid_date
        except ValueError:
            pass 
    else:
        logging.error(f'No time pattern matched for {param_name}.' + \
                      'Use -h flag to see the whole pattern')
        sys.exit()
        

def convert_datetime(date_time: datetime) -> str:
    for pattern in time_patterns_set:
        try:
            str_datetime = date_time.strftime(pattern)
            return str_datetime
        except:
            pass 