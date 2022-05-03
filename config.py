import toml

env = toml.load('env.toml')


class Api:
    data = env['Api']

    ID = data['ID']
    HASH = data['HASH']


class Secret:
    data = env['Secret']

    channel_id = data['channel_id']
    post_id = data['post_id']
    texts = data['texts']
