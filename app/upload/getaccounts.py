import sys
sys.path.append("/usr/src/app/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from upload.managefiles import ManageFiles
from upload.scraper import DataScraper
from upload.models import Accounts
from upload.scraped_headers import wanted

url = 'http://download.companieshouse.gov.uk/Accounts_Bulk_Data-2020-05-16.zip'
m = ManageFiles(url)
m.download()
#m.unzip()
#file_list = m.list_files()
#for file_name in file_list[:10]:
#    scrape = DataScraper('/usr/src/app/upload/temp/' + file_name)
#    output = scrape.get_id() + scrape.get_num(wanted)
#    ac = Accounts(scrape)
#    ac.save()
#m.delete()





LOOKUP = {
        'accumulateddepreciationnotincludingimpairmentpropertyplantequipment': 'accdepnotincludimpairmentpropertyplantequipment'
        'additionalprovisionsincreasefromnewprovisionsrecognisedinprofitorloss': 'addprovincreasefromnewprovrecognisedinprofitorloss'
        'additionsotherthanthroughbusinesscombinationsinvestmentpropertyfairvaluemodel': 'addsotherthanthrubusincombosinvstmntproprtyfairvaluemodel'
        'additionstherthanthroughbusinesscombinationspropertyplantequipment': 'addsotherthanthroughbusincombospropertyplantequipment'
        'carryingamountundercostmodelrevaluedassetspropertyplantequipment': 'crryingamntundercostmodelrevaluedassetspropertyplantequipment'
        'deferredtaxexpensecreditrelatingtooriginationreversaltimingdifferences': 'deftaxexpensecreditrelatingtoorigintionreversltimingdiffs'
        'furtherdepartmentitemaveragenumberemployeescomponentaveragenumberlist': 'furtherdepitemavgnoemployeescomponentaveragenumberlist'
        'furtheritemgainlossinothercomprehensiveincomebeforetaxcomponenttotalothercomprehensiveincomebeforetax': 'inothercomprehincomepretaxcmpntttlothercompincomepretax'
        'furtheritemgainlossinothercomprehensiveincomenettaxcomponenttotalothercomprehensiveincomenettax': 'gainlssinothercomprehincomenttxcmpnttotalothercomprencomenttx'
        'furtheritemincomefromothertradingactivitiescomponenttotalincomefromothertradingactivities': 'itmincmefrmothertrdingactvtiestotalmfrmothertradingactivities'
        'furtheritemincreasedecreaseinequitycomponenttotalincomeexpenserecogniseddirectlyinequity': 'frthritemincdecrinequitytotalincomxpnsercognseddirctlyinquity'
        'furtheritemincreasedecreaseininvestmentpropertyfairvaluemodelcomponentcorrespondingtotal': 'itmincreasedecreaseininvestmentpropertyfrvalumodelcorrespttl'
        'furtheritemoperatingexpenselossincomestatementitemcomponentoperatingprofitloss': 'itemoperatingxpnslossincmesttmntitemcomponentopratngproftlss'
        'gainlossfromfairvalueadjustmentinvestmentpropertyrecognisedinprofitorloss': 'gainlossfromfrvaluadjstmntinvstmentpropertyrecgnsedinprftlss'
        'gainlossonremeasurementdefinedbenefitplansbeforetaxinothercomprehensiveincome': 'gainlossonremeasurementdfndbnftplnsbfrtxinothrcomprehincome'
        'gainlossonrevaluationotherassetsnettaxinothercomprehensiveincome': 'gainlssonrvluationotherasstsnttxinothercmprehensveincome'
        'gainlossonrevaluationpropertyplantequipmentbeforetaxinothercomprehensiveincome': 'gnlssonrvltionprpertyplnteqpmentbfortxinothrcomprehincme'
        'gainlossonrevaluationpropertyplantequipmentnettaxinothercomprehensiveincome': 'gainlossonrvaluationprprtyplnteqpmentnttxinthercmprehincme'
        'increasedecreaseduetotransfersbetweenclassespropertyplantequipment': 'incrsedcrseduetotrnsfrsbtwnclassespropertyplantequipment'
        'increasedecreasefromfairvalueadjustmentinvestmentpropertyfairvaluemodel': 'increasedecreasefromfrvaluadjstmntinvstmntprprtyfrvluemdel'
        'increasedecreaseincashcashequivalentsbeforeforeignexchangedifferenceschangesinconsolidation': 'incrdecrincashbeforeexchangedifferenceschangesinconsolidation'
        'increasedecreaseindeferredtaxliabilityfromamountrecognisedinprofitorloss': 'incrsdcseindeftxlbilityfromamountrecognisedinprofitorloss'
        'increasedecreaseinnetdeferredtaxliabilityfromamountrecognisedinprofitorloss': 'incdecrinntdeftxlbilityfrmamountrecognisedinprfitorlss'
        'interestexpenseonfinancialliabilitiesfairvaluethroughprofitorloss': 'intrstexpnseonfinanciallbilitiesfrvluethruprftorlss'
        'interestexpenseonobligationsunderfinanceleaseshirepurchasecontracts': 'interestexpnsonobligtionsunderfinleasehirepurchcntrcts'
        'netincomeexpenditurebeforetransfersbetweenfundsotherrecognisedgainslosses': 'netincomexpndbeftrnsfrsbtwnfndsotherrcognisedgainslsses'
        'othercreditorsincludingtaxationsocialsecuritybalancesheetsubtotal': 'othercrditorsincltxtionscialsecurtyblncesheetsubtotal'
        'otherdisposalsdecreaseindepreciationimpairmentpropertyplantequipment': 'otherdspsalsdcrseindeprecimprmentprprtyplantequipment'
        'otherincreasedecreaseindepreciationimpairmentpropertyplantequipment': 'otherincrsedecrseindeptionimprmentprprtyplantequipment'
        'revaluationsincreasedecreaseindepreciationimpairmentpropertyplantequipment': 'revlutionsincrsedecrseindprctionimprmntpropertyplnteqpmnt'
        'taxincreasedecreasefromeffectadjustmentinresearchdevelopmenttaxcredit': 'txincrsdecrsefromffectadjstmntinresrchdevtaxcredit'
        'taxincreasedecreasefromeffectexpensesnotdeductiblefortaxpurposesotherthangoodwillamortisationimpairment': 'txincdecrfrmffctxpnssntddctiblefrtaxotherthngdwllamortimprmen'
        'taxincreasedecreasefromeffectexpensesnotdeductibleindeterminingtaxableprofitorloss': 'txincrdecrfromefectexpensesnotdctindeterintxableproforloss'
        'totaladditionsincludingfrombusinesscombinationspropertyplantequipment': 'totaladdsinclfrmbusincombopropertyplantequipment'
        'transfersbetweenppeclassesincreasedecreaseindepreciationimpairment': 'transfersbetwnppeclassesincreasedecrindeprimpairment'
        'transfersintooroutpropertyplantequipmentincreasedecreaseindepreciationimpairment': 'trnsfrsintopropertyplantequipmentincrecrindeimprment'
        'additionsotherthanthroughbusinesscombinationspropertyplantequipment': 'additionsotherthanthrubusincombospropertyplantequipment'
        }
