from materials.QueryAPI import WolframAPI

key = 'YOUR-KEY-HERE'

api = WolframAPI(key)

ans = api.query("water","density")

print(ans)