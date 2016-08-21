import tweepy
import time
import csv

auth = tweepy.OAuthHandler('jAzSxPFvOq2GIuXvNMNjJoB9e', 'GnOSfYMzQbrtfuY3lvxdJuqRFqBneRh6AghRIOea5EOVCvzoMf') 
auth.set_access_token('612416835-wEMoMN1R49XDZl8FuCNqI6Y3jdHPDChhqZOkJ9Ut', 'jmR7Udd0HhLPJE8wrrIBis1XzLKgZhZrKqqDY1Xgpnlab')    
api = tweepy.API(auth)

cfr = api.get_user('cfr_iigg')

# followers, followers_count, followers_ids,
# following, friends, friends_count, id, id_str, 
# screen_name, status, statuses_count
# cfr.status.created_at.day (.year, .month)

# 
# for item in items:
#     not_finished=True
#     while not_finished:
#         try:
# #            code
#             not_finished=False
#         except:
#             time.sleep(1)

## MOST ACTIVE = STATUSES_COUNT (total number of statuses)
cfr_fol_ids = []
for f in cfr.followers_ids():
	try:
		cfr_fol_ids.append([f])
	except:
		print "Error with follower id: %s, sleeping and trying again" %(f)
		time.sleep(5)

## most active among followers of target

cfr_fol_statuses = []
def get_fol_statuses(status_list, start_index):
	for index in range(start_index,len(cfr_fol_ids)):
		try:
			usr = api.get_user(id[0])
			stat_count = usr.statuses_count
			status_list.append(stat_count)
		except:
			print "Error getting status count for follower id: %s (index #%s), sleeping and trying again" %(cfr_fol_ids[index],index)
			time.sleep(10)
			get_fol_statuses(status_list, index)
	return status_list

cfr_fol_statuses = get_fol_statuses(cfr_fol_statuses, 0)

## most popular (greatest # followers) among target's followers
cfr_fol_fol_ids = []
## first - getting all followers' followers (will need it later)
# to solve this problem, just need to count
def get_fol_fols(fol_fol_id_list, start_index):
	for index in range(start_index,len(cfr_fol_ids)):
		try:
			fol_fol_id_list[index] = []
			usr = api.get_user(id[0])
			fol_ids = usr.follower_ids()
			fol_fol_id_list[index] = fol_ids
		except:
			print "Error getting status count for follower id: %s (index #%s), sleeping and trying again" %(cfr_fol_ids[index],index)
			time.sleep(10)
			get_fol_fols(fol_fol_id_list, index)
	return fol_fol_id_list

cfr_fol_fol_ids = get_fol_fols(cfr_fol_fol_ids, 0)

## most active layman, expert, and celebrity among target's friends

def: get_friend_ids():
	try:
		cfr_friend_ids = []
		cfr_friend_ids = cfr.friends_ids()
		return cfr_friend_ids
	except:
		print "error, trying again"
		time.sleep(10)
		get_friend_ids()
		

# 
# cfr_friend_ids = []
# for f in cfr.followers_ids():
# 	try:
# 		cfr_fol_ids.append([f])
# 	except:
# 		print "Error with follower id: %s, sleeping and trying again" %(f)
# 		time.sleep(5)
# 

## most popular among friends of target



## (limit the following to laymen (<100 followers) and experts (100-1000))

## most active among followers of target and their followers


## most active among followers of target and their friends




### writing to csv


c = open('cfr_twitter.csv','wb')
c_writer = csv.writer(c)
c_writer.writerow(["follower ID", "follower user name", "number of statuses" "number of followers"])

for i in range(len(:
	try:
		c_writer.writerow([p[0], p[2], p[3], p[4]])
	except:
		print "ERROR: " + p[0] + '\n'
		pass

c.flush()
c.close()
