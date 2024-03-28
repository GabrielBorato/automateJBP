####################imports###################
from botcity.plugins.ms365.credentials import MS365CredentialsPlugin, Scopes
from botcity.plugins.ms365.outlook import MS365OutlookPlugin
from botcity.plugins.excel import BotExcelPlugin
bot_excel = BotExcelPlugin()

service = MS365CredentialsPlugin(
    client_id='af7bc03b-8366-4a4e-98b0-4a3bbe488e3b',
    client_secret='umk8Q~PSCPFcHPeU9J2dVKfFCeKNf_XNUwM2tbVM',
)
scopes_list = [Scopes.BASIC, Scopes.FILES_READ_WRITE_ALL, Scopes.MAIL_READ_WRITE, Scopes.MAIL_READ_WRITE, Scopes.MAIL_SEND]
service.authenticate(scopes=scopes_list)
outlook = MS365OutlookPlugin(service_account=service)
####################JBP-Outlook#######################
bot_excel.read('K:\\JBP\\JBP-Auto\\01 -Parâmetros\\Disparo JBP.xlsx')

def ler_dados_excel():
    return {
        "fornecedores": bot_excel.get_column(column="A")[1:],
        "emails": bot_excel.get_column(column="B")[1:],
        "copias": bot_excel.get_column(column="C")[1:],
        "caminhoArquivo": bot_excel.get_column(column="D")[1:],
    }

dados = ler_dados_excel()
subject = "Teste"

for fornecedor, email, copia, caminhoArq in zip(
        dados["fornecedores"],dados["emails"], dados["copias"],
        dados["caminhoArquivo"]
 ):
    body = f"Olá {fornecedor}, segue arquivo.\n"
    files = [caminhoArq]
   #Enviando a mensagem de e-mail
    outlook.send_message(subject,body,[email],attachments=files)
# falta anexo