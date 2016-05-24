Helo, Geraint ydw i. Rwy'n fyfyriwr PhD yng Nghaerdydd, a fyddaf yn siarad am darn o waith yn deilo gyda llwyrgo yn rhwydweithiau ciwio.

---

Yn gyntaf, beth yw llwyrglo (deadlock)? Mae'r diagram yma yn dangos un fath of lwyrglo, sef gridlock, neu tagfa traffig. Gwelwn fod y ceir gwyrdd wedi'i flocio rhag parahau gyda'i taith oherwydd y ceir coch; sy wedi'i flocio gan yh ceir glas; sy wedi'i flocio gan y ceir melyn; sy wedi'i flocio gan y ceir gwyrdd. Felly mae'r ceir gwyrdd yn flocio'i hun yn anuniongyrchol, ac yn aros nes i'w hunain symyd er mwyn iddynt symyd.

---

Beth am ciwio?
Rydym ni yn siarad am pobl yn sefyll mewn rhes, yn aros am rhyw fath o wasanaeth.
Pam y mae'n bwysig astudio ac optimeiddio ciwiau?
Wel, dychmygwch bod gennych busnes dros ffon lle mae cwsmeriaid yn aros 'on hold' nes bod ar flaen y ciw. Mae cadw llawer o gwsmeriaid ar y ffon yn gostus i'r busnes, ac hefyd gallwch colli cwsmeriaid trwy ei cadw'n aros ar y ffon.
Beth am trio optimeiddio ciwiau yn systemau iechyd lle mae amseroedd aros hir yn gallu rhoi cleifion mewn peryg?

---

Yn y gwaith yma disgrifiwn ciw fel y system a ddangoswyd: mae cwsmeriaid yn cyrraedd 'ar hap' gyda cyfradd Lambda, yn ymuno a ciw, aros nes iddynt fod ar blaen y ciw, yna yn gwario rhyw fath o amser mewn gawasaneth cyn gadael y system.

Mae'r amseroedd gwasanaeth, ac amseroedd rhwng pob cwsmer yn cyrraedd yn stochastic, ar hap, ond yn dod o dosraniad penodol.

---

I ddangos beth dwi'n golygu gan hwn, mae ameroedd yn cael eu ddewis ar hap o dosraniad Lognormal fan hyn. Wrth i'r histogram adaeladau, gwelwn fod y dosraniad yn cael ei creu.

Ar gyfer y gwaith yma tybiwn dosraniadau Esbonyddol yn unig.

---

Mewn rhwydwaith o ciwiau, unwaith i cwsmer gorffen wasanaeth mae yna tebygolrwydd  o naill ai ymuno o'r ciw eto, ymuno o ciw arall, neu gadael y system.

Yn rhwydweithiau rhwystredig, mae ond lle ar gyfer n cwsmer i aros. Os yw'r ciw yn llawn, a mae cwsmer moin cyrraedd o'r tu allan, mae'r cwsmer yn cael ei colli. Os yw cwsmer yn trio ymuno a ciw llawn ar ol gorffen gwasanaeth, mae'r cwsmer yn cael ei flocio nes bod lle yn y ciw. Yn ystod y cyfnod o flocio yma, ni all unrhyw cwsmer arall dechrau gwasanaeth gyda'r gweinydd yna.

---

Mae'r rheolau blocio yma, mewn rhwydweithiau gyda cylchredau, yn gallu achosi'r ffenomenon llwyrglo, fel y dangosir. Mae'r cwsmer yn A1 yn aros i'r cwsmer yn B1 symyd, ond ni all B1 symud heb i A1 symyd.

Mae'r gwaith yma yn edrych ar sur allwn canfod pryd mae cyflwr llwyrglo yn digwydd mewn efelychiadau o systemau ciwio, ac hefyd yn adaeladu modelau Markov o rhwydeithiau ciwio sy'n cyrraedd llwyrglo, an yn edrych ar yr amser cymedrig nes cyrraedd llwyrglo.

---

I canfod llwyrglo, defnyddir graff cyflwr.

Ar y chwith mae rhwydwaith ciwio 3 nod llawn, gyda pob gweinydd yn nghanol gwasanaeth.
Ar y dde mae graff cyflwr y system: mae fertigau yn cyfateb a gweinyddion, a mae ymyl cyfeiriedig rhwng fertigau yn dynodi perthynas blocio rhwng y ddau gweinydd cyfatebol.

Fel enghraifft, mae'r cwsmer yn weinydd B1 yn cael ei blocio i'r nod top; nawr mae yna ymyl o fertig B1 i bob fertig sy'n cyfateb i weinydd yn y nod top.

Mae'r cwsmer yn weinydd C1 yn cael ei flocio i'r nod canol; mar yna ymyl o fertig C1 i bob fertig sy'n cyfateb i pob weinydd yn y nod canol.

Mae'r cwsmer yn A1 yn cael ei flocio;

A'r cwsmer yn B2 yn cael ei flocio.

Fe allwn weld fod y nod top a canol mewn cyflwr llwyrglo. Dangosir y llwyrglo yma gan cwlwm (knot) yn y graff cyflwr. Hynny yw, set o fertigau ni allwch ddianc ohonynt trwy trafeilu'r ymylon.

Mae'r dechneg yma o canfod llwyrglo wedi'i cynnwys yn y llyfrgell elefychu ciwio yn Python, lle allwch recordio'r amser o system gwag nes cyrraedd llwyrglo.

Nesaf, adaeladwn modelau Markov o rhai rhwydeweithiau ciwio sy'n cyrraedd llwyrglo; cyfrifo'r amser nes cyrraedd llwyrglo yn analytig, ac yna cymharu gyda canlyniadau'r efelychiad.

