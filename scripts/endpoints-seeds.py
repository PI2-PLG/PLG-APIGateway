from endpoints.models import Endpoint

'''

No lugar de "localhost" você deve colocar o ip local da sua máquina :)

'''
endpoint_data = [
                 ["GetAllModuleData","BI","http://localhost:8003/all-module-data/"],
                 ["GetAllModuleList","BI","http://localhost:8003/all-modules-list/"],
                 ["GetAllData","BI","http://localhost:8003/all-data/"],
                ]

print("Adicionando endpoints... ", end="")
for data in endpoint_data:
    endpoint, created = Endpoint.objects.get_or_create(name=data[0], service=data[1], url=data[2])
    if created:
        print(endpoint.name)
    else:
        endpoint.save()
print("Ok!")