# Generated by Django 3.0.6 on 2020-05-13 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyname', models.CharField(max_length=255)),
                ('companynumber', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('regaddress_careof', models.CharField(max_length=255)),
                ('regaddress_pobox', models.CharField(max_length=255)),
                ('regaddress_addressline1', models.CharField(max_length=255)),
                ('regaddress_addressline2', models.CharField(max_length=255)),
                ('regaddress_posttown', models.CharField(max_length=255)),
                ('regaddress_county', models.CharField(max_length=255)),
                ('regaddress_country', models.CharField(max_length=255)),
                ('regaddress_postcode', models.CharField(max_length=255)),
                ('companycategory', models.CharField(max_length=255)),
                ('companystatus', models.CharField(max_length=255)),
                ('countryoforigin', models.CharField(max_length=255)),
                ('dissolutiondate', models.DateTimeField()),
                ('incorporationdate', models.DateTimeField()),
                ('accounts_accountrefday', models.IntegerField(null=True)),
                ('accounts_accountrefmonth', models.IntegerField(null=True)),
                ('accounts_nextduedate', models.DateTimeField()),
                ('accounts_lastmadeupdate', models.DateTimeField()),
                ('accounts_accountcategory', models.CharField(max_length=255)),
                ('returns_nextduedate', models.DateTimeField()),
                ('returns_lastmadeupdate', models.DateTimeField()),
                ('mortgages_nummortcharges', models.IntegerField(null=True)),
                ('mortgages_nummortoutstanding', models.IntegerField(null=True)),
                ('mortgages_nummortpartsatisfied', models.IntegerField(null=True)),
                ('mortgages_nummortsatisfied', models.IntegerField(null=True)),
                ('siccode_sictext_1', models.CharField(max_length=255)),
                ('siccode_sictext_2', models.CharField(max_length=255)),
                ('siccode_sictext_3', models.CharField(max_length=255)),
                ('siccode_sictext_4', models.CharField(max_length=255)),
                ('limitedpartnerships_numgenpartners', models.IntegerField(null=True)),
                ('limitedpartnerships_numlimpartners', models.IntegerField(null=True)),
                ('url', models.CharField(max_length=255)),
                ('previousname_1_condate', models.DateTimeField()),
                ('previousname_1_companyname', models.CharField(max_length=255)),
                ('previousname_2_condate', models.DateTimeField()),
                ('previousname_2_companyname', models.CharField(max_length=255)),
                ('previousname_3_condate', models.DateTimeField()),
                ('previousname_3_companyname', models.CharField(max_length=255)),
                ('previousname_4_condate', models.DateTimeField()),
                ('previousname_4_companyname', models.CharField(max_length=255)),
                ('previousname_5_condate', models.DateTimeField()),
                ('previousname_5_companyname', models.CharField(max_length=255)),
                ('previousname_6_condate', models.DateTimeField()),
                ('previousname_6_companyname', models.CharField(max_length=255)),
                ('previousname_7_condate', models.DateTimeField()),
                ('previousname_7_companyname', models.CharField(max_length=255)),
                ('previousname_8_condate', models.DateTimeField()),
                ('previousname_8_companyname', models.CharField(max_length=255)),
                ('previousname_9_condate', models.DateTimeField()),
                ('previousname_9_companyname', models.CharField(max_length=255)),
                ('previousname_10_condate', models.DateTimeField()),
                ('previousname_10_companyname', models.CharField(max_length=255)),
                ('confstmtnextduedate', models.DateTimeField()),
                ('confstmtlastmadeupdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equity', models.IntegerField(null=True)),
                ('creditors', models.IntegerField(null=True)),
                ('propertyplantequipment', models.IntegerField(null=True)),
                ('netassetsliabilities', models.IntegerField(null=True)),
                ('netcurrentassetsliabilities', models.IntegerField(null=True)),
                ('totalassetslesscurrentliabilities', models.IntegerField(null=True)),
                ('currentassets', models.IntegerField(null=True)),
                ('accumulateddepreciationimpairmentpropertyplantequipment', models.IntegerField(null=True)),
                ('propertyplantequipmentgrosscost', models.IntegerField(null=True)),
                ('debtors', models.IntegerField(null=True)),
                ('averagenumberemployeesduringperiod', models.IntegerField(null=True)),
                ('cashbankonhand', models.IntegerField(null=True)),
                ('fixedassets', models.IntegerField(null=True)),
                ('othercreditors', models.IntegerField(null=True)),
                ('increasefromdepreciationchargeforyearpropertyplantequipment', models.IntegerField(null=True)),
                ('otherdebtors', models.IntegerField(null=True)),
                ('tradedebtorstradereceivables', models.IntegerField(null=True)),
                ('tradecreditorstradepayables', models.IntegerField(null=True)),
                ('othertaxationsocialsecuritypayable', models.IntegerField(null=True)),
                ('calledupsharecapitalnotpaidnotexpressedascurrentasset', models.IntegerField(null=True)),
                ('parvalueshare', models.IntegerField(null=True)),
                ('provisionsforliabilitiesbalancesheetsubtotal', models.IntegerField(null=True)),
                ('totalinventories', models.IntegerField(null=True)),
                ('totaladdsinclfrmbusincombopropertyplantequipment', models.IntegerField(null=True)),
                ('corporationtaxpayable', models.IntegerField(null=True)),
                ('accruedliabilitiesnotexpressedwithincreditorssubtotal', models.IntegerField(null=True)),
                ('numbersharesallotted', models.IntegerField(null=True)),
                ('amountspecificadvanceorcreditdirectors', models.IntegerField(null=True)),
                ('prepaymentsaccruedincomenotexpressedwithincurrentassetsubtotal', models.IntegerField(null=True)),
                ('intangibleassets', models.IntegerField(null=True)),
                ('bankborrowingsoverdrafts', models.IntegerField(null=True)),
                ('numbersharesissuedfullypaid', models.IntegerField(null=True)),
                ('additionsotherthanthrubusincombospropertyplantequipment', models.IntegerField(null=True)),
                ('accruedliabilitiesdeferredincome', models.IntegerField(null=True)),
                ('financeleaseliabilitiespresentvaluetotal', models.IntegerField(null=True)),
                ('taxationsocialsecuritypayable', models.IntegerField(null=True)),
                ('profitloss', models.IntegerField(null=True)),
                ('accumulatedamortisationimpairmentintangibleassets', models.IntegerField(null=True)),
                ('disposalspropertyplantequipment', models.IntegerField(null=True)),
                ('intangibleassetsgrosscost', models.IntegerField(null=True)),
                ('accruedliabilities', models.IntegerField(null=True)),
                ('amountspecificadvanceorcreditrepaidinperioddirectors', models.IntegerField(null=True)),
                ('disposalsdecreaseindepreciationimpairmentpropertyplantequipment', models.IntegerField(null=True)),
                ('amountspecificadvanceorcreditmadeinperioddirectors', models.IntegerField(null=True)),
                ('advancescreditsdirectors', models.IntegerField(null=True)),
                ('futureminimumleasepaymentsundernon', models.IntegerField(null=True)),
                ('investmentproperty', models.IntegerField(null=True)),
                ('investmentsfixedassets', models.IntegerField(null=True)),
                ('prepaymentsaccruedincome', models.IntegerField(null=True)),
                ('taxationincludingdeferredtaxationbalancesheetsubtotal', models.IntegerField(null=True)),
                ('totalborrowings', models.IntegerField(null=True)),
                ('amountsowedtodirectors', models.IntegerField(null=True)),
                ('bankborrowings', models.IntegerField(null=True)),
                ('taxtaxcreditonprofitorlossonordinaryactivities', models.IntegerField(null=True)),
                ('turnoverrevenue', models.IntegerField(null=True)),
                ('depreciationrateusedforpropertyplantequipment', models.IntegerField(null=True)),
                ('dividendspaid', models.IntegerField(null=True)),
                ('advancescreditsmadeinperioddirectors', models.IntegerField(null=True)),
                ('prepayments', models.IntegerField(null=True)),
                ('increasefromamortisationchargeforyearintangibleassets', models.IntegerField(null=True)),
                ('otherdisposalspropertyplantequipment', models.IntegerField(null=True)),
                ('deferredincome', models.IntegerField(null=True)),
                ('otherdspsalsdcrseindeprecimprmentprprtyplantequipment', models.IntegerField(null=True)),
                ('administrationsupportaveragenumberemployees', models.IntegerField(null=True)),
                ('amountsowedtogroupundertakings', models.IntegerField(null=True)),
                ('loansfromdirectors', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('deferredtaxliabilities', models.IntegerField(null=True)),
                ('otherremainingborrowings', models.IntegerField(null=True)),
                ('investmentpropertyfairvaluemodel', models.IntegerField(null=True)),
                ('provisions', models.IntegerField(null=True)),
                ('comprehensiveincomeexpense', models.IntegerField(null=True)),
                ('financeleasepaymentsowingminimumgross', models.IntegerField(null=True)),
                ('bankoverdrafts', models.IntegerField(null=True)),
                ('otherinvestmentsotherthanloans', models.IntegerField(null=True)),
                ('nominalvalueallottedsharecapital', models.IntegerField(null=True)),
                ('otheroperatingexpensesformat2', models.IntegerField(null=True)),
                ('investmentsingroupundertakings', models.IntegerField(null=True)),
                ('advancescreditsrepaidinperioddirectors', models.IntegerField(null=True)),
                ('staffcostsemployeebenefitsexpense', models.IntegerField(null=True)),
                ('profitlossonordinaryactivitiesbeforetax', models.IntegerField(null=True)),
                ('accdepnotincludimpairmentpropertyplantequipment', models.IntegerField(null=True)),
                ('amountsowedbygroupundertakings', models.IntegerField(null=True)),
                ('recoverablevalue', models.IntegerField(null=True)),
                ('amountsowedbyrelatedparties', models.IntegerField(null=True)),
                ('rawmaterialsconsumablesused', models.IntegerField(null=True)),
                ('netdeferredtaxliabilityasset', models.IntegerField(null=True)),
                ('corporationtaxrecoverable', models.IntegerField(null=True)),
                ('furtheritemcreditorscomponenttotalcreditors', models.IntegerField(null=True)),
                ('calledupsharecapitalnotpaid', models.IntegerField(null=True)),
                ('administrativeexpenses', models.IntegerField(null=True)),
                ('workinprogress', models.IntegerField(null=True)),
                ('operatingprofitloss', models.IntegerField(null=True)),
                ('grossprofitloss', models.IntegerField(null=True)),
                ('depreciationamortisationimpairmentexpense', models.IntegerField(null=True)),
                ('otheroperatingincomeformat2', models.IntegerField(null=True)),
                ('netassetsliabilitiesincludingpensionassetliability', models.IntegerField(null=True)),
                ('cashbankinhand', models.IntegerField(null=True)),
                ('currenttaxforperiod', models.IntegerField(null=True)),
                ('currentassetinvestments', models.IntegerField(null=True)),
                ('finishedgoodsgoodsforresale', models.IntegerField(null=True)),
                ('dividendspaidonshares', models.IntegerField(null=True)),
                ('directorremuneration', models.IntegerField(null=True)),
                ('shareholderfunds', models.IntegerField(null=True)),
                ('merchandise', models.IntegerField(null=True)),
                ('investments', models.IntegerField(null=True)),
                ('costsales', models.IntegerField(null=True)),
                ('sharecapitalallottedcalleduppaid', models.IntegerField(null=True)),
                ('otherinventories', models.IntegerField(null=True)),
                ('issueequityinstruments', models.IntegerField(null=True)),
                ('cashcashequivalents', models.IntegerField(null=True)),
                ('investmentsinsubsidiaries', models.IntegerField(null=True)),
                ('interestpayablesimilarchargesfinancecosts', models.IntegerField(null=True)),
                ('charityfunds', models.IntegerField(null=True)),
                ('salesmarketingdistributionaveragenumberemployees', models.IntegerField(null=True)),
                ('totalincreasedecreasefromrevaluationspropertyplantequipment', models.IntegerField(null=True)),
                ('otherinterestreceivablesimilarincomefinanceincome', models.IntegerField(null=True)),
                ('incomeexpenserecogniseddirectlyinequity', models.IntegerField(null=True)),
                ('depreciationexpensepropertyplantequipment', models.IntegerField(null=True)),
                ('furtherdepitemavgnoemployeescomponentaveragenumberlist', models.IntegerField(null=True)),
                ('incdecrinntdeftxlbilityfrmamountrecognisedinprfitorlss', models.IntegerField(null=True)),
                ('amountsrecoverableoncontracts', models.IntegerField(null=True)),
                ('furtheritemdebtorscomponenttotaldebtors', models.IntegerField(null=True)),
                ('rawmaterials', models.IntegerField(null=True)),
                ('finishedgoods', models.IntegerField(null=True)),
                ('amountsowedtogroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('incrsedcrseduetotrnsfrsbtwnclassespropertyplantequipment', models.IntegerField(null=True)),
                ('financialassets', models.IntegerField(null=True)),
                ('distributioncosts', models.IntegerField(null=True)),
                ('deferredtaxassetdebtors', models.IntegerField(null=True)),
                ('amountsowedtorelatedparties', models.IntegerField(null=True)),
                ('rawmaterialsconsumables', models.IntegerField(null=True)),
                ('totaladditionsincludingfrombusinesscombinationsintangibleassets', models.IntegerField(null=True)),
                ('percentageclassshareheldinsubsidiary', models.IntegerField(null=True)),
                ('balancesamountsowedtorelatedparties', models.IntegerField(null=True)),
                ('addsotherthanthrubusincombosinvstmntproprtyfairvaluemodel', models.IntegerField(null=True)),
                ('additionalprovisionsincreasefromnewprovisionsrecognised', models.IntegerField(null=True)),
                ('furtheritemtaxincreasedecreasecomponentadjustingitems', models.IntegerField(null=True)),
                ('deftaxexpensecreditrelatingtoorigintionreversltimingdiffs', models.IntegerField(null=True)),
                ('dividendpersharefinal', models.IntegerField(null=True)),
                ('costcharitableactivity', models.IntegerField(null=True)),
                ('totalliabilities', models.IntegerField(null=True)),
                ('totalassets', models.IntegerField(null=True)),
                ('otherpayablesaccruedexpenses', models.IntegerField(null=True)),
                ('increasedecreaseinpropertyplantequipment', models.IntegerField(null=True)),
                ('donationslegacies', models.IntegerField(null=True)),
                ('finaldividendspaid', models.IntegerField(null=True)),
                ('increasedecreaseindepreciationimpairmentpropertyplantequipment', models.IntegerField(null=True)),
                ('auditfeesexpenses', models.IntegerField(null=True)),
                ('amountsowedbygroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('taxexpensecreditapplicabletaxrate', models.IntegerField(null=True)),
                ('netincomexpndbeftrnsfrsbtwnfndsotherrcognisedgainslsses', models.IntegerField(null=True)),
                ('increasedecreaseincurrenttaxfromadjustmentforpriorperiods', models.IntegerField(null=True)),
                ('additionsotherthanthroughbusinesscombinationsintangibleassets', models.IntegerField(null=True)),
                ('capitalemployed', models.IntegerField(null=True)),
                ('calledupsharecapital', models.IntegerField(null=True)),
                ('otheroperatingincomeformat1', models.IntegerField(null=True)),
                ('incomeendowments', models.IntegerField(null=True)),
                ('expenditure', models.IntegerField(null=True)),
                ('costsraisingfunds', models.IntegerField(null=True)),
                ('totalcurrenttaxexpensecredit', models.IntegerField(null=True)),
                ('dividendpershareinterim', models.IntegerField(null=True)),
                ('crryingamntundercostmodelrevaluedassetspropertyplantequipment', models.IntegerField(null=True)),
                ('calledupsharecapitalnot', models.IntegerField(null=True)),
                ('addprovincreasefromnewprovrecognisedinprofitorloss', models.IntegerField(null=True)),
                ('dividenddeclaredpayable', models.IntegerField(null=True)),
                ('capitalcommitments', models.IntegerField(null=True)),
                ('wagessalaries', models.IntegerField(null=True)),
                ('paymentstorelatedparties', models.IntegerField(null=True)),
                ('nominalvaluesharesissuedspecificshareissue', models.IntegerField(null=True)),
                ('investmentincome', models.IntegerField(null=True)),
                ('interimdividendspaid', models.IntegerField(null=True)),
                ('frthritemincdecrinequitytotalincomxpnsercognseddirctlyinquity', models.IntegerField(null=True)),
                ('amountsowedbyassociates', models.IntegerField(null=True)),
                ('socialsecuritycosts', models.IntegerField(null=True)),
                ('paymentsreceivedonaccount', models.IntegerField(null=True)),
                ('incomefromothertradingactivities', models.IntegerField(null=True)),
                ('incomefromcharitableactivity', models.IntegerField(null=True)),
                ('disposalsinvestmentpropertyfairvaluemodel', models.IntegerField(null=True)),
                ('disposalsintangibleassets', models.IntegerField(null=True)),
                ('pensionotherpost', models.IntegerField(null=True)),
                ('dividendspaidonsharesinterim', models.IntegerField(null=True)),
                ('disposalsdecreaseinamortisationimpairmentintangibleassets', models.IntegerField(null=True)),
                ('transferstofromretainedearningsincreasedecreaseinequity', models.IntegerField(null=True)),
                ('profitlossonordinaryactivitiesaftertax', models.IntegerField(null=True)),
                ('otherincrsedecrseindeptionimprmentprprtyplantequipment', models.IntegerField(null=True)),
                ('numbersharesissuedspecificshareissue', models.IntegerField(null=True)),
                ('numbersharesissuedbutnotfullypaid', models.IntegerField(null=True)),
                ('incomefromrelatedparties', models.IntegerField(null=True)),
                ('amortisationrateusedforintangibleassets', models.IntegerField(null=True)),
                ('transfersbetwnppeclassesincreasedecrindeprimpairment', models.IntegerField(null=True)),
                ('gnlssonrvltionprpertyplnteqpmentbfortxinothrcomprehincme', models.IntegerField(null=True)),
                ('gainlossonremeasurementdfndbnftplnsbfrtxinothrcomprehincome', models.IntegerField(null=True)),
                ('deferredtaxassets', models.IntegerField(null=True)),
                ('carryingamountpropertyplantequipmentwithrestrictedtitle', models.IntegerField(null=True)),
                ('balancesamountsowedbyrelatedparties', models.IntegerField(null=True)),
                ('applicabletaxrate', models.IntegerField(null=True)),
                ('keymanagementpersonnelcompensationtotal', models.IntegerField(null=True)),
                ('incrsdcseindeftxlbilityfromamountrecognisedinprofitorloss', models.IntegerField(null=True)),
                ('financialliabilities', models.IntegerField(null=True)),
                ('totaloperatingleasepayments', models.IntegerField(null=True)),
                ('productionaveragenumberemployees', models.IntegerField(null=True)),
                ('numberdirectorsaccruingbenefitsundermoneypurchasescheme', models.IntegerField(null=True)),
                ('loansowedtorelatedparties', models.IntegerField(null=True)),
                ('increasedecreasefromfrvaluadjstmntinvstmntprprtyfrvluemdel', models.IntegerField(null=True)),
                ('amountsowedtootherrelatedpartiesotherthandirectors', models.IntegerField(null=True)),
                ('amountsowedbydirectors', models.IntegerField(null=True)),
                ('accumulatedamortisationnotincludingimpairmentintangibleassets', models.IntegerField(null=True)),
                ('unpaidcontributionstopensionschemes', models.IntegerField(null=True)),
                ('interestincomeonbankdeposits', models.IntegerField(null=True)),
                ('incometaxexpensecreditoncomponentsothercomprehensiveincome', models.IntegerField(null=True)),
                ('companycontributionstomoneypurchaseplansdirectors', models.IntegerField(null=True)),
                ('usefullifeintangibleassetsyears', models.IntegerField(null=True)),
                ('txincrdecrfromefectexpensesnotdctindeterintxableproforloss', models.IntegerField(null=True)),
                ('revenuefromsalegoods', models.IntegerField(null=True)),
                ('ownshares', models.IntegerField(null=True)),
                ('interestexpnsonobligtionsunderfinleasehirepurchcntrcts', models.IntegerField(null=True)),
                ('incomematerialfund', models.IntegerField(null=True)),
                ('governmentgrantspayable', models.IntegerField(null=True)),
                ('inothercomprehincomepretaxcmpntttlothercompincomepretax', models.IntegerField(null=True)),
                ('financialcommitmentsotherthancapitalcommitments', models.IntegerField(null=True)),
                ('expenditurematerialfund', models.IntegerField(null=True)),
                ('directorremunerationbenefitsincludingpaymentstothirdparties', models.IntegerField(null=True)),
                ('creditorsduewithinoneyear', models.IntegerField(null=True)),
                ('amountsowedbyassociatesjointventuresparticipatinginterests', models.IntegerField(null=True)),
                ('otherdeferredtaxexpensecredit', models.IntegerField(null=True)),
                ('netassetsliabilitiessubsidiaries', models.IntegerField(null=True)),
                ('issuebonussharesdecreaseincreaseinequity', models.IntegerField(null=True)),
                ('investmentsinjointventures', models.IntegerField(null=True)),
                ('investmentsingroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('gainlossondisposalspropertyplantequipment', models.IntegerField(null=True)),
                ('balanceswithbanks', models.IntegerField(null=True)),
                ('totaldeferredtaxexpensecredit', models.IntegerField(null=True)),
                ('taxincreasedecreasefromeffectcapitalallowancesdepreciation', models.IntegerField(null=True)),
                ('profitlosssubsidiaries', models.IntegerField(null=True)),
                ('pensioncostsdefinedcontributionplan', models.IntegerField(null=True)),
                ('othercurrentassetinvestmentsbalancesheetsubtotal', models.IntegerField(null=True)),
                ('numbersharesauthorised', models.IntegerField(null=True)),
                ('heritageassets', models.IntegerField(null=True)),
                ('gainlossduetoforeignexchangedifferencesrecognisedinprofitorloss', models.IntegerField(null=True)),
                ('furtheriteminterestexpensecomponenttotalinterestexpense', models.IntegerField(null=True)),
                ('itmincreasedecreaseininvestmentpropertyfrvalumodelcorrespttl', models.IntegerField(null=True)),
                ('gainlssinothercomprehincomenttxcmpnttotalothercomprencomenttx', models.IntegerField(null=True)),
                ('cumulativepreferencesharedividendsunpaid', models.IntegerField(null=True)),
                ('totalincreasedecreasefromrevaluationsintangibleassets', models.IntegerField(null=True)),
                ('otheroperatingincome', models.IntegerField(null=True)),
                ('otherloansclassifiedunderinvestments', models.IntegerField(null=True)),
                ('othercrditorsincltxtionscialsecurtyblncesheetsubtotal', models.IntegerField(null=True)),
                ('investmentsinsubsidiariesmeasuredfairvalue', models.IntegerField(null=True)),
                ('investmentsinassociates', models.IntegerField(null=True)),
                ('employeestotal', models.IntegerField(null=True)),
                ('decreaseinloansowedtorelatedpartiesduetoloansrepaid', models.IntegerField(null=True)),
                ('companycontributionstodefinedbenefitplansdirectors', models.IntegerField(null=True)),
                ('cashonhand', models.IntegerField(null=True)),
                ('weightedaverageexercisepriceequityinstrumentsoutstandingshare', models.IntegerField(null=True)),
                ('usefullifepropertyplantequipmentyears', models.IntegerField(null=True)),
                ('revlutionsincrsedecrseindprctionimprmntpropertyplnteqpmnt', models.IntegerField(null=True)),
                ('pensioncostsdefinedbenefitplan', models.IntegerField(null=True)),
                ('otherprovisionsbalancesheetsubtotal', models.IntegerField(null=True)),
                ('otherinterestincome', models.IntegerField(null=True)),
                ('otherinterestexpense', models.IntegerField(null=True)),
                ('otherincreasedecreaseinamortisationimpairmentintangibleassets', models.IntegerField(null=True)),
                ('otherdebtorsbalancesheetsubtotal', models.IntegerField(null=True)),
                ('othercomprehensiveincomeexpensebeforetax', models.IntegerField(null=True)),
                ('operatingleasepaymentsowing', models.IntegerField(null=True)),
                ('numberequityinstrumentsoutstandingshare', models.IntegerField(null=True)),
                ('numberemployeesdate', models.IntegerField(null=True)),
                ('netcashgeneratedfromoperations', models.IntegerField(null=True)),
                ('loanstogroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('loansowedbyrelatedparties', models.IntegerField(null=True)),
                ('interestexpenseonbankoverdraftsbankloanssimilarborrowings', models.IntegerField(null=True)),
                ('interestexpenseonbankoverdrafts', models.IntegerField(null=True)),
                ('interestexpenseonbankloanssimilarborrowings', models.IntegerField(null=True)),
                ('increasedecreaseduetotransfersbetweenclassesintangibleassets', models.IntegerField(null=True)),
                ('gainlossonrvaluationprprtyplnteqpmentnttxinthercmprehincme', models.IntegerField(null=True)),
                ('itmincmefrmothertrdingactvtiestotalmfrmothertradingactivities', models.IntegerField(null=True)),
                ('furtheritemdonationslegaciescomponenttotaldonationslegacies', models.IntegerField(null=True)),
                ('dividendspaidonsharesfinal', models.IntegerField(null=True)),
                ('depreciationamortisationexpense', models.IntegerField(null=True)),
                ('capitalisedborrowingcostsrelatedtopropertyplantequipment', models.IntegerField(null=True)),
                ('capitalreductiondecreaseinequity', models.IntegerField(null=True)),
                ('amountsowedbyotherrelatedpartiesotherthandirectors', models.IntegerField(null=True)),
                ('amortisationexpenseintangibleassets', models.IntegerField(null=True)),
                ('taxincreasedecreasearisingfromgrouprelieftaxreconciliation', models.IntegerField(null=True)),
                ('paymentsonaccountinventories', models.IntegerField(null=True)),
                ('ownershipinterestinsubsidiarypercent', models.IntegerField(null=True)),
                ('otherexpenditure', models.IntegerField(null=True)),
                ('numbersharesissuedinperiod', models.IntegerField(null=True)),
                ('nominalvaluesharesissuedinperiod', models.IntegerField(null=True)),
                ('interestexpenseonpreferencesharesclassifiedasdebt', models.IntegerField(null=True)),
                ('increaseinloansowedbyrelatedpartiesduetoloansadvanced', models.IntegerField(null=True)),
                ('increasedecreaseinstocksinventoriesfinishedgoodsworkinprogress', models.IntegerField(null=True)),
                ('increasedecreaseduetotransfersintooroutpropertyplantequipment', models.IntegerField(null=True)),
                ('transferstofromnon', models.IntegerField(null=True)),
                ('Trnsfrsintopropertyplantequipmentincrecrindeimprment', models.IntegerField(null=True)),
                ('taxationcomplianceservicesfees', models.IntegerField(null=True)),
                ('taxincreasedecreasefromothershort', models.IntegerField(null=True)),
                ('taxincreasedecreasefromeffectunrelievedtaxlossescarriedforward', models.IntegerField(null=True)),
                ('taxincreasedecreasefromeffectforeigntaxrates', models.IntegerField(null=True)),
                ('txincdecrfrmffctxpnssntddctiblefrtaxotherthngdwllamortimprmen', models.IntegerField(null=True)),
                ('txincrsdecrsefromffectadjstmntinresrchdevtaxcredit', models.IntegerField(null=True)),
                ('taxdecreaseincreasefromeffectrevenueexemptfromtaxation', models.IntegerField(null=True)),
                ('researchdevelopmentexpenserecognisedinprofitorloss', models.IntegerField(null=True)),
                ('researchdevelopmentaveragenumberemployees', models.IntegerField(null=True)),
                ('redeemablepreferencesharesliability', models.IntegerField(null=True)),
                ('purchasepropertyplantequipment', models.IntegerField(null=True)),
                ('profitlossattributabletoownersparent', models.IntegerField(null=True)),
                ('presentvaluefinanceleasereceivables', models.IntegerField(null=True)),
                ('percentageclassshareheldinjointventure', models.IntegerField(null=True)),
                ('pensionschemesprepayments', models.IntegerField(null=True)),
                ('paymentsfinanceleaseliabilitiesclassifiedasfinancingactivities', models.IntegerField(null=True)),
                ('outstandingpre', models.IntegerField(null=True)),
                ('othertaxationpayable', models.IntegerField(null=True)),
                ('othernon', models.IntegerField(null=True)),
                ('otherincreasedecreaseinnetdeferredtaxliability', models.IntegerField(null=True)),
                ('othergeneralgrants', models.IntegerField(null=True)),
                ('otherdisposalsinvestmentpropertyfairvaluemodel', models.IntegerField(null=True)),
                ('netinterestreceivedpaidclassifiedasinvestingactivities', models.IntegerField(null=True)),
                ('netfinanceincomecosts', models.IntegerField(null=True)),
                ('netcashflowsfromusedinoperatingactivities', models.IntegerField(null=True)),
                ('netcashflowsfromusedininvestingactivities', models.IntegerField(null=True)),
                ('netcashflowsfromusedinfinancingactivities', models.IntegerField(null=True)),
                ('loansfromgroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('liabilitiessecuredbyassets', models.IntegerField(null=True)),
                ('investmentsinassociatesjointventuresparticipatinginterests', models.IntegerField(null=True)),
                ('interestpaidclassifiedasoperatingactivities', models.IntegerField(null=True)),
                ('interestincomefromgroupundertakingsparticipatinginterests', models.IntegerField(null=True)),
                ('interestexpenseondebtsecuritiesinissueothersimilarloans', models.IntegerField(null=True)),
                ('increaseinloansowedtorelatedpartiesduetoloansadvanced', models.IntegerField(null=True)),
                ('increasedecreaseinprovisionsthroughtransfersreclassifications', models.IntegerField(null=True)),
                ('increasedecreaseinexistingprovisions', models.IntegerField(null=True)),
                ('incrdecrincashbeforeexchangedifferenceschangesinconsolidation', models.IntegerField(null=True)),
                ('incometaxespaidrefundclassifiedasoperatingactivities', models.IntegerField(null=True)),
                ('incomefromothertradingactivity', models.IntegerField(null=True)),
                ('incomefromcharitableactivities', models.IntegerField(null=True)),
                ('impairmentlosspropertyplantequipment', models.IntegerField(null=True)),
                ('giftaid', models.IntegerField(null=True)),
                ('gainlssonrvluationotherasstsnttxinothercmprehensveincome', models.IntegerField(null=True)),
                ('gainlossondisposalsothernon', models.IntegerField(null=True)),
                ('gainlossincashflowsfromchangeindebtorstradeotherreceivables', models.IntegerField(null=True)),
                ('gainlossincashflowsfromchangeincreditorstradeotherpayables', models.IntegerField(null=True)),
                ('futurefinancechargesonfinanceleases', models.IntegerField(null=True)),
                ('furtherrentalleasingincomeitemcomponenttotalrentalleasingincome', models.IntegerField(null=True)),
                ('furtheroperatingexpenseitemcomponenttotaloperatingexpenses', models.IntegerField(null=True)),
                ('itemoperatingxpnslossincmesttmntitemcomponentopratngproftlss', models.IntegerField(null=True)),
                ('fundraisingsupportcosts', models.IntegerField(null=True)),
                ('feesfornon', models.IntegerField(null=True)),
                ('donatedgoodsfacilitiesservices', models.IntegerField(null=True)),
                ('dividendsproposedbutnotpaid', models.IntegerField(null=True)),
                ('dividendspaidclassifiedasfinancingactivities', models.IntegerField(null=True)),
                ('dividendincomefromgroupundertakings', models.IntegerField(null=True)),
                ('deferredtaxexpensecreditrelatingtochangesintaxratesorlaws', models.IntegerField(null=True)),
                ('decreaseinloansowedbyrelatedpartiesduetoloansrepaid', models.IntegerField(null=True)),
                ('debenturesinissue', models.IntegerField(null=True)),
                ('currentliabilities', models.IntegerField(null=True)),
                ('considerationreceivedforsharesissuedspecificshareissue', models.IntegerField(null=True)),
                ('amountsowedtoparententities', models.IntegerField(null=True)),
                ('amountsowedtoassociatesjointventuresparticipatinginterests', models.IntegerField(null=True)),
                ('amountsowedtoassociates', models.IntegerField(null=True)),
                ('amountsowedbyjointventures', models.IntegerField(null=True)),
                ('amountpaidliabilityincurredinfulfillingguaranteesdirectors', models.IntegerField(null=True)),
                ('advancesoninvoicediscountingfacilities', models.IntegerField(null=True)),
                ('accruedincome', models.IntegerField(null=True)),
                ('weightedaverageexercisepriceequityinstrumentsforfeitedshare', models.IntegerField(null=True)),
                ('weightedaverageexercisepriceequityinstrumentsexpiredshare', models.IntegerField(null=True)),
                ('unusedprovisionreversed', models.IntegerField(null=True)),
                ('totaladditionsheritageassets', models.IntegerField(null=True)),
                ('taxincreasedecreasefromtransferpricingadjustments', models.IntegerField(null=True)),
                ('redemptionsharesdecreaseinequity', models.IntegerField(null=True)),
                ('provisionsused', models.IntegerField(null=True)),
                ('othertaxationadvisoryservicesfees', models.IntegerField(null=True)),
                ('otherexternalcharges', models.IntegerField(null=True)),
                ('othercurrenttaxexpense', models.IntegerField(null=True)),
                ('numberequityinstrumentsforfeitedshare', models.IntegerField(null=True)),
                ('numberequityinstrumentsexpiredshare', models.IntegerField(null=True)),
                ('investmentsinotherentitiesmeasuredfairvalue', models.IntegerField(null=True)),
                ('intrstexpnseonfinanciallbilitiesfrvluethruprftorlss', models.IntegerField(null=True)),
                ('governmentgrantincome', models.IntegerField(null=True)),
                ('gainlossfromfrvaluadjstmntinvstmentpropertyrecgnsedinprftlss', models.IntegerField(null=True)),
                ('dividendrecommendedbydirectors', models.IntegerField(null=True)),
                ('dividendpershareproposedbutnotpaid', models.IntegerField(null=True)),
                ('derivativeliabilities', models.IntegerField(null=True)),
                ('deferredtaxexpensecreditfromunrecognisedtaxlossorcredit', models.IntegerField(null=True)),
                ('companynumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Company')),
            ],
        ),
    ]
