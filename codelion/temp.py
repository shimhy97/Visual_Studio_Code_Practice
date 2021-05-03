url = "https://www.wadiz.kr/web/campaign/detail/105474"



# res_list = [i for i, value in enumerate(url) if value == "/"]

# url = url.split("")
# backer_index = res_list[-3]+6

# url.insert(backer_index, 'Backer')

new_url = url.split('detail')[0] +'detailBacker'+url.split('detail')[1]



print(new_url)




