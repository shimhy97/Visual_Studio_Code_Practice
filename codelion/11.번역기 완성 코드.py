from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력해주세요 : ")

def type_lang(sentence):
    try:
        lang = input("어떤 언어로 번역을 원하시나요? 코드를 입력하세요")
        #translate(번역을 원하는 문장,번역을 원하는 언어,src) dest = destination
        result = translator.translate(sentence,dest=lang)
        detected = translator.detect(sentence)
        return result,detected
    except:
        print("잘못된 언어 입력입니다. 다시 입력해주세요")
        type_lang(sentence)

gtrans_list = list(type_lang(sentence))
detected = gtrans_list[1]
result = gtrans_list[0]

print("===========출 력 결 과===========")
# detected.lang 우리가 감지한 언어가 어디 언어인가?
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=================================")