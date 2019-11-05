import ipdb
class UnnecessaryError(Exception):
    pass


def i_just_throw_an_exception():

    ipdb.set_trace()
    raise UnnecessaryError("You actually called this function...")
