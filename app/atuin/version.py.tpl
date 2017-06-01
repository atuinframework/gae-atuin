
version = (0, 0, 1)
date = (21, 3, 2016)

string = "{}.{}.{}".format(*version)
date_string = '{}.{}.{}'.format(*date)

full_string = ' - '.join((string, date_string))
