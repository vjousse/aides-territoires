from collections import namedtuple


# The variable name that stores goal conversion
GOAL_KEY = '_analytics_goal'


# A basic structure to store custom variables to pass to matomo
CustomVariable = namedtuple('CustomVariable', ['index', 'name', 'value'])


def track_goal(session, goal_id):
    """Set an analytics goal to be tracked."""
    session[GOAL_KEY] = goal_id


def get_goal(session):
    """Returns the currently tracked goal id.

    Also, clears the session, so we only track a specific goal using
    the js api once.
    """
    return session.pop(GOAL_KEY, '')


def track_custom_variable(index, name, value):
    """Custom variables can be passed to matomo."""

    context = {
        'analytics_custom_variable': CustomVariable(index, name, value)
    }
    return context