---

Ystyriwch y system un nod hon: Mae cwsmeriaid yn cyrraedd ar gyfradd Lambda ac yn cael ei weinu ar gyfradd mu. Mae c weinydd parallel i'w gael, ar ol wasanaeth mae tebygolrwydd r11 o ail-ymuno a'r ciw. Ond lle i n cwsmer i ciwio sydd.

Diffinir cyflwr y system gan i, y nifer o cwsmeriaid yn y system y nifer o cwsmeriaid wedi'i flocio.

Fe allwn ysgrifennu'r lle cyflwr fel hyn; a diffiniwn delta fel y gwahaniaeth rhwng dau cyflwr.

---

Yna allwn ysgrifennu lawr yr holl cyfraddau o drosglwyddo rhwng cyflyrau.

---

Dangosir y cadwyn Markov, o system gwag, un cwsmer yn y system, ... nes llwyrglo.
Gweler fod llwyrglo yn "absorbing state", cyflwr ni allet ddianc. Mae hyn yn dweud wrthyn fod unrhyw rhwydwaith ciwio sydd a'r potensial i cyrraedd llwyrglo yn pendant mynd i cyrraedd llwyrgo mewn digon o amser.
Hefyd mae dechnegau algebra llinol yn gadael i ni ffeindio'r amser cymedrig nes cyrraedd llwyrglo.

---

Felly cymharwn ni'r dull analytig yma (mewn gwyrdd) gyda chanlyniadau'r efelychiad (yn oren) o'r amser nes cyrraedd llwyrglo; a edrych ar effaith rhai paramedrau;r system. A welwn rhai pethau amlwg:

* Wrth i'r cyfradd dyfodi cynyddu, mae'r amser ne llwyrglo yn lleihau - mae'r system yn cael ei llenwi'n gyflymach
* Wrth i'r cynhwysedd ciwio, a nifer o weinyddwir cynyddu, mae'r amser nes llwyrglo cynyddu - Mae mwy o le i gwsmeriaid aros cyn i'r system llenwi

Ond hefyd welwn rhywbeth oni ddim yn disgwyl, wrth i'r cyfradd gwasanaeth cynyddu gwelwn siap bowlen yma.
Pam?
Mae cynyddu cyfradd gwasanaeth yn cyfri tuag at cael gwared a cwsmeriaid o'r system ac hefyd cyfri tuag at cwsmeriaid yn ail-ymuno a'r system. Mae yna rhyw fath o trobwynt lle mae effaith un yn fwy nag effaith y llall.

---

Gwnaethon ni'r un peth gyda'r system dau nod canlynol:

---

Ysgrifenwn ni lawr y cyfradd trosglwyddiadau:

---

I cael y cadwyn Markov yma. Noder y cyflwr llwyrglo fan hyn, yr "absorbing state".

---

A welwn ymddygiad tebyg wrth amrywio'r paramedrau.

---

Yna edrychon ni ar y system yma. Gwelwn nawr fod yna tri cylchred i'r rhwydwaith: felly tri gwahanol fath o llwyrglo: y top wedi'i flocio i'w hun, y gwaelod wedi;i flocio i'w hun, a'r ddau wedi'i flocio i'w gilydd. Felly mae yna nawr tri cyflwr llwyrglo gwahanol.

Noder hefyd ond un weinydd sydd yn y nodau yma. Oherwydd y ffordd o dynodi'r cyfyrau, no allyn modelu'r system yma gyda mwy nag un weinydd yn yr un modd ac o'r blaen. Gyda mwy nag un weinydd mae nifer o cyflyrau yn cynyddu'n cyfuniadol.

---

Ysgrifennon ni lawr y cyfraddau trosglwyddo:

--

I cael y cadwyn Markov yma. Mae'r tri cyflwr llwyrglo nawr yn tri "absorbing state" ei hun. Nawr mae'r amser nes llwyrglo yn golygu'r amser nes cyrraedd unrhyw un o'r tri cyflwr yma.

---

A welwn ymddygiad tebyg, heblaw am wrth cynyddu'r cynhwysedd ciwio, lle mae'r amser nes llwyrglo yn dechrau dod yn wastad.
Pam?

Cofia'r tri cylchred, a'r tri fath o llwyrglo. Canolbwyntiwch ar y cylchred top a gwaelod yn unig. Os ydyn yn cynyddu'r cynhwysedd ciwio yn y nod gwaelod, rydym yn cynyddu'r amser nes llwyrglo yn y cylchred gwaelod. Fe allwn cynyddu'r cynhwysedd ciwio nes iddo cymryd mor hir i cyrraedd llwyrglo yn y cylchred gwaelod, ry' ni byth yn cyrraedd llwyrglo yn y cylchred yna, ac ond yn cyrraedd llwyrglo yn y cylchred top. Nid yw cynyddu'r cynhwysedd ciwio yn y gwaelod yn effeithio ar yr amser nes llwyrglo yn y cylchred top... ac felly gwelwn y gromlin yma.

---

Felly, crynodeb bach o'r gwaith:

Ry'n ni wedi ymchwilio i fewn i llwyrglo yn rhwydweithiau ciwio, ac focussu ar yr amser nes cyrraedd llwyrglo.
Ni wedi rhoi un dull i canfod llwyrglo mewn efelychiadau o rhwydweithiau ciwio.
Ac wedi adaeladu tri model Markov o rhwydweithiau ciwio syml sy'n cyrraedd llwyrglo.

---

Diolch yn fawr am gwrando.