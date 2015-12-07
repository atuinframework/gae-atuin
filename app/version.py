version = (0, 0, 1)
date = (01, 01, 2015)

string = "{}.{}.{}".format(*version)
date_string = '{}.{}.{}'.format(*date)

full_string = ' - '.join((string, date_string))
