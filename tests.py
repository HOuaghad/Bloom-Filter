from src.bloom_filter import BloomFilter
import csv

def print_success(message):
	print("\033[1m\033[0;32m %s \033[0m"  % message)

def print_failure(message):
	print("\033[1m\033[0;31m%s \033[0m"  % message)

def loadTop2MFile():
	items = []
	with open('./files/top2m.csv') as f: 
		r = csv.reader(f);
		for row in r:
			items.append(row[1])

	return items

def testFileCreation():
	path = './files/bands.bloom'
	try:
		BloomFilter(10, 0.00000001, path)
	except Exception as e:
		print_failure("Test failed with: %s" % str(e))
		raise e
	else:
		import os
		if os.path.exists(path):
			print_success("File created successfully")
		else:
			print_failure("Failed to crate file")

def testBasicBloomFilter():
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']

	filepath = './files/randomwords.bloom'
	
	bloomfilter = BloomFilter(len(items), 0.001, filepath)
	
	bloomfilter.add(items)

	nitems = ['Jackson', 'Inline', 'Whatever']

	ci = 0
	for i in items:
		if i in bloomfilter:
			print_success("Found in bloomfilter: %s" % i)
		else:
			ci += 1
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented missed\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements of bloomfilter are found\n\n")


	ci = 0
	for i in nitems:
		if i in bloomfilter:
			ci += 1
			print_success("Found in bloomfilter: %s" % i)
		else:
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented found\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements that are not in the bloomfilter weren't found\n\n")

def testBasicBloomFilterFile():
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']

	filepath = './files/randomwords.bloom'
	
	bloomfilter = BloomFilter(len(items), 0.001, filepath)

	nitems = ['Jackson', 'Inline', 'Whatever']

	ci = 0
	for i in items:
		if i in bloomfilter:
			print_success("Found in bloomfilter: %s" % i)
		else:
			ci += 1
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented missed\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements of bloomfilter are found\n\n")


	ci = 0
	for i in nitems:
		if i in bloomfilter:
			ci += 1
			print_success("Found in bloomfilter: %s" % i)
		else:
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented found\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements that are not in the bloomfilter weren't found\n\n")

