import toml

env = toml.load('env.toml')


class Api:
    data = env['Api']

    ID = data['ID']
    HASH = data['HASH']
