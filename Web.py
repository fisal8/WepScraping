import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.ae/Casio-Mens-Watch-MTP-1374D-1AVDF-Silver/dp/B00GRRIZK2/ref=sr_1_8?crid=AU4YFSK9V7BB&dib=eyJ2IjoiMSJ9.o-JTfjLcfFx0JbpgVtIaIGzx45-cFFLJdlNHeGjBzjXMpcGvqA3U6gWPjn8z_JTA7_t4mTOx_Ttx0sUX1AweaJgp903bJpL85RVJv2CLRbDpomPdlH5Q4ocqF5SeDjnrP-pKdyEBti7T1izHTuoDlhlXavCJqJ1O_cVkX4u7c9IOK5NMcjeeyw5TjYMWICKuHpI4dftrk7SA-NUo5-m0TDJBCerM6xdcnV1f9a2I-oTg0C_MXl3AwJnIhwNLJxF5SMjpSVxN8s6Dh40UGmILHyYy5UOPYxaJpQBoNfxx3RCG4KH8xILpTLi7ZU5ZDl74XZyoiHIeturkM1hp1jRAChdRFP1s2M4EM0jRznwOPU2M7QYaZD7r8ybp1QDIVLn96-_RDClh-tFVg0svwxzbNy8kjaoU2Njp8FQ61AiVTMEGeVLIPbTkoRCoQtplkriC.u5-F1G2XZ9otl8FBm3jtpYJj8lbjVeEQaYUZbfP6Hjc&dib_tag=se&keywords=ساعه+يد&qid=1737295095&sprefix=ساعه+يد%2Caps%2C139&sr=8-8'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'}
response= requests.get(url, headers=headers, params={'k':'ساعه+يد'})

soup = BeautifulSoup(response.text, 'html.parser')

title= soup.find("span", id='productTitle')

print(title.string.strip())

tech_details = {}
table = soup.find("table", id='technicalSpecifications_section_1')

rows = table.find_all('tr')
for row in rows:
    key =  row.th.text.strip()
    value = row.td.text.strip()
    tech_details[key] = value

print(title.string.strip())
print(tech_details)
