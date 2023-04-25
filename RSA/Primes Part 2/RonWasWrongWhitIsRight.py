from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

e = 6553
n = 911155430397089868893710399679843124299455958854629791471074639340378853507919464565810613293797452094094419935791316019378845266444423939069591777393674738696600039645897332187483027169161226989463007958162660511833293293934680580795884835915313555665028500273978111975141483711972416976051841007136079560842930618009244952633494357039685233438172831394231820157810045590724112193897315806153435024753655632608473402805617714869872186030635147363770587791422138471720933891531786826222624075389616924907447441888709731985493341989380909384044148308972895318737298279201161927233884653041034925026221365261861897721220653242120761984486476073104852961087732061243614950426772704615616351403821143864605052161365099625909493963610940101256661638103038287477307037516480655622483809303973844914111675448758165915304217110383740650242709810054890529380273089938565187583433898011098193322584247150816917331201462582657698512259466266467891678088041219884140157617779080424490085443389141752344203813840060106563190054773064792934495477729541544277637486134526425276923313072437402635187015371607927851364757573804279682763676084186465911588299208965058610144991287224616962493760669148885986144273990509506917829875014575681080262558165579783076765660193031162935128415991494869107015989320398687972326200569107240071210145877231390571616043489752316478596708456751559975181688088516026334899322294703865900392081637370670610001746419748464485461186336107253585654909405811415364943187972977795714207432456907751605269930478002755232084922463849167034964311000757003822836396625765900984940363082552313118484509184504317922624334876645052025073648609570099819847985458003040099734106611690135903402566586049952555685885129167949699135190659447558932337919259697368802685025241864769010304936839822392261403853930937011037322345944122791531705024153346939404340299053282463816135162799746979069053739021760882877630867181836643699922817756581868559378190317154945587598406935787422788156408738900082828687918258191147242549110812512887371014023446801086634829279768440364090252588453227384663956539541609351183298197012676011524752900153903629441235349425281050546200540159001545754825292288245399374715709620586639621734512134963505768992518699532365136633077433424884644404975480104687269688186070343890063473871474522626591333445128238108321171232365531356095520991346873717177021044283092373174179512606967225038176778565236701000826596381944707372969518852801195663
p = 919031168254299342928662994540730760042229248845820491699169870943314884504551963184014786520812939038906152950817942941469675496074887272906954399256046690838233813273902630076899906873722574023918253104149453601408405078374008695616160025877687382663027910687942091698042309812910101246025081363544171351624307177908410700904833438480012985928358897861427063761678614898919524867442676631453135379994570031284289815099294504127712924001149921480778993635917803466637717023744788311275545126346774536416864472035644211758788016642401235014385037912224180351022196262011724157012443048941426178651665266181311662824205620324073087330858064769424755443807165558567191049013947419763315902476674266627953223373671797370373786249718677582213173537848582863398367624397247597103174897140005790273296171101569756006898658668311846034013183862374297777882433967015111727139360441681664840944403450472574336901043555319067050153928231938431298082827397506406624964952344826628463723499263165279281720105570577138817805451223334196017505528543229067732013216932022575286870744622250293712218581458417969597311485156075637589299870500738770767213366940656708757081771498126771190548298648709527029056697749965377697006723247968508680596118923
q = 991430390905926023965735525726256769345153760248048478891327804533279477721590201738061124861790305326884541900044434890157058142414306020739922709698601329762087825767461256626800629782378634339618941488765491437487541851308806651586976069659042714378353883168031522106709494592827914376213512564492771821921367377484213072867988877925314809325159382342584541006645302760204539354879391605736604946702073863673524002591877977949645618863730441482821840664748508050205004505250025193611888170440612737112479006348533153568103452396596042639466753099280111709882461562564978070397786887446291916733276692400981917025361391646188802038772976331121474570242334921390569285834250256522656433623912544555266998750630136756355560927237594975904642791712318215315246754105993145827690531584325461597482035600919501967088106457091199733024323755210212616553447076697617349235377466327471959683763796707566328536834402308887105044128592177681553611608618850780128709949316259039664054913946726480968288231015999572777436469163437066403964134928735809253108394078092917006632332098357725950865697047565284013456253933234017983509582245874130968218422573483012858388392588302838940565560162598810462310034964473576147200222580784694005333482381
c = 0xc62d91677825632cb8ac9d2fbee7490fca70b3f067bd8d811fa446a21001de7943cacafc429b2513d3f20c3224d212ca2937a4a4ea10792a1c498b791e978e4b050b525576bc68421e40d9f420c0b8a07778daf69edf2095bf48222896bb2d6581288ce7a2e7aec15a88a440ff1a1e48beb56f68b4f860d1f64a6ec8cafed90846b7d893bc482df69c8478d5a0d6fc2d043cdd97178740a9eb59d2576b5136200c8ea77e648c88e6c5104ca5d0c6add2fc2c8569ce909f8461e7fa3d901fe67eaeff656399d4751fedba9973e246427e0c7a217f5bdc3edcb5033f17b5ef53419e340355a809eb46f48f538e880abd6f72212b02d3dbf2c4f633a503e648d1a835c4574b23e329e1c51078ea7cbb7533e771899498d4a5760bc0799b7e046f268f098fe0b57de47cd70ccf01ad3c9daec5027f306141bfe7a6c0bd29ee6caf94c7433c25e34ee974005e2360337cb6b3cec5eaf5d31d19f01435f4cdcaa455a18e78dee078395b8ad14b9c3a0d817dc1e3109c7b8af35ab3a5950bf47d5e621f9373ef421540052aac307ecea91f9c29c14bfd81b41d4c5a9b34a8ec2fa1ae06c3d881f39286c3d8dbb1849602fecc27bb135f7dd443e2598d247d1182d350b04be1ac0a734cb0e852a36902d88066ac375a35e279b126e413a97aaa35a0ba933f7b8d574c298332ce428c181464b240709a414af1b77103441b6ccfd0790eccea5926844054903c83f4cb415d600a6b7bc771c9e7a86394a2b427ebe8edec08b8095f561827716898e11caf6f0fe562af8a69f7b6469f0e86bdcc32f429f10821c763b34307efc5b2ae7fd524a07e5d0b762c096f025a3f240fb7bd3554582dcce32c175867d93970b0422e17870ec58f2a305545a3d284b3abb2d21a45ad8fd5faed0dc66312a5aa2f994606a51cd6682acd48ea3fb883f0611e1e5c2fb4047b5c80815ba5d3bcfefaf121bfde4d5c91ee27bb899ef0d29fa5c6dc4223ac2bfcff0217d08579a13e9b02dc97aa2622df62eeaaa38bb3bd087cdd209f03e8926a951e90eaa0f678a252a067ac66402a4c85865931689ed3b33f9f6de0c499f140ef508dfba6007a607a271dcbec18a61f7488bba34d143f93bc259310ffbf23f3391734d8d8811a4be8abf6382e55c2ccbfd80b1559d907fd8d46e0431cdbcd8fdb06d57973437f7b8ff5efc5a53c80d552e8fe622971f7376eeea35f4df9b32ada93e531a52b63ba13f6b7bf61ab337d6d93feb0e8c8a309dfa7e5f50e8cf9655b73ae64822b50db5312f35f4718b0668305065ea283ddf8f0a4e8f486ee9d119ebc584be1837b3d959a25ace208ffac2fb703390a72d3027b64fdd1955b513c0403f09232efa1794a277e0be3f4f9f3a6fd23c6e52101e723cef5db7a2a18a107cd522379adb40c5ed36b26cdf53a1000d7d576f1157b42aac3d3ee011275

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

print(cipher.decrypt(bytes.fromhex(hex(c)[2:])).decode())
