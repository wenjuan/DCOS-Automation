# -*- coding: utf-8 -*-

__author__  = "YanHuiru <hyan@linkernetworks.com>"
__version__ = "1.1"

#############通用#############
ConfirmL       = "xpath=//*[@class='btn btn-primary ng-binding']"    #Confirmation buttons for all pop-up boxes, including confirmation,deletion,creation,saving,and so on
CancelL        = "xpath=//*[@class='btn btn-warning ng-binding']"    #Cancel button for all pop-up boxes
TableNameL     = "xpath=//*[text()='Name']"                          #The column name in the table cell,used to wait for the page to load

#############登录页面#############
LinkerlogoL    = "xpath=//img[@src='img/linker.png']"              #The logo on the login page,used to wait for the page to load
UserNameL      = "xpath=//input[@name='usernameInput']"            #Input Box-User Name
PasswordL      = "xpath=//input[@name='passwordInput']"            #Input Box-Password
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
CreatekeyL     = "xpath=//button[@ng-click='createKeyPair()']"      #Button-Create Key Pair
UploadkeyL     = "xpath=//*[@ng-click='uploadKeyPair()']"           #Button-Upload Key Pair
KeyNameL	   = "xpath=//input[@ng-model='keypair.name']"          #Input Box-Key Name
Testkey1L      = "xpath=//tr/td[text()='test1']"                    #Cell Locator-The Name Of The Key test1
Testkey2L      = "xpath=//tr/td[text()='test2']"                    #Ibidem
Testkey3L      = "xpath=//tr/td[text()='test3']"                    #Ibidem
Testkey3DeleteL   = "xpath=//td[text()='test3']/../td/button"       #Button-Delete Key test3
PubkeyValueL   = "xpath=//*[@ng-model='keypair.pubkeyValue']"       #Input Box-Public Key When Uploading A Key Pair
#SMTP Server 
AddServerL    = "xpath=//*[@ng-click='addSMTPServer()']"            #Button-Create Server
EditServerL = "xpath=//tr/td/button[1]"                             #Button-Edit Server
DeleteServerL = "xpath=//tr/td/button[2]"                           #Button-Delete Server
ServerNameL   = "name=address"                                      #Input Box-Server Name
SMTPUserNameL     = "name=smtpname"                                 #Input Box-User Name Of Server
SMTPPasswordL     = "name=passwd"                                   #Input Box-Password Of Server
ServerCellName1L   = "xpath=//*[text()='smtp.qiye.163.com']"        #Cell Locator-The Name Of The Server 'smtp.qiye.163.com'
ServerCellName2L   = "xpath=//*[text()='smtp.qq.com']"              #Cell Locator-The Name Of The Server 'smtp.qq.com'
#Platform Management
CreatePlatformL    = "xpath=//*[@ng-click='createPlatform()']"          #Button-Create Platform
PlatformTypeL    = "xpath=//*[@ng-model='platform.type']"               #Select From List-Platform Type
PSshUserL	    = "name=SshUser"                                        #Input Box-SSH User
PNameL	        = "name=name"                                           #Input Box-Platform Name
PAccessKeyL	    = "name=AccessKey"                                      #Input Box-Access Key
PSecretKeyL	    = "name=SecretKey"                                      #Input Box-Secret Key
PImageIdL	    = "name=ImageId"                                        #Input Box-Image ID
PInstanceTypeL   = "name=InstanceType"                                  #Input Box-Instance Type
PRootSizeL       = "name=RootSize"                                      #Input Box-Root Size(GB)
PRegionL         = "name=Region"                                        #Input Box-Region
PVPCIDL          = "name=VPCID"                                         #Input Box-VPC ID
AwsPlatform1L  = "xpath=//tr/td[text()='aws1']"                      #Cell Locator-The Name Of The Platform aws1
AwsPlatform2L  = "xpath=//tr/td[text()='aws2']"                      #Cell Locator-The Name Of The Platform aws2
AwsPlatform2DeleteL   = "xpath=//td[text()='aws2']/../td/button[2]"  #Button-Delete Platform aws2
AwsPlatform3EditL   = "xpath=//td[text()='aws3']/../td/button[1]"    #Button-Edit Platform aws3
#Docker Registry
CreateRegistryL    = "xpath=//*[@ng-click='createRegistry()']"          #Button-Create Registry
RegistryNameL      = "name=name"                                        #Input Box-Registry Name
RegistryURLL       = "name=registry"                                    #Input Box-Registry URL
SecureTrueL        = "xpath=//input[@ng-value='true']"                  #Check-True
SecureFalseL       = "xpath=//input[@ng-value='false']"                 #Check-False
CertificateL       = "name=ca_text"                                     #Input Box-Certificate
RegistryUserNameL  = "xpath=//input[@ng-model='registry.username']"     #Input Box-Username
RegistryPasswordL  = "xpath=//input[@ng-model='registry.password']"     #Input Box-Password
InsecureCellNameL = "xpath=//tr/td[text()='Insecure']"                  #Cell Locator-The Name Of The Registry Insecure
InauthCellNameL   = "xpath=//tr/td[text()='Inauth']"                    #Cell Locator-The Name Of The Registry Inauth
CACellNameL       = "xpath=//tr/td[text()='CA']"                        #Cell Locator-The Name Of The Registry CA
CAauthCellNameL   = "xpath=//tr/td[text()='CAauth']"                    #Cell Locator-The Name Of The Registry CAauth
ForDeleteCellNameL   = "xpath=//tr/td[text()='ForDelete']"              #Cell Locator-The Name Of The Registry ForDelete
ForDeleteDeleteL   = "xpath=//tr/td[text()='ForDelete']/../td/button[2]"#Button-Delete Registry ForDelete