def testOldBloomFilterFile():
	items = loadTop2MFile()

	bloomfilter = BloomFilter(len(items), 0.0001, './files/urls.bloom')

	bloomfilter.add(items)

	nitems = ["atapattu.net","exyu.info","sergioalbanese.it","leshopping.com.br","natura-naturans.de","footbuddies.com","sieuthimucin.net","kuma-bus.co.jp","biit.no","kndkmc.or.kr","flygo.net","0552.ua","tsukashin.com","sites.google.com/a/marist.com","ad-topia.com","wpgogo.com","meme-italia.it","centrostudihelios.it","lubimayaoptika.by","thewandergirls.com","vrapps.co","oksdf.com","whalesmall.co.kr","bankbazar.com","matthewsdiehl.com","videoplaylistgallery.com","bestmuseum.ru","it-site.net","taunigma.biz","cdcpederzoli.it","vikaskumrai.com","lodensoftware.com","barami.us","tilsonhome.com","proutene-kosiky.cz","rboots.ru","commercedc.com.my","energia.fi","budidayanews.blogspot.com","aghed.blogfa.com","petcareclinics.co.uk","simonpattonracing.com","alliebeth.com","powershop.jp","pismotechnic.com","sacramentocoaches.org","alloextra.com","book-of-ra-deluxe.de","beststyle.me","btr-k.ru","sceny-z-uzycia.blog.pl","my7sports.com","gazetaonline.in","vicensvives.es","etaal.gov.in","site-pedia.ro","sweatvac.com","camberleywebdesign.com","lettre-de-motivation-facile.com","importir.org","eapc.cat","smartdiesel.ro","onewideo.com","goodrelaxation.com","plasenta.com.tr","openfilepro.com","sempatiza.es","hljfood.net","stream2watch.eu","pointofreturn.com","certificadosprofesionalidad.com","pavementresources.com","daralab.com","businesstechnologyguide.com.au","sanostra.es","view-events.com","antiques-jp.com","starina-mebel.ru","chajian110.com","eyworkflow.com","keenitsolution.com","vitadomo.ch","kintek.com.au","theship.co.uk","mgs-subs.de","innovservers.com","kindersoaps.com","hotelpitangueiras.com.br","noweprzetargi.pl","notebooksapp.com","hrtrainingcenter.com","sunshinenigeria.com","x-sense.jp","agenciafosforo.com.br","topfriend.org","paranoidprintco.bigcartel.com","metropolitan.org.uk","jpi.at","fixplanta.net","i2office.co.uk","lisboatriathlon.com","just2craft.fr","downloaden.nl","epharmadeals.gr","bettd.com","fix.no","sumaprojektow.pl","atcloudspeakers.co.uk","fashionjudy.com","dshop.vn","tribesports.co.uk","trinityviaggistudio.it","encyclosights.com","dhg-marketing.de","xiayizhan.cn","gfxtra2.net/user/Orten","fetchrobotics.com","max-joomla.ru","lrt.ru","turk-diziler14.ir","eidos.ic.i.u-tokyo.ac.jp/~tau","liberacionprofesional.com","brainvoyager.com","sms2greece.com","mumok.at","usa.edu.co","it-nomikai.jp","lmls.org","corporatetrainerclub.com","kho.fi","miuu.de","chelles-creations.com","swimstyle.com","4options.pt","vod.blog.pl","woodsplitterdirect.com","ou.com","21bitcoingratis.com","tattoo-sprueche.de","igpublish.com","spreewald-unterkuenfte.de","sanluissa.cl","puppyleague.tumblr.com","staybcnapart.com","cpt.gov.vn","greenhex.net","dallastechnologies.in","powerwerks.com","santillana.com.uy","prozonemarketing.com","mybadges.com","readysettroll.com","prochoiceny.nationbuilder.com","factsfromfiction.blogspot.com","ktateb.com","inmueblesbanorte.com.mx","aliceinweddingland.co.uk","tvdsb.on.ca","reddit.com/user/amirarice","mafiamax.com","postgazetesi.com","inventorum.com","nonsologhiaccio.com","citejournal.org","facesculptormd.com","wtop.blogspot.com.au","elo-street.blogspot.co.uk","ebarticles.com","orexvideourok.ru","forexstrategy.com","othersdayquotesz.com","ebdesignhelper.co.uk","utterycolorfulkryptonite.tumblr.com","arandz.com","ighwoods.com","ajdirabota.mk","va.org.uk","ankrecruitment.co.in","acturacionlib-tol.com.mx","h3technician.com","otfreetraffic.net","onottouch.org","apenziraha.com","uytra.com","sc-lohfelden.de","lberni.ca","portaktiv.sk","ichcoffee.ru","ord-travel.com","rdineavvocatitreviso.it","upazena.com","log-transmission-entreprise.com","inoheld.de","ukouri.com","righttrac.com","heteachertoolkit.com","concepts-auto.com","awrencevilleweather.com","allouslab.net","hirazi.blogfa.com","60degree.blogsky.com","omeditorial.com","therside.su","androvercentre.com","olitape.ru","sservatoreseriale.it","lackjackround.com","freeworks.com","avenecommerce.com","-bike.co.uk","tntechnologies.in","stutesol.com","zoneclubs.com","ath.umn.edu/~olver","ncotexkkm.ru","hubbybody.com","kcthundernation.com","ostmap.com","ent-wifi.com","killdrick.co.uk","irtualeduca.org","piritualite2000.com","nvestingontrack.com","utsuzunhikayeleri.tumblr.com","kentoo.com","raycor.com","2volt.sk","ornogameonline.com","edicalyoga.in","evue-amateur.com","retaportobello.com","abernacleatl.com","en-mart.com","rzanic.com","ridgersteel.com","sgguncesi.com","lobemoving.net","utodoplnky-prodej.cz","35678.com","objscott.com","esource-auto.ru","exnokom.com","dainternet.com","ions-net.com","ostonmamas.com","ecolafacil.com.br","-daama.com","kis.org.hk","odrum-rentacar.com","zieu.pl","ookshopblog.com","on-dualitypress.org","lmedauniversity.org","achelwcole.com","omethingvalue.com","luczykarze.pl","asargrup.com","ousageguide.com","nexplainedstuff.com","alifa.org","reebtcd.org","anbu-city.com","uciemanet.fr","iwoyuen.com","ishes.dev","ilgiyuvasi1.info","xdcm.com","ppincomereport.com","hbs.in","ecure128.com","itpro.us","rl.com.tw","echgeeker.com","naptech.com","otalhorsechannel.com","vantisport.de","ictorfoo.com","ost5.ir","anouba-sugarfree.com","xpomuseum.com","oodvood.com","anzaniaonline-cn.org","cecat.tw","enteparaviajar.com","eadsplus.us","ertificadoecool.com.br","lp.co.jp","elesur.sr","stituto-besta.it","adioboxapp.com.br","nmaya0001.tumblr.com","onnectedfamilies.org","etzaehler.de","espreslaporte.com","remierescene.net","obileaff.mobi","eddingcollectibles.com","ngular.dev","huo-hot.com","repaidstart.com","n--b1agviax.xn--p1ai","mooozesh.ir","elun.com"]

	ci = 0
	for i in items:
		if not (i in bloomfilter): # remove not if you want to use the prints
			ci += 1

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented missed\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements of bloomfilter are found\n\n")

	ci = []
	for i in nitems:
		if not i in bloomfilter:
			ci.append(i)

	print(ci)
	print_success("%d element are not malicious ouf of %d, and they are printed above" % (len(ci), len(items)))
	# print(bloomfilter.bit_array)

if __name__ == "__main__":

	print("\033[1mTest file creation:\n\n \033[0m")
	testFileCreation()

	print("\n\n\033[1mTest Bloom Filter:\n\n \033[0m")
	testBasicBloomFilter()

	print("\n\n\033[1mTest Bloom Filter:\n\n \033[0m")
	testBasicBloomFilterFile()

	print("\n\n\033[1mTest old bloom filter file:\n\n \033[0m")
	testOldBloomFilterFile()
