import requests  
import yfinance as yf
from flask import Flask, render_template
import os





app = Flask(__name__, template_folder="templates")


@app.route("/")  
def home():
    
    
    """ kripto """
    crypto_symbols = [
    "BTC-USD", "ETH-USD", "XRP-USD", "USDT-USD", "SOL-USD", "BNB-USD", "DOGE-USD", "USDC-USD", "ADA-USD", "TRX-USD",
    "AVAX-USD", "LINK-USD", "LTC-USD", "DOT-USD", "MATIC-USD", "SHIB-USD", "UNI-USD", "FTT-USD", "ALGO-USD", "ICP-USD"]
    """ abd """
    usstocks = [ 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'META', 'TSLA', 'NVDA', 'PYPL', 'NFLX', 'ADBE', 'INTC', 'CSCO', 'PEP', 'CMCSA', 'AVGO', 'COST', 'TMUS', 'TXN', 'QCOM', 'AMGN', 'HON', 'SBUX', 'INTU', 'AMD', 'MDLZ', 'ISRG', 'GILD', 'BKNG', 'ADI', 'VRTX', 'REGN', 'LRCX', 'MU', 'CSX', 'MRNA', 'CHTR', 'MAR', 'KLAC', 'PANW', 'ORLY', 'MNST', 'SNPS', 'ASML', 'CDNS', 'ADP', 'CTAS', 'WDAY', 'NXPI', 'KDP', 'MELI', 'PDD', 'ROST', 'AEP', 'DXCM', 'IDXX', 'BIIB', 'ALGN', 'EXC', 'EA', 'XEL', 'MCHP', 'MRVL', 'AZN', 'DLTR', 'CTSH', 'FAST', 'VRSK', 'CPRT', 'WBA', 'ILMN', 'LULU', 'KHC', 'PAYX', 'CRWD', 'ODFL', 'BIDU', 'JD', 'PCAR', 'SIRI', 'ZM', 'TEAM', 'ANSS', 'DDOG', 'ZS', 'SWKS', 'FANG', 'TTD', 'OKTA', 'MTCH', 'PTON', 'DOCU', 'VRSN', 'NTES', 'SE', 'LCID', 'RIVN']
    """ tr """
    turkk=[
      'ACSEL.IS', 'AEFES.IS', 'AFYON.IS', 'AGHOL.IS', 'AHGAZ.IS', 'AKBNK.IS', 'AKCNS.IS', 'AKENR.IS', 'AKFGY.IS', 'AKSA.IS', 'AKSEN.IS', 'ALARK.IS', 'ALFAS.IS', 'ALGYO.IS', 'ALKA.IS', 'ALMAD.IS', 'ANELE.IS', 'ANHYT.IS', 'ANSGR.IS', 'ARDYZ.IS', 'ARZUM.IS', 'ASELS.IS', 'ATAGY.IS', 'ATATP.IS', 'ATEKS.IS', 'ATSYH.IS', 'AVGYO.IS', 'AVHOL.IS', 'AYDEM.IS', 'AYEN.IS', 'AZTEK.IS', 'BAGFS.IS', 'BAKAB.IS', 'BALAT.IS', 'BANVT.IS', 'BASCM.IS', 'BAYRK.IS', 'BERA.IS', 'BEYAZ.IS', 'BIMAS.IS', 'BIOEN.IS', 'BIZIM.IS', 'BOBET.IS', 'BOSSA.IS', 'BRISA.IS', 'BRKSN.IS', 'BRMEN.IS', 'BSOKE.IS', 'BURCE.IS', 'BUCIM.IS', 'CANTE.IS', 'CASA.IS', 'CEMTS.IS', 'CEOEM.IS', 'CIMSA.IS', 'CMBTN.IS', 'CMENT.IS', 'CONSE.IS', 'COSMO.IS', 'CRDFA.IS', 'CRFSA.IS', 'CUSAN.IS', 'DAGHL.IS', 'DAGI.IS', 'DARDL.IS', 'DESPC.IS', 'DERIM.IS', 'DERHL.IS', 'DESA.IS', 'DGATE.IS', 'DGGYO.IS', 'DIRIT.IS', 'DITAS.IS', 'DMSAS.IS', 'DOAS.IS', 'DOBUR.IS', 'DOGUB.IS', 'DOHOL.IS', 'DOKTA.IS', 'DURDO.IS', 'ECILC.IS', 'EGEEN.IS', 'EGGUB.IS', 'EGPRO.IS', 'EKGYO.IS', 'EMKEL.IS', 'ENJSA.IS', 'ENKAI.IS', 'ERCB.IS', 'EREGL.IS', 'ESCOM.IS', 'ETILR.IS', 'EUHOL.IS', 'EUKYO.IS', 'FADE.IS', 'FENER.IS', 'FLAP.IS', 'FMIZP.IS', 'FONET.IS', 'FORMT.IS', 'FROTO.IS', 'GARAN.IS', 'GEDIK.IS', 'GEDZA.IS', 'GENTS.IS', 'GEREL.IS', 'GLCVY.IS', 'GLYHO.IS', 'GOLTS.IS', 'GOODY.IS', 'GOZDE.IS', 'GRSEL.IS', 'GSRAY.IS', 'GUBRF.IS', 'HALKB.IS', 'HATEK.IS', 'HDFGS.IS', 'HEKTS.IS', 'HLGYO.IS', 'HUBVC.IS', 'ICBCT.IS', 'IDGYO.IS', 'IHGZT.IS', 'IHEVA.IS', 'IHLGM.IS', 'IHYAY.IS', 'INDES.IS', 'INFO.IS', 'INTEM.IS', 'ISBIR.IS', 'ISCTR.IS', 'ISKPL.IS', 'ISMEN.IS', 'IZINV.IS', 'IZMDC.IS', 'JANTS.IS', 'KAREL.IS', 'KARSN.IS', 'KARTN.IS', 'KATMR.IS', 'KAYSE.IS', 'KCAER.IS', 'KENT.IS', 'KERVT.IS', 'KLRHO.IS', 'KLMSN.IS', 'KMPUR.IS', 'KONTR.IS', 'KORDS.IS', 'KOZAA.IS', 'KOZAL.IS', 'KRGYO.IS', 'KRPLS.IS', 'KSTUR.IS', 'KTSKR.IS', 'KUTPO.IS', 'KUYAS.IS', 'LIDFA.IS', 'LKMNH.IS', 'LOGO.IS', 'LUKSK.IS', 'MAALT.IS', 'MAKIM.IS', 'MAKTK.IS', 'MANAS.IS', 'MARKA.IS', 'MARTI.IS', 'MAVI.IS', 'MEPET.IS', 'MERKO.IS', 'MIATK.IS', 'MMCAS.IS', 'MPARK.IS', 'MRGYO.IS', 'MTRKS.IS', 'NETAS.IS', 'NIBAS.IS', 'NTHOL.IS', 'NUGYO.IS', 'NUHCM.IS', 'ODAS.IS', 'ORGE.IS', 'OTKAR.IS', 'OYYAT.IS', 'OZRDN.IS', 'PAGYO.IS', 'PAPIL.IS', 'PARSN.IS', 'PCILT.IS', 'PEKGY.IS', 'PETKM.IS', 'PGSUS.IS', 'PKENT.IS', 'PLTUR.IS', 'PNSUT.IS', 'POLHO.IS', 'POLTK.IS', 'PRDGS.IS', 'PRKAB.IS', 'PRZMA.IS', 'PSDTC.IS', 'QUAGR.IS', 'RALYH.IS', 'RAYSG.IS', 'RODRG.IS', 'RUBNS.IS', 'SAFKR.IS', 'SAHOL.IS', 'SANEL.IS', 'SANKO.IS', 'SANFM.IS', 'SARKY.IS', 'SASA.IS', 'SAYAS.IS', 'SELEC.IS', 'SILVR.IS', 'SKTAS.IS', 'SMRTG.IS', 'SNGYO.IS', 'SNKRN.IS', 'SOKM.IS', 'SONME.IS', 'SUNTK.IS', 'TATGD.IS', 'TAVHL.IS', 'TBORG.IS', 'TCELL.IS', 'THYAO.IS', 'TKFEN.IS', 'TKNSA.IS', 'TLMAN.IS', 'TMPOL.IS', 'TMSN.IS', 'TOASO.IS', 'TSKB.IS', 'TTKOM.IS', 'TTRAK.IS', 'TUCLK.IS', 'TUKAS.IS', 'TUPRS.IS', 'UFUK.IS', 'ULAS.IS', 'ULKER.IS', 'ULUUN.IS', 'UNLU.IS', 'VAKBN.IS', 'VAKFN.IS', 'VAKKO.IS', 'VESTL.IS', 'VKGYO.IS', 'YAPRK.IS', 'YATAS.IS', 'YBTAS.IS', 'YGGYO.IS', 'YUNSA.IS', 'YYAPI.IS', 'ZOREN.IS']
   
    def fetch_data(symbols):
      
     crepto_dt=[]
     for symbol in symbols:
       try:
          

         tce=yf.Ticker(symbol)
         a= tce.history(period="1d")
         if not a.empty: 
            b=round( a["Close"].iloc[-1],3 )
            crepto_dt.append({"name": symbol , "price": b })
         else:
            print(f"tekrar deneyin {symbol} ")
       except Exception as e:
         print(f"hata oluştu tekrar deneyiniz {symbol} ")

     return crepto_dt
    """ kripto """
    crypto_data= fetch_data(crypto_symbols)
    """ abd borsası """
    usabd=fetch_data(usstocks)
    """ tr bist borsası """
    trist=fetch_data(turkk)
          
    return render_template("hm.html" , crypto=crypto_data , us=usabd ,bist=trist )
    



if __name__ == "__main__":
    app.run(debug=True)
