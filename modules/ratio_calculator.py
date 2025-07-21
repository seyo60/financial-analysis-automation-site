def toplam_hisse(pay_lot, ek_pay_lot):
    return (pay_lot if pay_lot is not None else 0) + (ek_pay_lot if ek_pay_lot is not None else 0)

def fk_orani(piyasa_fiyati: float, hisseBasiKar: float) -> float:
    return piyasa_fiyati / hisseBasiKar


def fd_divide_favok(
    kisaVadeli: float,
    uzun_vadeli_borclanma_kisa_vadeli: float,
    kiralama_borclarinin_kisa_vadeli_kismi: float,
    uzunVadeliBorc: float,
    uzun_vadeli_kiralama_borclari: float,
    net_kar: float,
    finansman_giderleri: float,
    amortismanVeItfaPaylari: float,
    donemOncesiVergiGelirGideri: float,
    piyasa_fiyati: float,
    toplam_hisse: int,
    nakit: float,
    finansal_yatirimlar: float
) -> float:
    try:
        # Temel kontroller
        if toplam_hisse <= 0 or piyasa_fiyati <= 0:
            return None

        # Piyasa değeri hesaplama
        piyasa_degeri = piyasa_fiyati * toplam_hisse
        
        # Net borç hesaplama
        toplam_borc = (kisaVadeli + uzun_vadeli_borclanma_kisa_vadeli + 
                       kiralama_borclarinin_kisa_vadeli_kismi + uzunVadeliBorc + uzun_vadeli_kiralama_borclari)
        net_borc = toplam_borc - (nakit + finansal_yatirimlar)

        

        fd = piyasa_degeri + net_borc
        
        # Firma değeri
        firma_degeri = piyasa_degeri + net_borc
        
        # FAVOK hesaplama
        favok = net_kar + donemOncesiVergiGelirGideri + finansman_giderleri + amortismanVeItfaPaylari

        
        # Oranın anlamlı olması için kontrol
        if favok <= 0 or firma_degeri <= 0:
            return None
            
        return fd / favok
        
    except Exception as e:
        raise ValueError(f"FD/FAVOK hesaplanırken hata: {str(e)}")


def pd_divide_dd(
    pay_lot: int, 
    ek_pay_lot: int, 
    piyasa_fiyati: float, 
    oz_kaynak: float
) -> float:
    try:
        # Toplam hisse ve değer kontrolleri
        toplam_hisse = pay_lot + ek_pay_lot
        if toplam_hisse <= 0 or oz_kaynak <= 0 or piyasa_fiyati <= 0:
            return None
            
        piyasa_degeri = piyasa_fiyati * toplam_hisse
        return piyasa_degeri / oz_kaynak
        
    except Exception as e:
        raise ValueError(f"PD/DD hesaplanırken hata: {str(e)}")
    
def carioran(donenVarliklar, kisaVadeliYukumlulukler):
    return (donenVarliklar)/(kisaVadeliYukumlulukler)

def asittestorani(donenVarliklar, stoklar, kisaVadeli, uzun_vadeli_borclanma_kisa_vadeli, ticariBorclar, calisanlaraIliskinYukumlulukler, digerBorclar, ertelenmisGelirler, kisaVadeliKarsiliklar):
    return (donenVarliklar-stoklar)/(kisaVadeli + uzun_vadeli_borclanma_kisa_vadeli + ticariBorclar + calisanlaraIliskinYukumlulukler + digerBorclar + ertelenmisGelirler + kisaVadeliKarsiliklar)

def borctoplamvarlik(donenVarliklar, duranVarliklar, kisaVadeliYukumlulukler, uzunVadeliYukumlulukler):
    return ((kisaVadeliYukumlulukler + uzunVadeliYukumlulukler)/(donenVarliklar + duranVarliklar))*100

def finansalkaldiracorani(kisaVadeliYukumlulukler, uzunVadeliYukumlulukler, toplamVarliklar):
    return (kisaVadeliYukumlulukler + uzunVadeliYukumlulukler)/(toplamVarliklar)

def netkarmarji(netKar, hasilat):
    return (netKar/hasilat)*100

def aktifkarlilik(netKar, donenVarlik, duranVarlik):
    return (netKar/(donenVarlik + duranVarlik))*100

def ozsermayekarliligi(netKar, ozKaynak):
    return (netKar / ozKaynak)*100

def alacakdevirhizi(hasilat, ticariAlacaklar_son):
    return 365/(ticariAlacaklar_son/hasilat*365)

def stokdevirhizi(satilanMalinMaliyeti, stoklar_son):
    return 365/(stoklar_son/satilanMalinMaliyeti*365)
