import requests, bs4
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from SpreadsheetTools import SpreadsheetTools

def getCharNickname(s):
    x = str(s)
    newstr = x.replace("[", "")
    newstr2 = newstr.replace("]", "")
    return newstr2.replace("'", "")

def main():
    CREDENTIALS_FILE = 'wowparserassist-bfeb2fb346fa.json' # имя файла с закрытым ключом
    tools = SpreadsheetTools(CREDENTIALS_FILE, debugMode=True)
    #docId = '17MvXorJo_stNi8129gOStuTrGKdfO5cf-3x82ddqXdQ' #тестовый док
    #docId = '1eI61oFGr1BmPjvI3rlrwbxQvOq6CDNvA1z1P19zSLRQ' #это мой ID
    docId = '1IKgfrzC2yIzMUABSQbJoU34xu1BWdHzraS7TbmoNulI' #Спектр
    tools.setSpreadsheetById(docId)
    tools.setSheet('Чары 12')

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    request = service.spreadsheets().get(spreadsheetId= docId, ranges= [], includeGridData= False)
    response = request.execute()

    #request = service.spreadsheets().values().get(spreadsheetId=docId, range="Сие есть название листа!A:A")
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 12!A:A")
    response = request.execute()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                r = requests.get(URL)
                json = r.json()
                items = json.get('items')
                averangeItemLevelEquipped = items.get('averageItemLevelEquipped')
                item2 = items.get('neck')
                neckItemLevel = item2.get('itemLevel')
                item3 = item2.get('azeriteItem')
                artLevel = item3.get('azeriteLevel')
                values = 'B' + str(t + 1) + ':C' + str(t + 1);
                tools.prepare_setValues(values,
                                        [[str(neckItemLevel) + '(' + str(artLevel) + ')', averangeItemLevelEquipped]])
                tools.runPrepared()
            except:
                values = 'B' + str(t + 1) + ':C' + str(t + 1);
                tools.prepare_setValues(values,
                                        [['error', 'error']])
                tools.runPrepared()
                t += 1
                continue
        t += 1



    tools.setSheet('Чары 20')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 20!A:A")
    response = request.execute()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                r = requests.get(URL)
                json = r.json()
                items = json.get('items')
                averangeItemLevelEquipped = items.get('averageItemLevelEquipped')
                item2 = items.get('neck')
                neckItemLevel = item2.get('itemLevel')
                item3 = item2.get('azeriteItem')
                artLevel = item3.get('azeriteLevel')
                values = 'B' + str(t + 1) + ':C' + str(t + 1);
                tools.prepare_setValues(values,
                                        [[str(neckItemLevel) + '(' + str(artLevel) + ')', averangeItemLevelEquipped]])
                tools.runPrepared()
            except:
                values = 'B' + str(t + 1) + ':C' + str(t + 1);
                tools.prepare_setValues(values,
                                        [['error', 'error']])
                tools.runPrepared()
                t += 1
                continue
        t += 1

    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 20!D:D")
    response = request.execute()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                r = requests.get(URL)
                json = r.json()
                items = json.get('items')
                averangeItemLevelEquipped = items.get('averageItemLevelEquipped')
                item2 = items.get('neck')
                neckItemLevel = item2.get('itemLevel')
                item3 = item2.get('azeriteItem')
                artLevel = item3.get('azeriteLevel')
                values = 'E' + str(t + 1) + ':F' + str(t + 1);
                tools.prepare_setValues(values,
                                        [[str(neckItemLevel) + '(' + str(artLevel) + ')', averangeItemLevelEquipped]])
                tools.runPrepared()
            except:
                values = 'E' + str(t + 1) + ':F' + str(t + 1);
                tools.prepare_setValues(values,
                                        [['error', 'error']])
                tools.runPrepared()
                t += 1
                continue
        t += 1


if __name__ == "__main__":
    main()
'''
CREDENTIALS_FILE = 'wowparserassist-bfeb2fb346fa.json'  # имя файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
#1eI61oFGr1BmPjvI3rlrwbxQvOq6CDNvA1z1P19zSLRQ #это мой ID
docId = '17MvXorJo_stNi8129gOStuTrGKdfO5cf-3x82ddqXdQ' #тестовый док
#spreadsheet = service.spreadsheets().create(body = {
#    'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
#    'sheets': [{'properties': {'sheetType': 'GRID',
#                               'sheetId': 0,
#                               'title': 'Сие есть название листа',
#                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
#}).execute()
request = service.spreadsheets().get(spreadsheetId= docId, ranges= [], includeGridData= False)
response = request.execute()
print(response)
#driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
#shareRes = driveService.permissions().create(
#    fileId = docId,
#    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'zioba1404@gmail.com'},
#).execute()
request = service.spreadsheets().values().get(spreadsheetId=docId, range="Сие есть название листа!B2:C2", valueRenderOption='', dateTimeRenderOption='')
response = request.execute()
pprint(response)

results = service.spreadsheets().values().batchUpdate(spreadsheetId = docId, body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "Сие есть название листа!B2:C2",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": [["Azerite Level", "Item Level"]]}
    ]
}).execute()
s=requests.get('https://www.wowprogress.com/character/eu/ревущий-фьорд/Зёба')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p3=b.select('.char_rating_area .gearscore')
    pogoda1=p3[3].getText()
    print('Azerite Level:' + pogoda1)
'''