
class MyNullAction(Action):
    """
    :doc: control_action

    Does nothing.

    This can be used to make a button responsive to hover/unhover events,
    without actually doing anything.
    """

    def __call__(self):
        return
