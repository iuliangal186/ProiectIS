**Document de analiză a cerințelor clientului**

**Sera Smart – Echipa 17**

## Scopul aplicației: 
*Aplicatia are ca scop modificarea serei traditionale prin automatizarea acesteia, folosindu-se de date de natura variabila pe care le preia din mediul inconjurator (lumina, temperatura, umiditate etc.). Aceasta aplicatie poate fi rulata si parametrii pot fi modificati de catre utilizator remote prin intermediul telefonului/desktopului si va oferi un feedback in timp real a conditiilor din sera.*

## Obiectivele aplicației:
- Sera va avea ca scop maximizarea cantitatii de recolta din interiorul acesteia de-a lungul timpului.
- Aceasta va economisi resursele neregenerabile folosite si timpul persoanei care o detine/opereaza. 
- Aplicatia ar trebui sa fie usor de folosit si foarte intuitiva*.*


## Grupul țintă
Aplicatia se adreseaza agricultorilor, dar si amatorilor pasionati de legumicultura, ce cauta sa isi automatizeze propriile culturi.

- Ca agricultor, as vrea sa pot sa accesez o serie de statistici relevante despre sera, pentru a optimiza calitatea viitoarei recolte.
- Ca agricultor, as vrea sa pot modifica parametrii din interior, precum umiditatea solului, temperatura aerului, cantitatea de lumina, pentru a influenta recolta. 
- Ca utilizator, mi-ar fi foarte util ca aplicatia sa fie foarte usor de folosit.
- Ca legumicultor amator, as dori sa pot sa ma descurc cu sera intr-un mod cat mai necostisitor.


## Colectarea cerințelor

- prezenta unui spatiu de stocare ce retine in timp datele senzorilor si compileaza statistici pe baza lor.
- folosirea unui numar minim de senzori de temperatura, umiditate, lumina.
- accesarea unui api extern pentru preluarea datelor metereologice.
- citirea unui senzor de temperatura.
- citirea unui senzor de umiditate.
- citirea unui senzor de lumina.
- citirea unui senzor de miscare.
- performanta sistemului nu este critica.
- conexiunea la internet.
- crearea unei interfete minimaliste.
- adaptarea aplicatiei atat pe mobil cat si pe desktop.


## Interpretarea și prioritizarea cerințelor

*1. Label-uiți cerințele funcționale / non-funcționale.* 

- prezenta unui spatiu de stocare ce retine in timp datele senzorilor si compileaza statistici pe baza lor.      **Functional**
- folosirea unui numar minim de senzori de temperatura, umiditate, lumina.  **Nonfunctional**
- accesarea unui api extern pentru preluarea datelor metereologice.  **Functional**
- citirea unui sensor de temperatura.       **Functional**
- citirea unui sensor de umiditate.            **Functional**
- citirea unui sensor de lumina.        **Functional**
- citirea unui sensor de miscare.        **Functional**
- performanta sistemului nu este critica.    **Nonfunctional**
- conexiunea la internet.            **Functional**
- crearea unei interfete minimaliste. **Nonfunctional**
- adapatarea aplicatiei atat pe mobil cat si pe desktop. **Nonfunctional**
- accesarea sistemului prin HTTP  **Functional**
- implementarea serverului prin tehnologia MQTT   **Functional**



*2. Gruparea cerințelor*

**STOCAREA DATELOR**

- prezenta unui spatiu de stocare ce retine in timp datele senzorilor si compileaza statistici pe baza lor.

**PERFORMANTA** 

- folosirea unui numar minim de senzori de temperatura, umiditate, lumina.
- crearea unei interfete minimaliste.
- performanta sistemului nu este critica.

**FUNCTIONABILITATE**

- adapatarea aplicatiei atat pe mobil cat si pe desktop.
- conexiunea la internet.

**APIs**

- accesarea unui api extern pentru preluarea datelor metereologice.

**CITIREA SI PRELUCRAREA DATELOR**

- citirea unui sensor de temperatura.
- citirea unui sensor de umiditate. 
- citirea unui sensor de lumina.        
- citirea unui sensor de miscare. 




*3. Proiectul de github creat* 

*4. Play planning poker.* 

**Poker planning dupa dificultate**:
1. prezenta unui spatiu de stocare ce retine in timp datele senzorilor si compileaza statistici pe baza lor. Functional 3 3 3 4 = 3.25
2. folosirea unui numar minim de senzori de temperatura, umiditate, lumina. Nonfunctional 1 2 1 2 = 1.50
3. accesarea unui api extern pentru preluarea datelor metereologice. Functional 2 3 2 3 = 2.50 
4. citirea unui sensor de temperatura. Functional 2 2 2 2 = 2 
5. citirea unui sensor de umiditate. Functional 2 2 2 2 = 2 
6. citirea unui sensor de lumina. Functional 2 2 2 2 = 2 
7. citirea unui sensor de miscare. Functional 2 2 2 2 = 2 
8. performanta sistemului nu este critica. Nonfunctional 1 1 1 2 = 1.25 
9. conexiunea la internet. Functional 4 2 1 3 =2.50 
10. crearea unei interfete minimaliste. Nonfunctional 3 3 3 4 =3.25 
11. adapatarea aplicatiei atat pe mobil cat si pe desktop. Nonfunctional 5 5 5 4 = 4.75

**Poker planning dupa prioritate**:
1. prezenta unui spatiu de stocare ce retine in timp datele senzorilor si compileaza statistici pe baza lor. Functional 3 3 3 4 = 3.25; Prioritate= 5 5 5 5 = 5 
2. folosirea unui numar minim de senzori de temperatura, umiditate, lumina. Nonfunctional 1 2 1 2 = 1.50; Prioritate= 1 1 3 5 = 2.5 
3. accesarea unui api extern pentru preluarea datelor metereologice. Functional 2 3 2 3 = 2.50; Prioritate= 4 5 4 4 = 4.25 
4. citirea unui sensor de temperatura. Functional 2 2 2 2 = 2; Prioritate= 3 4 4 3 = 3.50
5. citirea unui sensor de umiditate. Functional 2 2 2 2 = 2; Prioritate= 3 4 4 3 = 3.50 
6. citirea unui sensor de lumina. Functional 2 2 2 2 = 2; Prioritate= 3 4 4 3 = 3.50 
7. citirea unui sensor de miscare. Functional 2 2 2 2 = 2; Prioritate= 3 4 4 3 = 3.50 
8. performanta sistemului nu este critica. Nonfunctional 1 1 1 2 = 1.25; Prioritate= 1 1 2 2 = 1.50 
9. conexiunea la internet. Functional 4 2 1 3 =2.50; Prioritate= 3 5 5 3 = 4 
10. crearea unei interfete minimaliste. Nonfunctional 3 3 3 4 =3.25; Prioritate= 3 2 2 2 = 2.25
11. adapatarea aplicatiei atat pe mobil cat si pe desktop. Nonfunctional 5 5 5 4 = 4.75; Prioritate= 1 2 3 3 = 2.25

*5. Plot the issues.* 
![Axa Dificultate/Prioritate](https://cdn.discordapp.com/attachments/899336393657036871/902527635400327198/Screenshot_2021-10-26_150217.png)
