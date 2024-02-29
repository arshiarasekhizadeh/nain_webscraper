from de import get_product_data_de , get_product_links_de
from dk import get_product_data_dk , get_product_links_dk
from en import get_product_data_en , get_product_links_en
from es import get_product_data_es , get_product_links_es
from fi import get_product_data_fi , get_product_links_fi
from fr import get_product_data_fr , get_product_links_fr
from it import get_product_data_it , get_product_links_it
from jp import get_product_data_jp , get_product_links_jp
from nl import get_product_data_nl , get_product_links_nl
from no import get_product_data_no , get_product_links_no
from pt import get_product_data_pt , get_product_links_pt
from se import get_product_data_se , get_product_links_se


url_de = 'https://www.naintrading.com/orientteppiche/traditionell-c-317.html?p=400'
url_dk = 'https://www.naintrading.dk/orientalske-taepper/traditional-c-317.html?p=400'
url_en = 'https://www.naintrading.co.uk/oriental-carpets/traditional-c-317.html?p=400'
url_es = 'https://www.naintrading.es/alfombras-orientales/traditional-c-317.html?p=400'
url_fi = 'https://www.naintrading.fi/itamaiset-matot/traditional-c-317.html?p=400'
url_fr = 'https://www.naintrading.fr/tapis-orientaux/traditional-c-317.html?p=400'
url_it = 'https://www.naintrading.it/tappeti-orientali/traditional-c-317.html?p=400'
url_jp = 'https://www.naintrading.jp/orientaru-jutan/traditional-c-317.html?p=400'
url_nl = 'https://www.naintrading.nl/oosterse-tapijten/traditionele-perzische-oosterse-tapijten-c-317.html?p=400'
url_no = 'https://www.naintrading.co.no/orientalske-tepper/traditional-c-317.html?p=400'
url_pt = 'https://www.naintrading.pt/tapetes-orientais/traditional-c-317.html?p=400'
url_se = 'https://www.naintrading.se/orientaliska-mattor/traditionella-persiska-och-orientaliska-mattor-c-317.html?p=400'


user_selected_languge = input('chose the language you need data in [de , dk , en , es , fi , fr , it , jp , nl , no , pt , se]\ntype all to get data for all languages\n')
if user_selected_languge == 'de' : 
    de_links = get_product_links_de.get_product_links_de(url_de)
    get_product_data_de.get_product_data_de(de_links)
elif user_selected_languge == 'dk' : 
    dk_links = get_product_links_dk.get_product_links_dk(url_dk)
    get_product_data_dk.get_product_data(dk_links)
elif user_selected_languge == 'en' : 
    en_links = get_product_links_en.get_product_links(url_en)
    get_product_data_en.get_product_data(en_links)
elif user_selected_languge == 'es' : 
    es_links = get_product_links_es.get_product_links(url_es)
    get_product_data_es.get_product_data(es_links)
elif user_selected_languge == 'fi' : 
    fi_links = get_product_links_fi.get_product_links(url_fi)
    get_product_data_fi.get_product_data(fi_links)
elif user_selected_languge == 'fr' : 
    fr_links = get_product_links_fr.get_product_links(url_fr)
    get_product_data_fr.get_product_data(fr_links)
elif user_selected_languge == 'it' : 
    it_links = get_product_links_it.get_product_links(url_it)
    get_product_data_it.get_product_data(it_links)
elif user_selected_languge == 'jp' : 
    jp_links = get_product_links_jp.get_product_links(url_jp)
    get_product_data_jp.get_product_data(jp_links)
elif user_selected_languge == 'nl' : 
    nl_links = get_product_links_nl.get_product_links(url_nl)
    get_product_data_nl.get_product_data(nl_links)
elif user_selected_languge == 'no' : 
    no_links = get_product_links_no.get_product_links(url_no)
    get_product_data_no.get_product_data(no_links)
elif user_selected_languge == 'pt' : 
    pt_links = get_product_links_pt.get_product_links(url_pt)
    get_product_data_pt.get_product_data(pt_links)
elif user_selected_languge == 'se' : 
    se_links = get_product_links_se.get_product_links(url_se)
    get_product_data_se.get_product_data(se_links)
elif user_selected_languge == 'all' :
    de_links = get_product_links_de.get_product_links_de(url_de)
    get_product_data_de.get_product_data_de(de_links)
    dk_links = get_product_links_dk.get_product_links_dk(url_dk)
    get_product_data_dk.get_product_data(dk_links)
    en_links = get_product_links_en.get_product_links(url_en)
    get_product_data_en.get_product_data(en_links)
    es_links = get_product_links_es.get_product_links(url_es)
    get_product_data_es.get_product_data(es_links)
    fi_links = get_product_links_fi.get_product_links(url_fi)
    get_product_data_fi.get_product_data(fi_links)
    fr_links = get_product_links_fr.get_product_links(url_fr)
    get_product_data_fr.get_product_data(fr_links)
    it_links = get_product_links_it.get_product_links(url_it)
    get_product_data_it.get_product_data(it_links)
    jp_links = get_product_links_jp.get_product_links(url_jp)
    get_product_data_jp.get_product_data(jp_links)
    nl_links = get_product_links_nl.get_product_links(url_nl)
    get_product_data_nl.get_product_data(nl_links)
    no_links = get_product_links_no.get_product_links(url_no)
    get_product_data_no.get_product_data(no_links)
    pt_links = get_product_links_pt.get_product_links(url_pt)
    get_product_data_pt.get_product_data(pt_links)
    se_links = get_product_links_se.get_product_links(url_se)
    get_product_data_se.get_product_data(se_links)