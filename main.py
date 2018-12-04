import requests, bs4
import httplib2
import apiclient.discovery
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from SpreadsheetTools import SpreadsheetTools

def getCharNickname(s):
    x = str(s)
    newstr = x.replace("[", "")
    newstr2 = newstr.replace("]", "")
    return newstr2.replace("'", "")

def main():
    CREDENTIALS_FILE = 'wowparserassist-bfeb2fb346fa.json' # имя файла с закрытым ключом
    docId = '1IKgfrzC2yIzMUABSQbJoU34xu1BWdHzraS7TbmoNulI'  # Спектр
    tools = SpreadsheetTools(CREDENTIALS_FILE, debugMode=True)
    tools.setSpreadsheetById(docId)

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

#чары 12 лист
    tools.setSheet('Чары 12')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 12!A:A")
    response = request.execute()
    tools.prepare_setValues("H1:H1", [[str(datetime.datetime.now().date())]])
    tools.runPrepared()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            values = 'B' + str(t + 1) + ':C' + str(t + 1);
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                json = requests.get(URL).json()
                averangeItemLevelEquipped = json.get('items').get('averageItemLevelEquipped')
                neck = json.get('items').get('neck')
                neckItemLevel = neck.get('itemLevel')
                artLevel = neck.get('azeriteItem').get('azeriteLevel')
                tools.prepare_setValues(values,
                                        [[averangeItemLevelEquipped, str(artLevel) + ' (' + str(neckItemLevel) + ')']])
            except:
                tools.prepare_setValues(values,
                                        [['error', 'error']])
            tools.runPrepared()
        t += 1
#чары 20 лист мейны
    tools.setSheet('Чары 20')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 20!A:A")
    response = request.execute()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            values = 'B' + str(t + 1) + ':C' + str(t + 1);
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                json = requests.get(URL).json()
                averangeItemLevelEquipped = json.get('items').get('averageItemLevelEquipped')
                neck = json.get('items').get('neck')
                neckItemLevel = neck.get('itemLevel')
                artLevel = neck.get('azeriteItem').get('azeriteLevel')
                tools.prepare_setValues(values,
                                        [[averangeItemLevelEquipped,
                                          str(artLevel) + ' (' + str(neckItemLevel) + ')']])
            except:
                tools.prepare_setValues(values,
                                        [['error', 'error']])
            tools.runPrepared()
        t += 1

#чары 20 лист твинки
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Чары 20!D:D")
    response = request.execute()
    tools.prepare_setValues("H1:H1", [[str(datetime.datetime.now().date())]])
    tools.runPrepared()
    charNicknames = response.get('values')
    t = 0;
    for i in charNicknames:
        if (t != 0):
            values = 'E' + str(t + 1) + ':F' + str(t + 1);
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=items&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                json = requests.get(URL).json()
                averangeItemLevelEquipped = json.get('items').get('averageItemLevelEquipped')
                neck = json.get('items').get('neck')
                neckItemLevel = neck.get('itemLevel')
                artLevel = neck.get('azeriteItem').get('azeriteLevel')
                tools.prepare_setValues(values,
                                        [[averangeItemLevelEquipped, str(artLevel) + ' (' + str(neckItemLevel) + ')']])
            except:
                tools.prepare_setValues(values,
                                        [['error', 'error']])
            tools.runPrepared()
        t += 1
#доступы
    tools.setSheet('Доступы')
    tools.setSheetNumbId('Доступы') #функция костыльная, там забит id листа вручную
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Доступы!A:A")
    response = request.execute()
    charNicknames = response.get('values')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Доступы!B:B")
    response = request.execute()
    charRoles = response.get('values')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Доступы!C:C")
    response = request.execute()
    charEmails = response.get('values')
    request = service.spreadsheets().values().get(spreadsheetId=docId, range="Доступы!E:E")
    response = request.execute()
    charStatus = response.get('values')
    tools.prepare_setValues("H1:H1", [[str(datetime.datetime.now().date())]])
    tools.runPrepared()
    t = 0;
    for i in charNicknames:
        if (t > 1):
            try:
                status = getCharNickname(charStatus[t])
            except:
                status = "1"
            try:
                player = getCharNickname(i)
                URL = 'https://eu.api.battle.net/wow/character/ревущий-фьорд/' + player + '?fields=guild&locale=ru_RU&apikey=a54rf7cgky8w4nt6hwjt67bwkdmkkpbp'
                r = requests.get(URL)
                json = r.json()
                print(json)
                try:
                    guild = json.get('guild')
                    guildName = guild.get('name')
                except:
                    guildName = "no guild"
                values = 'D' + str(t + 1) + ':F' + str(t + 1);
                if (guildName == 'Спектр'):
                    try:
                        driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
                        if (status != 'права выданы'):
                            role = getCharNickname(charRoles[t])
                            email = getCharNickname(charEmails[t])
                            driveService.permissions().create(
                                fileId=docId,
                                body={'type': 'user', 'role': role, 'emailAddress': email},
                            ).execute()
                            tools.prepare_setValues(values, [['OK', 'права выданы', '']])
                            tools.runPrepared()
                            tools.prepare_setCellsFormats(values,
                                                          [[{'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}},
                                                            {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}},
                                                            {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}}]])
                            tools.runPrepared()
                    except:
                        tools.prepare_setValues(values, [['FAIL', 'неправильная роль или почта', 'права не выданы']])
                        tools.runPrepared()
                        tools.prepare_setCellsFormats(values, [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                                                {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}},
                                                                {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}}]])
                        tools.runPrepared()
                        t += 1
                        continue
                else:
                    if (status == 'права выданы'):
                        email = getCharNickname(charEmails[t])
                        driveService = apiclient.discovery.build('drive', 'v2', http=httpAuth)
                        permissions = driveService.permissions().getIdForEmail(email=email).execute()
                        print(permissions['id'])
                        driveService.permissions().delete(
                            fileId = docId,
                            permissionId=permissions['id']
                        ).execute()
                        tools.prepare_setValues(values, [['FAIL', 'чел в другой гильдии', 'права удалены']])
                        tools.runPrepared()
                        tools.prepare_setCellsFormats(values, [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                                                {'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                                                {'backgroundColor': {'red': 1, 'green': 1,
                                                                                     'blue': 1}}]])
                        tools.runPrepared()
            except:
                if (status == 'права выданы'):
                    email = getCharNickname(charEmails[t])
                    driveService = apiclient.discovery.build('drive', 'v2', http=httpAuth)
                    permissions = driveService.permissions().getIdForEmail(email=email).execute()
                    print(permissions['id'])
                    driveService.permissions().delete(
                        fileId=docId,
                        permissionId=permissions['id']
                    ).execute()
                values = 'D' + str(t + 1) + ':F' + str(t + 1);
                tools.prepare_setValues(values,
                                        [['FAIL', 'персонажа не существует', 'права удалены']])
                tools.runPrepared()
                tools.prepare_setCellsFormats(values, [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                                        {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}},
                                                        {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}}]])
                tools.runPrepared()
        t += 1


if __name__ == "__main__":
    main()