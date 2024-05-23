class SpotifyService:
    def __init__(self, access_code):
        self._access_code = access_code

    def test_connection(self):
        print(f'Accessing Spotify with {self._access_code}')


class ServiceBuilder:
    def __init__(self):
        self._instance = None
        print('Initializing builder..')

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        else:
            print('*There exists an exiting connection.. reusing it')
        return self._instance

    def authorize(self, key, secret):
        return f'key:{key} secret:{secret}'

    @property
    def name(self):
        print('lol what is the matter?')


if __name__ == '__main__':
    ConnectionBuilder = ServiceBuilder()     # this is the factory
    Service_instance_1 = ConnectionBuilder('my_key','my_secret')
    Service_instance_1.test_connection()
    Service_instance_1.test_connection()
    Service_instance_2 = ConnectionBuilder('my_key','my_secret') # try to create another service instance
    ConnectionBuilder.name
