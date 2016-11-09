# -*- coding: utf-8 -*-

__author__  = "YanHuiru <hyan@linkernetworks.com>"
__version__ = "1.1"

#############通用#############
ConfirmL       = "xpath=//*[@class='btn btn-primary ng-binding']"    #Confirmation buttons for all pop-up boxes, including confirmation,deletion,creation,saving,and so on
CancelL        = "xpath=//*[@class='btn btn-warning ng-binding']"    #Cancel button for all pop-up boxes
TableNameL     = "xpath=//*[text()='Name']"                          #The column name in the table cell,used to wait for the page to load

#############登录页面#############
LinkerlogoL    = "xpath=//img[@src='img/linker.png']"              #The logo on the login page,used to wait for the page to load
UserNameL      = "xpath=//input[@name='usernameInput']"            #The input box for the user name
PasswordL      = "xpath=//input[@name='passwordInput']"            #The input box for the password
LoginButtonL   = "xpath=//button[@ng-click='login();']"            #Login button

#############Node#############
EnglishL       = "xpath=//*[text()='English']"                     #Switch to English
TableNameChineseL     = "xpath=//*[text()='名称']".decode('utf-8') #The column name in the table cell,used to wait for the page to load

#############Configuration#############
ConfigurationL    = "xpath=//*[text()=' Configuration']"              #Page-Configuration
KeyL              = "xpath=//*[text()='Login Key Pair']"              #Tab-Login Key Pair
SMTPL             = "xpath=//*[text()='SMTP Server']"                 #Tab-SMTP Server
PlatfromL         = "xpath=//*[text()='Platform Management']"         #Tab-Platform Management
RepositoryL       = "xpath=//*[text()='Docker Registry']"             #Tab-Docker Registry
#Login Key Pair
CreatekeyL     = "xpath=//button[@ng-click='createKeyPair()']"      #创建密钥
UploadkeyL     = "xpath=//*[@ng-click='uploadKeyPair()']"           #上传密钥
KeyNameL	   = "xpath=//input[@ng-model='keypair.name']"          #密钥名称输入框
Testkey1L      = "xpath=//tr/td[text()='test1']"                    #table内test1密钥的名称定位，多用于验证该密钥是否存在
Testkey2L      = "xpath=//tr/td[text()='test2']"                    #类上test2
Testkey3L      = "xpath=//tr/td[text()='test3']"                    #类上test3
Testkey3DeleteL   = "xpath=//td[text()='test3']/../td/button"       #密钥test3的删除按钮
PubkeyValueL   = "xpath=//*[@ng-model='keypair.pubkeyValue']"       #上传密钥时密钥值输入框
#SMTP Server
AddServerL    = "xpath=//*[@ng-click='addSMTPServer()']" 
EditServerL = "xpath=//tr/td/button[1]"
DeleteServerL = "xpath=//tr/td/button[2]"
ServerNameL   = "name=address"
SMTPUserNameL     = "name=smtpname"
SMTPPasswordL     = "name=passwd"
ServerCellName1L   = "xpath=//*[text()='smtp.qiye.163.com']"
ServerCellName2L   = "xpath=//*[text()='smtp.qq.com']"
#Platform Management
CreatePlatformL    = "xpath=//*[@ng-click='createPlatform()']"          #创建平台
PlatformTypeL    = "xpath=//*[@ng-model='platform.type']"               #aws的tokyotest账号信息
SshUserL	    = "name=SshUser"
NameL	        = "name=name"
AccessKeyL	    = "name=AccessKey"
SecretKeyL	    = "name=SecretKey"
ImageIdL	    = "name=ImageId"
InstanceTypeL   = "name=InstanceType"
RootSizeL       = "name=RootSize"
RegionL         = "name=Region"
VPCIDL          = "name=VPCID"
AwsPlatform1L  = "xpath=//tr/td[text()='aws1']"                   #table内aws1t平台名称定位
AwsPlatform2L  = "xpath=//tr/td[text()='aws2']"                   #table内aws2t平台名称定位
AwsPlatform2DeleteL   = "xpath=//td[text()='aws2']/../td/button[2]"  #平台aws2的删除按钮
#Docker Registry
CreateRegistryL    = "xpath=//*[@ng-click='createRegistry()']"
RegistryNameL      = "name=name"
RegistryURLL       = "name=registry"
SecureTrueL        = "xpath=//input[@ng-value='true']"
SecureFalseL       = "xpath=//input[@ng-value='false']"
CertificateL       = "name=ca_text"
RegistryUserNameL  = "xpath=//input[@ng-model='registry.username']"
RegistryPasswordL  = "xpath=//input[@ng-model='registry.password']"
InsecureCellNameL = "xpath=//tr/td[text()='Insecure']"
InauthCellNameL   = "xpath=//tr/td[text()='Inauth']"
CACellNameL       = "xpath=//tr/td[text()='CA']"
CAauthCellNameL   = "xpath=//tr/td[text()='CAauth']"
ForDeleteCellNameL   = "xpath=//tr/td[text()='ForDelete']"
ForDeleteDeleteL   = "xpath=//tr/td[text()='ForDelete']/../td/button[2]"