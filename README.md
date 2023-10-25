# GoogleTester
Seleniumi testid [Google](https://google.com) veebilehe jaoks. Teste tehakse Firefox brauseri abil.

Läbitakse järgmised testid:
1. Nõustu küpsistega - kontrollitakse, kas aken küpsiste kohta on nähtaval, klõpsatakse "Nõustu", kui jah
2. Tavaline otsing - sisestatakse märksõna otsinguväljale ja käivitatakse otsing, veendutakse, et otsinguleht on avanenud
3. _Ehk mul veab_ otsing - kontrollitakse, et _Ehk mul veab_ nupule klikkides minnakse esimese tulemuse lehele, mitte Google otsingulehele
4. Märksõna kustutamine - sisestatakse märksõna, proovitakse see ära kustutada otsinguvälja ilmuva ristikese abil
5. Esimesel tulemusel klõpsamine - siseneme märksõnaga otsingulehele, klõpsame esimesel tulemusel ja kontrollime, et oleme Google-st väljas

Testid läbitakse üksteise järel selles järjekorras, iga testi lõpus minnakse tagasi Google avalehele.
