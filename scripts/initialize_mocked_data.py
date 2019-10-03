from mock.models import Mock

print("Criando mock...", "end")

mock_data = [
            ["Pegaso","20.22","1122.11","2222.22","111.111.2","111.1111.3"],
            ["Dragao","30.33","1133.11","3333.22","111.111.4","111.1111.5"],
            ["Cisne","40.44","1144.11","4444.22","111.111.6","111.1111.7"],
            ["Andromeda","50.55","1155.11","5555.22","111.111.8","111.1111.9"]
            ]

for mock in(mock_data):

    data = Mock.objects.create(
        module_name = mock[0],
        temperature = mock[1],
        co2 = mock[2],
        humidity = mock[3],
        latitude = mock[4],
        longitude = mock[5]
    )

print("OK")