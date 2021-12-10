from collections import deque

# Queue used for storing mqtt messages and sent them
# Format: [ (<sub_topic>,<command>),(<topic>,<command>) ]
# Subtopic means that the root topic must not be specified
mqqt_commands_queue=deque([])


def get_mqtt_queue():
    return mqqt_commands_queue

