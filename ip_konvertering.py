from functions import lag_ip_adresse,lag_subnet_maske, regn_nettverks_adresse, regn_kringkasting_adresse, regn_antall_verter 

def main():
    print("Velkommen til IP-adressekonverteringsprogrammet!")
    print("Dette programmet hjelper deg med å øve på subnetting og konvertering av IP-adresser.")

    valg = input("Ønsker du å øve på konvertering av IP-adresser? Skriv 'JA' for å øve. Skriv 'NEI' for å avslutte: ").lower().strip()

    while valg not in ["ja","nei"]:
        valg = input("Venligst skriven enten 'JA' for å øve eller 'NEI' for å avslutte").lower().strip()
                       

    while valg == "ja":

        ip_adresse = lag_ip_adresse()
        subnet_adresse,cidr = lag_subnet_maske()

        nettverks_adresse = regn_nettverks_adresse(ip_adresse,subnet_adresse)
        kringkasting_adresse = regn_kringkasting_adresse(ip_adresse,subnet_adresse)
        antall_verter = regn_antall_verter(cidr)
        cidr_notasjon = ip_adresse + "/" + str(cidr)

        antall_riktige = 0

        mulige_gjett = [["Hva er nettverksadressen? ", nettverks_adresse],["Hva er kringkastingsadressen? ", kringkasting_adresse], ["Hva er antall brukbare IP-adresser? ", antall_verter ], ["Skriv IP-adressen i CIDR-notasjon: ", cidr_notasjon]]

        for gjett_svar in mulige_gjett:
            svar = input(gjett_svar[0]).strip()
            if svar == gjett_svar[1]:
                antall_riktige +=1
                print("Hurra! Riktig svar.")
            else:
                print("Riktig svar er:", gjett_svar[1])
        
        print("Antall riktige denne runden:", antall_riktige)

        valg = input("Ønsker du å fortsette å øve på konvertering av IP-adresser? Skriv 'JA' for å øve. Skriv 'NEI' for å avslutte ").lower().strip()
        while valg not in ["ja","nei"]:
            valg = input("Venligst skriven enten 'JA' for å øve eller 'NEI' for å avslutte: ").lower().strip()

    print("Takk for at du brukte programmet!")
    ...

main()
